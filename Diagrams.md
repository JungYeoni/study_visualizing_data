[GitHub - mingrammer/diagrams: :art: Diagram as Code for prototyping cloud system architectures](https://github.com/mingrammer/diagrams)

**Diagrams 란?**

- `python` 을 사용하여 클라우드 시스템 아키텍처 or 시스템 구성도를 쉽게 그릴 수 있는 라이브러리
- 코드로 노드와 연결을 선언하면 내부적으로 `Graphviz` 로 이미지(png/svg)를 렌더링 해줌.

**기능:** 코드로 시스템 구성도를 만든다. 

- AWS / GCP / Azure / Kubernetes / 온프레미스 / SaaS 아이콘 등을 **노드 컴포넌트처럼 import**해서 배치함
- 리소스를 실제로 생성/제어 x → 단순히 그림을 생성하는 용도

**기본 사용 개념**

1. Diagram 컨텍스트
    - `with Diagram("제목")` 블록 안에 작성한 것들이 한 장의 다이어그램이 됨.
2. Node
    - 서비스/컴포넌트 하나
3. Edge
    - 노드 간 연결. `>>` , `<<` , `-` 같은 연산자로 연결 방향/관계를 표현함
    - `Edge` 객체로 라벨/스타일 등을 줄 수도 있음
4. Cluster
    - 논리적 묶음 (ex. “Services”, “DB Cluster”)을 박스로 그룹핑

**특징**

- **장점**
    1. 코드 기반 다이어그램: 아키텍처가 바뀌면 코드만 수정하면 됨. 
    2. 다양한 리소스 지원: 아이콘/프로바디어가 풍부함. 
    3. 간편한 사용법
    4. 리뷰/협업이 쉬움: 다이어그램 변경이 diff로 남아서 Git으로 버전 관리하기 좋음
- **단점**
    1. 레이아웃이 `Graphviz` 자동 배치라서 미세한 픽셀 단위 수동 조정은 어려움. 
    2. 노드/엣지가 많아지면 가독성 튜닝 이슈가 생길 수 있음 
    3. 예쁘진 않음. 기술 문서/아키텍처 문서용
    

**사용 사례**

- GitHub README / 위키 / 기술 블로그
- 컴포넌트가 명확한 구성도일 때
- 최신 구성도를 자동 생성하고 싶을 때

**실습 코드**

⚠️ 주의: `Graphviz` 가 시스템에 설치되어 있어야 렌더링 가능
