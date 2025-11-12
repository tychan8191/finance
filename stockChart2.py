import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

ticker = "SPY"
end_date = dt.datetime.now()
start_date = end_date - dt.timedelta(days = 365)


data = yf.download(ticker, start = start_date, end = end_date, auto_adjust=False)

print(data.head(5))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (12,8), gridspec_kw= {'height_ratios': [4,1]})

ax1.plot(data.index, data['Adj Close'], label = 'Adjusted Close Price', linewidth = 1)
ma_50 = data['Adj Close'].rolling(window=50, min_periods=0).mean()
ma_20 = data['Adj Close'].rolling(window=20, min_periods=0).mean()
ax1.plot(data.index, ma_50, label = "50 Day MA", color = 'orange', linewidth = 0.5)
ax1.plot(data.index, ma_20, label = "20 Day MA", color = 'red', linewidth = 0.5)

ax1.set_ylabel('Price', fontsize = 12)
ax1.set_title('SPY Ajusted Close', fontsize = 12, fontweight = 'bold')

color = ['green' if data['Close'].values[i] >= data['Open'].values[i] else 'red' for i in range(len(data))]

ax2.bar(data.index,data['Volume', 'SPY'], color = color)
ax2.set_xlabel('Date', fontsize = 12)

plt.grid(True, alpha = 0.3)

print(data.columns.nlevels)
plt.tight_layout()
#plt.show()