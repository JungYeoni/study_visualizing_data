https://github.com/apache/superset

https://superset.apache.org/

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

---

**\*SQLAlchemy: 파이썬 코드로 SQL를 다루게 해주는 DB 추상화 라이브러리**

**\*Celery: 백그라운드 작업을 처리하는 파이썬 워커 시스템으로, 웹 서버와 분리되어 있다.**

**\*Redis/RabbitMQ: Task Queue로, 쿼리를 실행해달라는 요청을 저장하고, `Celery` 워커들이 하나씩 꺼내서 처리한다.**

**\*ETL: Extract-Transform-Load → 분석하기 좋게 데이터를 정리해서 DB에 적재하는 과정**

**\*RABC(Role-Based Access Control): 사람마다 볼 수 있는 데이터와 할 수 있는 행동을 역할로 통제하는 것**
