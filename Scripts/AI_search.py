import pandas as pd
from pylab import *
import dfdf



# получение данных по ММВБ, Futsee100 за 01.10.2007-01.12.2015
micexurl = \
    "http://www.micex.ru/issrpc/marketdata/stock/index/history/" \
      "by_ticker/index_history_MICEXBORRON.csv?secid=MICEXBORRON&lang=ru"
url='http://www.micex.ru/issrpc/marketdata/stock/index/history/' \
    'by_ticker/index_history_MICEXEQRRON.csv?secid=MICEXEQRRON&lang=ru'
micex = pd.read_csv(micexurl, sep=';', index_col=2, parse_dates = [2])
micex = micex[micex.index < datetime.datetime(2016, 1, 1)]
micex = micex[micex.index > datetime.datetime(2007, 10, 1)]
micext = pd.read_csv(url, sep=';', index_col=2, parse_dates = [2])
micext = micext[micext.index < datetime.datetime(2016, 1, 1)]
micext = micext[micext.index > datetime.datetime(2007, 10, 1)]
#fig,axes=plt.subplots(ncols=2,figsize=(10,4))
k=pd.DataFrame()
t={}
t1={}
figure()
plot(micex['CLOSE'], 'r', label='bonds')
plot(micext['CLOSE'], 'b', label='shares')
#plot(ind_un_min, 'g', label='ind min')
legend()
title('REPO')
#show()
#t=micex['CLOSE']
#t1=micext['CLOSE']
#k=k.append([t,t1])
#plt.plot(micex['CLOSE'],micext['CLOSE'])
show()
#print(k)