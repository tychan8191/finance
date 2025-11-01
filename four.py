import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import datetime as dt

start = dt.datetime(2010, 1, 1)
end = dt.datetime.now()

rets = yf.download(tickers = ['SPY', 'MSFT'], start = start, end = end, interval = '1mo', auto_adjust=False)['Adj Close']
print(rets.head())


rets.plot()

plt.show()
