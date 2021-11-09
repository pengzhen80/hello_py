# basic
import numpy as np
import pandas as pd

import yfinance as yf
import plotly.graph_objects as go

stock_no='2330.TW'

# 查询起始时间
start_date='2021-01-01'
# 查询截止时间
end_date='2021-5-28'

df=yf.download(stock_no,start=start_date)
print(df)
df.tail(10)

figure= go.Figure(
    data=[
          go.Candlestick(
              x=df.index,
              
              open=df['Open'],
              high=df['High'],
              low=df['Low'],
              close=df['Close'],
              increasing_line_color='red',
              decreasing_line_color='green'
          )
    ]
)
figure.update_layout(
    title='2330 Price',
    xaxis_title='Date',
    yaxis_title='Price',
)

#秀圖
figure.show()