import math
import plotly
import plotly.graph_objs as go 

yPlt = []
xPlt = []
for i, j in [(x, math.log10(x)) for x in range(1,101)]:
    yPlt.append(j)
    xPlt.append(i)

plotly.offline.plot(
{
    "data": [go.Scatter(x=xPlt, y=yPlt)],
    "layout": go.Layout(title="Plotly log() Test")
}, auto_open=True
)
