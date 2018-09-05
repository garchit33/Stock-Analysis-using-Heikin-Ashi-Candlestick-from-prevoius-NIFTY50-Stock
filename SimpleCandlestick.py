import plotly as py
import plotly.graph_objs as go
import xlrd
import pandas as pd
from datetime import datetime
df = pd.read_excel('nasdaq.xlsx')

trace = go.Candlestick(x=df.index,
                       open=df.Open,
                       high=df.High,
                       low=df.Low,
                       close=df.Close)
data = [trace]
layout = {
    'title': 'STOCK CHART',
    'yaxis': {'title': 'NIFTY50 STOCK'},
    'xaxis': {'title': 'DAYS (OCT 2017-MARCH 25,2018)'},
    
}
fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig ,filename='nasdaq-candlestick')
