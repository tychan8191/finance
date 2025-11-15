import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import mplfinance as mpf

def get_stock_data(ticker, startTime, endTime):
    return yf.download(ticker, start = startTime, end = endTime, auto_adjust=False)

ticker = 'NFLX'
end = dt.datetime.now()
start = end - dt.timedelta(days = 365)
figs = (12, 8)

df = get_stock_data(ticker, start, end)
df.columns = df.columns.droplevel(1)

mov_avg_window = 20

df['ma_20'] = df['Adj Close'].rolling(window = mov_avg_window, min_periods=0).mean()
df['diff']= df['Adj Close'] - df['ma_20']
df['signal'] = np.where(df['diff'] > 0, -1, 1)


figure1 = plt.figure(figsize = figs)
df['Adj Close'].plot()
df['ma_20'].plot()
plt.title("Stock Chart")

figure2 = plt.figure(figsize = figs)
df['diff'].plot()
(20*df['signal']).plot(linestyle = '--')
plt.legend()
plt.title("Difference Vs Signal")

figure3 = plt.figure(figsize = figs)
(df['Adj Close'] / df['ma_20']).plot()
plt.axhline(y=1, linestyle = ':', label = 'y = 1')
plt.title("Ratio of Close/Moving Avg")

figure4 = plt.figure(figsize = figs)
df['returns'] = df['Adj Close'].pct_change()
df['mean rev returns'] = df['signal'].shift(1) * df['returns']
df=df.dropna()
df['cumulative returns'] = (1 + df['mean rev returns']).cumprod()
df['cumulative returns'].plot()
plt.title("Cumulative Return")

#Comment these out to show certain figures
#plt.close(figure1)
#plt.close(figure2)
plt.close(figure3)
plt.show()