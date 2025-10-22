import numpy as np
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web

end = dt.datetime.now()
start = dt.datetime(2020, 1, 1)


savepath = 'c:/Users/Ty/Documents/GitHub/finance/second.csv'

df = yf.download('MSFT', start, end, auto_adjust=False)
df.to_csv(savepath)
df = pd.read_csv(savepath, parse_dates=True, header=[0,1], index_col=0)

df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
#print(df.head())
#df[['Adj Close', '100ma']].plot()
#plt.show()

ax1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan = 1, sharex =ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax1.plot.bar(df.index, df['Volume'])

print(df['Volume'].head(5))

plt.show()