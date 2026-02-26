**Plotly란?**

- 고급 인터랙티브 데이터 시각화를 위한 파이썬 라이브러리

**특징**

- **장점**
    - 인터랙티브 시각화: 동적으로 반응하는 그래프와 차트를 생성함
    - 다양한 시각화 타입 지원: 라인 차트, 산점도, 바 차트, 파이 차트, 3D 차트 등을 지원함
    - 웹 기반: `D3.js` 를 기반으로 하여 웹 브라우저에서 시각화를 표시함
    - 통합 지원: 다양한 플랫폼에서 사용이 가능함 (Python/R/JavaScript 등)
- **단점**
    - 대용량 데이터에서는 느릴 수 있음
    - 커스터마이징이 복잡해질 수 있음

**활용**

- plotly + Dash 조합
    - 많은 회사에서 Tableau, Superset 대신 내부 전용 대시보드로 많이 사용함.
    
    ```markup
    Python (Pandas)
        ↓
    Plotly
        ↓
    Dash or FastAPI
        ↓
    웹 배포
    ```
    

**실습 코드**

[Google Colab](https://colab.research.google.com/drive/1pB0oI4k8FWAI3X5tDkjfRcHJwI3d9HuS#scrollTo=m__zrBY-VSVy)
