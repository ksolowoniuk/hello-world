import math
import plotly
import plotly.graph_objs as go 

xPlt = []
yPlt = []

for i, j in [(x, math.log10(x)) for x in range(1,1001)]:
    xPlt.append(i)
    yPlt.append(j)
# testing with ron
plotly.offline.plot(
{
    "data": [go.Scatter(x=xPlt, y=yPlt)],
    "layout": go.Layout(title="Plotly log() Test")
}, auto_open=True
)