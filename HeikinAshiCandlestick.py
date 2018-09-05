import numpy as np
import plotly as py
import plotly.graph_objs as go
import xlrd
import pandas as pd
from datetime import datetime
df = pd.read_excel('nasdaq.xlsx')
workbook = xlrd.open_workbook('nasdaq.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
op = df['Open']
hi = df['High']
lo = df['Low']
cl = df['Close']
dum=df['Abc']
dum1=df['Abcd']
tempo=df['tempo']
hc=(op+hi+lo+cl)/4
i=0
while i<=99:
	dum[i]=max(op[i],hi[i],cl[i])
	dum1[i]=min(op[i],lo[i],cl[i])
	i=i+1

j=0
while j<=98:
	tempo[j] = (op[j+1] + cl[j+1])/2
	j=j+1
tempo[j]=6630.50



a=(worksheet.cell(2,1).value)
b=(worksheet.cell(2,4).value)
c=(worksheet.cell(1,2).value)
d=(worksheet.cell(1,1).value)
e=(worksheet.cell(1,4).value)
f=(worksheet.cell(1,3).value)
HClose = (op + hi + lo + cl)/4
HOpen = (a + b)/2
HHigh = max(c,d,e)
HLow = min(f,d,e)


trace = go.Candlestick(open=tempo,
                       high=dum,
                       low=dum1,
                       close=hc)
data = [trace]
layout = {
    'title': 'STOCK CHART',
    'yaxis': {'title': 'NIFTY50 STOCK'},
    'xaxis': {'title': 'DAYS (OCT 2017-MARCH 25,2018)'},
    
}
fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig ,filename='nasdaq-candlestick-2')
