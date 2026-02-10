참고 문헌

- https://github.com/apache/superset
- https://superset.apache.org/

---

# Apache Superset: 데이터 탐색과 시각화를 위한 오픈 소스 BI 툴

## Apache Superset란?

- 데이터 탐색과 시각화를 위한 오픈소스 BI 플랫폼이다.
- Apache Software Foundation의 산하 프로젝트로 관리되며, `Python` 을 기반으로 함. (Flask, Pandas, SQLAlchemy 등과 같은 라이브러리 사용)
- 웹 기반 인터페이스를 통해 데이터를 연결하고, 복잡한 대시보드를 생성하며, 다양한 데이터베이스와 쉽게 통합할 수 있도록 생성됨.
- SQL 중심 분석과 노코드/로우코드 시각화를 함께 제공한다.

## 주요 기능

- 다양한 데이터 소스 지원: `SQL` 기반 데이터 소스와의 연결을 지원하기 때문에, 거의 모든 데이터베이스에 접근할 수 있다.
- 인터랙티브 대시보드: 드래그 앤 드롭 인터페이스를 통해 인터랙티브한 대시보드를 손쉽게 구성할 수 있다.
- 대용량 데이터 시각화: 수백만~수십억 행 규모에서도 빠른 집계와 차트 렌더링이 가능하다.
- 강력한 시각화 도구: 다양한 시각화 옵션을 제공한다.
- 보안 기능: 강력한 보안 기능을 통해 데이터와 대시보드의 접근을 제어할 수 있다.
  - 사용자/역할/권한 관리
  - Row/Column Level Security

## 지원 데이터 소스

- 관계형 DB: MySQL, PostgreSQL, Oracle, SQL Server
- 분석형 DB/엔진: ClickHouse, Presto/Trino, Apache Druid
- 클라우드 DW: BigQuery, Snowflake, Redshift
- 기타: SQLite, Hive 등

→ **\*SQLAlchemy** 커넥터 기반으로 확장 가능

## 기술 아키텍처

- **Backend**: Python (Flask), SQLAlchemy
- **Frontend**: React, Ant Design
- **Async 처리**: *Celery + *Redis/RabbitMQ (대시보드 쿼리 비동기화 = 무거운 쿼리는 뒤에서 돌리고, 화면은 안 멈추게 하는 구조)
- **캐싱**: Redis/Memcached로 응답 속도 향상

## 특징

### **장점**

- 오픈소스이므로 특정 회사 라이선스에 묶이지 않는다. (=벤더 종속성이 낮음)
- 표준 SQL을 기반으로 하기때문에, DB가 바뀌어도 쿼리 개념을 유지한다.
- DB에 독립적이기 때문에 DBSM이 바뀌어도 계속 사용할 수 있다.
- 대규모 데이터에 적합하다.
- 별도 ETL 없이 기존 분석용 DB에 바로 연결한다.

### 단점

- 초기 설정에 난이도가 있다. (권한/커넥터/캐시 설정)
  예시) 권한을 RBAC으로 세팅한다.
  1. 누가 어떤 대시보드를 볼 수 있는지
  2. 누가 DB에 접근 가능한지
  3. 누가 SQL Lab에서 쿼리를 실행할 수 있는지
- Excel 수준의 셀 단위 조작에는 부적합하다. → Superset은 데이터를 고치는 도구가 아닌 데이터에서 인사이트를 보여주는 도구.
- 고급 데이터 모델링은 외부도구와 병행이 필요하다.

## 실습코드

\*Superset은 CLI 명령어로 서버를 띄우는 웹앱.
*윈도우기준

0. (권장) 가상환경 생성 및 활성화

Superset은 의존성이 무겁고 충돌이 잦아서 전용 가상환경을 추천한다.
```
conda create -n superset-env python=3.9 -y
conda activate superset-env
```

1. Superset 설치
```
pip install apache-superset
```

3. 환경변수 설정 (Windows 기준)

Superset CLI가 Flask 앱을 인식하도록 FLASK_APP를 지정한다.
Windows에서는 export가 아니라 set을 사용한다.

```
set FLASK_APP=superset
```

3. (중요) SECRET_KEY 설정

최근 Superset은 기본(불안전) SECRET_KEY 감지 시 실행을 거부할 수 있다.
이를 방지하기 위해 Superset 설정 파일을 만들어 SECRET_KEY를 명시한다.

3-1) 설정 폴더/파일 만들기
```
mkdir %USERPROFILE%\.superset
```


`C:\Users\<사용자>\.superset\superset_config.py` 파일을 만들고 아래 한 줄을 작성한다.

SECRET_KEY = "change_this_to_a_long_random_string_please_50_chars_minimum_1234567890"

3-2) Superset이 설정 파일을 읽도록 경로 지정
```
set SUPERSET_CONFIG_PATH=%USERPROFILE%\.superset\superset_config.py
```

4. Superset 내부 DB 마이그레이션 (초기화 1단계)

Superset은 내부 메타데이터(사용자/대시보드/권한 등)를 저장하기 위한 내부 DB를 사용한다(기본은 SQLite).
처음 설치하면 마이그레이션이 필요하다.

```
superset db upgrade
```


정상 예시:

`Migration scripts completed` 같은 로그가 출력됨

5. 관리자 계정 생성 (초기화 2단계)

웹 UI 로그인에 사용할 관리자 계정을 만든다.
여기서 입력하는 값은 내 DB 계정이 아니라 Superset 로그인 계정이다.

`superset fab create-admin`

```
Username = 로그인 ID (예: admin 또는 jungyeon)

Password 입력 시 화면에 표시가 안 되는 것이 정상(별표도 안 뜸)
```

6. Superset 초기 설정 로딩 (초기화 3단계)

기본 역할/권한 및 샘플 설정 등을 반영한다.

```
superset init
```

7. Superset 서버 실행

로컬 서버를 띄워서 브라우저에서 접속한다.

```
superset run -p 8088 --with-threads --reload --debugger
```


브라우저 접속:

```
http://localhost:8088
```

<p align="center">
  <img src="https://github.com/user-attachments/assets/0ed62db2-6817-4112-8d23-d2b6629b8108" width="700"/>
</p>

<p align="center">
  <em>Apache Superset 초기 실행 화면 (localhost:8088)</em>
</p>

다음과 같이 서버에 접속한 것을 확인할 수 있다!


⚠️ **자주 나는 문제**
* Refusing to start due to insecure SECRET_KEY
superset_config.py에 SECRET_KEY 추가 + SUPERSET_CONFIG_PATH 설정 필요

---

**\*SQLAlchemy: 파이썬 코드로 SQL를 다루게 해주는 DB 추상화 라이브러리**

**\*Celery: 백그라운드 작업을 처리하는 파이썬 워커 시스템으로, 웹 서버와 분리되어 있다.**

**\*Redis/RabbitMQ: Task Queue로, 쿼리를 실행해달라는 요청을 저장하고, `Celery` 워커들이 하나씩 꺼내서 처리한다.**

**\*ETL: Extract-Transform-Load → 분석하기 좋게 데이터를 정리해서 DB에 적재하는 과정**

**\*RABC(Role-Based Access Control): 사람마다 볼 수 있는 데이터와 할 수 있는 행동을 역할로 통제하는 것**
