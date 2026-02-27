import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

app = dash.Dash(__name__)

# 드롭다운에서 선택할 수 있는 데이터셋
data = {
    "과일": {"항목": ["사과", "바나나", "딸기", "포도", "수박"], "값": [30, 45, 25, 50, 20]},
    "성적": {"항목": ["수학", "영어", "과학", "국어", "역사"], "값": [85, 90, 78, 92, 70]},
    "판매량": {"항목": ["1월", "2월", "3월", "4월", "5월"], "값": [120, 95, 140, 160, 110]},
}

# 앱 레이아웃 정의 - 화면에 표시될 컴포넌트 구성
app.layout = html.Div([
    html.H2("막대 그래프 실습", style={"textAlign": "center"}),

    # 데이터셋을 선택하는 드롭다운
    dcc.Dropdown(
        id="data-selector",
        options=[{"label": k, "value": k} for k in data],  # data의 키를 옵션으로 사용
        value="과일",       # 초기 선택값
        clearable=False,    # 선택 해제 비활성화
        style={"width": "300px", "margin": "20px auto"}
    ),

    # 막대 그래프를 표시할 영역
    dcc.Graph(id="bar-chart"),

    # 합계/평균 텍스트를 표시할 영역
    html.Div(id="info-text", style={"textAlign": "center", "marginTop": "10px", "color": "gray"})
])

# 콜백 - 드롭다운 값이 바뀌면 그래프와 텍스트를 자동으로 업데이트
@app.callback(
    Output("bar-chart", "figure"),      # 그래프 출력
    Output("info-text", "children"),    # 텍스트 출력
    Input("data-selector", "value")     # 드롭다운 입력
)
def update_chart(selected):
    d = data[selected]  # 선택된 데이터셋 가져오기

    # 막대 그래프 생성
    fig = go.Figure(go.Bar(
        x=d["항목"],
        y=d["값"],
        marker_color="steelblue"
    ))

    # 그래프 레이아웃 설정
    fig.update_layout(
        title=f"{selected} 데이터",
        xaxis_title="항목",
        yaxis_title="값",
        plot_bgcolor="white",
        yaxis=dict(gridcolor="lightgray")
    )

    # 합계와 평균 계산
    total = sum(d["값"])
    return fig, f"합계: {total} / 평균: {total / len(d['값']):.1f}"

if __name__ == '__main__':
    app.run(debug=True)
