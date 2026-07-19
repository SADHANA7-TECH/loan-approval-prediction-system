import plotly.express as px
import plotly.graph_objects as go


# ----------------------------
# Asset Distribution Pie Chart
# ----------------------------
def asset_pie_chart(residential, commercial, luxury, bank):

    labels = [
        "Residential",
        "Commercial",
        "Luxury",
        "Bank"
    ]

    values = [
        residential,
        commercial,
        luxury,
        bank
    ]

    fig = px.pie(
        names=labels,
        values=values,
        hole=0.45,
        title="Asset Distribution"
    )

    fig.update_traces(textposition="inside", textinfo="percent+label")

    return fig


# ----------------------------
# Financial Health Gauge
# ----------------------------
def health_gauge(score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "Financial Health Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "green"},
            "steps": [
                {"range": [0, 40], "color": "#ff4d4d"},
                {"range": [40, 70], "color": "#ffd633"},
                {"range": [70, 100], "color": "#66cc66"}
            ]
        }
    ))

    fig.update_layout(height=350)

    return fig
