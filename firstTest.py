import pandas_datareader as web
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import numpy as np

endDate = dt.datetime.now()

startDate = endDate - dt.timedelta(days = 365 * 5)

stocks = ['MSFT', 'SPY', 'QQQ']
df = yf.download(stocks, start = startDate, end = endDate, auto_adjust=False)
adj_close = df['Adj Close']

log_returns = np.log(adj_close / adj_close.shift(1))

cum_log_returns = log_returns.cumsum()

cum_log_returns.plot(title = "Cumulative Returns", figsize = (10,6))
plt.show()