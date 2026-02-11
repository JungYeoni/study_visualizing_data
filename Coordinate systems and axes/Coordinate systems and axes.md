# 좌표계

- 위치 척도와 상대적인 기하학적 배치의 조합을 뜻함.

---

# 직교 좌표계

![직교 좌표계](https://github.com/user-attachments/assets/7ba247e7-f0d9-449f-98ed-d175558d5d58)

- 데이터 시각화에 가장 널리 사용되는 좌표계
  - 각 위치는 x값과 y값으로 고유하게 지정됨
  - 두 축은 연속적인 위치 척도이므로 양수와 음의 실수 모두 표현 가능

---

## 서로 다른 단위를 갖는 축

![서로 다른 단위 매핑](https://github.com/user-attachments/assets/5b8db144-b696-4700-ac61-0a2298f6d512)

- 서로 다른 유형의 변수를 x축과 y축에 매핑 가능
- 한 축을 늘리거나 줄여도 데이터의 유효한 시각화 유지 가능
  - 길고 좁은 그림 → y축 변화 강조
  - 짧고 넓은 그림 → x축 변화 강조
- 중요한 위치 차이가 눈에 띄도록 종횡비 선택 필요

---

## 동일 단위를 갖는 축

![정사각 격자](https://github.com/user-attachments/assets/7349e208-ed9f-4297-8fc5-bf8d3fa33d82)

- x축과 y축의 단위가 같다면 격자 간격도 같아야 함
- 격자선이 정사각형 형태가 되어야 왜곡 없음

---

- 직교 좌표계는 선형 변환에 대해 불변
  - 단위를 변경하더라도 축을 함께 조정하면 그래프 형태는 유지됨

---

# 비선형 축

- 직교 좌표계의 기본 스케일은 선형 스케일
- 선형 스케일이 적합한 경우: 데이터 값을 그대로 보여줄 때
- 비선형 스케일이 적합한 경우:
  - 값의 범위 차이가 매우 클 때
  - 작은 변화가 중요할 때

![비선형 스케일 예시](https://github.com/user-attachments/assets/c274e2c8-809b-42d7-9a2d-57e1ec100266)

---

## 로그 스케일

가장 일반적인 비선형 변환

### 사용 경우

1. 곱셈/나눗셈으로 얻은 데이터  
   - 로그 스케일에서 곱셈은 선형 스케일에서 덧셈과 유사  
   - 비율 표현에 적합

2. 값의 크기 차이가 매우 큰 데이터  
   - 단, 0이 포함된 경우 사용 불가  
   - 로그(0) → $-\infty$

---

## 제곱근 스케일

- 로그 스케일보다는 덜 일반적
- 제곱 데이터에 적합

### 사용 예

- 지리적 지역 면적
  - 2차원 값(면적)을 1차원 거리 개념으로 변환
  - 자동차 횡단 시간과 같은 선형 개념 강조 가능

![선형 vs 제곱근 비교](https://github.com/user-attachments/assets/87197307-5c44-4405-891c-4da4e94fc26b)

---

### 제곱근 스케일의 문제점

1. 단위 의미가 명확하지 않음
   - 선형 → 덧셈 단위
   - 로그 → 곱셈 단위
   - 제곱근 → 일정한 해석 규칙 없음

2. 축 눈금 배치가 직관적이지 않음

![제곱근 눈금 예시](https://github.com/user-attachments/assets/3f046b47-0dac-4a76-9c61-35ceecfdf2d7)

---

# 곡선축을 갖는 좌표계

## 극 좌표계

![극 좌표계](https://github.com/user-attachments/assets/0ba75bd2-38b4-4b41-8d2c-fb8776022400)

- 원점으로부터의 각도 + 반지름 거리로 위치 표현
- 주기적 데이터에 적합

![주기 데이터 예시](https://github.com/user-attachments/assets/0f19031b-7b41-4a19-83a3-9174f528eedd)

- 예: 12/31과 1/1 연결 표현 가능

---

## 지리 공간 데이터

![지리 데이터 왜곡](https://github.com/user-attachments/assets/649c3c20-7a6e-4fc0-a21d-832b881345e2)

- 위도/경도를 데카르트 좌표계에 매핑하면 면적과 각도 왜곡 발생 가능

---

## 참고 문헌

> Claus O. Wilke, *Fundamentals of Data Visualization*  
> https://clauswilke.com/dataviz/coordinate-systems-axes.html
