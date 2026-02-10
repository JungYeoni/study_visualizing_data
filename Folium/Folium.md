https://wikidocs.net/234454

**Folium**

- `python` 에서 지도를 생성하고 시각화하기 위한 라이브러리
- `Leaflet.js` 를 기반으로 하며, 이를 통해 사용자는 파이썬 코드를 사용하여 대화하여 지도를 쉽게 만들 수 있다.
- 지리적 데이터를 시각화하고, 지도 위에 다양한 마커와 레이어를 추가하여 풍부한 정보를 표현할 수 있게 해준다.
- 데이터 과학, 지리 정보 시스템, 도시 계획 등 다양한 분야에서 활용됨.

---

`Leaflet.js` 는 웹브라우저에서 동작하는 오픈소스 자바스크립트 지도 라이브러리로, 지도 그 자체를 브라우저에 띄우고 조작하는 역할을 한다.

구체적으로는,

- 지도 확대/축소 (zoom)
- 지도 이동 (pan)
- 마커 표시 (marker)
- 팝업, 툴팁
- 선, 면 그리기
- 여러 지도 레이어 관리 등

우리가 웹에서 보는 드래그되고 클릭되는 지도를 만드는 엔진이다.

**⇒ `Folium` 은 `Leaflet.js` 를 파이썬에서 쉽게 쓰게 해주는 래퍼(wrapper)**

---

**주요 기능**

- 대화형 지도 생성: 다양한 스타일과 속성을 가진 지도 생성 가능
- 마커 및 팝업 추가: 지도 위에 다양한 위치에 마커와 팝업 정보 추가 가능
- 레이어와 타일 추가: 다양한 레이어와 배경 지도를 추가해 정보의 표현 다양화 가능
- 경로, 도형, 그리기: 지도 위에 다양한 경로, 도형을 그리거나 사용자가 그림을 그릴 수 있게 지원
- `GeoJSON`과 `TopoJSON` 지원: 지리적 데이터 형식을 지도에 통합하여 사용할 수 있음

**실습코드**

https://colab.research.google.com/drive/1RkvgpKij3dcSQb2jthQXMhlCtCDF2aX-#scrollTo=e6eAcRvSMkQ0

https://github.com/JungYeoni/study_visualizing_data/blob/main/%EC%A0%9C%EC%9D%BC_%EC%89%AC%EC%9A%B4_%EC%A7%80%EB%8F%84_%EA%B7%B8%EB%A6%AC%EA%B8%B0_Folium.ipynb
