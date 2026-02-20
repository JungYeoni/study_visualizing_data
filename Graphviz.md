[GitHub - xflr6/graphviz: Simple Python interface for Graphviz](https://github.com/xflr6/graphviz)

**Graphviz**

- 그래프 시각화 소프트웨어와의 인터페이스를 제공하는 파이썬 라이브러리
- Graphviz의 강력한 기능을 파이썬 환경에서 직접 사용할 수 있도록 해줌.

**DOT 언어**

- 그래프를 정의하는 간단한 텍스트 언어
- `graph` : 무방향 그래프 (`—` 로 연결)
- `diagram` : 방향 그래프 (`→` 로 연결)
- 노드/엣지/그래프에 속성을 달아 스타일과 배치를 조정
- `diagraph {A -> B}` :  A에서 B로 흐름

**레이아웃 엔진(배치 알고리즘) - 노드를 어떻게 배치할지** 

- 여러 배치 엔진이 있고, 그래프의 성격에 따라 잘 나오는 엔진이 다름
- **dot**: 계층형(흐름도, 파이프라인, 의존성) – 방향 그래프에 특히 강함, 대부분 사용
    
    ```css
    A → B → C
    ```
    
- **neato**: 스프링(물리) 모델 – 관계망(네트워크)
    
    ```css
      A
     / \
    B   C
     \ /
      D
    ```
    
- **fdp / sfdp**: force-directed 계열 (특히 sfdp는 큰 그래프용) → neato의 더 강한 버전
- **circo**: 원형 배치
    
    ```css
    A — B
    |    |
    D — C
    ```
    
- **twopi**: 방사형(중심에서 퍼짐) (레이아웃 목록 페이지에 함께 소개되는 Graphviz 엔진)
    
    ```css
            C
         B     D
             A
         E     F
    ```
    

**출력 포맷과 CLI 사용 방식**

- 입력 그래프를 다양한 출력으로 변환
    - 웹 문서: SVG
    - 문서: PDF
    - 이미지: PNG

**특징**

- **장점**
    1. 다양한 그래프 타입 지원
    2. 사용자 친화적인 API
    3. 강력한 시각화 
- **단점**
    1. 사이클, 양방향 엣지가 많으면 `dot` 의 계층 개념이 꼬이기 쉽다. 

**실습코드**

[study_visualizing_data/Graphviz.ipynb at main · JungYeoni/study_visualizing_data](https://github.com/JungYeoni/study_visualizing_data/blob/main/Graphviz.ipynb)
