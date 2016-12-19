import pandas as pd
import numpy as np
from pylab import *
import math
import random
url = \
    'http://www.micex.ru/issrpc/marketdata/stock/index/history/by_ticker/index_history_MICEXEQRRON.csv?secid=MICEXEQRRON&lang=ru'
micexurl = \
    'http://www.micex.ru/issrpc/marketdata/stock/index/history/by_ticker/index_history_MICEXINDEXCF.csv?secid=MICEXINDEXCF&lang=ru'
repo = pd.read_csv(url, sep=';', index_col=2, parse_dates = [2])
micex = pd.read_csv(micexurl, sep=';', index_col=2, parse_dates = [2])
repo = repo[repo.index < datetime.datetime(2015, 10, 1)]
repo = repo[repo.index > datetime.datetime(2006, 1, 1)]
#repo.pivot_table('OPEN','CLOSE').plot(kind='bar', stacked=True)
#show()
y = repo['CLOSE']
def cauchy(location, scale):
    p = 0.0
    while p == 0.0:
        p = random.random(y.values)
    return location + scale*math.tan(math.pi*(p - 0.5))
def running_average():
  sum = 0
  count = 0
  while True:
    sum += cauchy(3,1)
    count += 1
    yield sum/count
for i in y:
    y = y[y.index < datetime.datetime(2006, 1, 13)]
    z = np.ma.average(y)
    print(z)
    break

#z.to_text('D:\work\data\j1.xlsx')