import math
import plotly
import plotly.graph_objs as go 

yPlt = []
xPlt = []

for i, j in [(x, math.log10(x)) for x in range(1,1001)]:
    yPlt.append(j)
    xPlt.append(i)
    print(i, j)

plotly.offline.plot(
{
    "data": [go.Scatter(x=xPlt, y=yPlt)],
    "layout": go.Layout(title="Plotly log() Test")
}, auto_open=True
)