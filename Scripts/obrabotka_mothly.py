# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pylab import *
from datetime import*

url_12m = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_monthly_2012.xlsx'
url_13m = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_monthly_2013.xlsx'
url_14m = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_monthly_2014.xlsx'
url_15m = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_monthly_2015.xlsx'
data_moth1 = pd.read_excel(url_12m,header=3,skip_footer=6, index_col=0, parse_cols="A:D,F:H,J:L,N:P")
data_moth2 = pd.read_excel(url_13m,header=3,skip_footer=6, index_col=0, parse_cols="A:D,F:H,J:L,N:P")
data_moth3 = pd.read_excel(url_14m,header=3,skip_footer=6, index_col=0, parse_cols="A:D,F:H,J:L,N:P")
data_moth4 = pd.read_excel(url_15m,header=3,skip_footer=6, index_col=0, parse_cols="A:D,F:H,J:L")
data_moth12 = data_moth1.rename(columns={u'январь':'январь 2012', u'февраль':'февраль 2012', u'март':'март 2012', u'апрель':'апрель 2012', u'май':'май 2012', u'июнь':'июнь 2012', u'июль':'июль 2012', u'август':'август 2012', u'сентябрь':'сентябрь 2012', u'октябрь':'октябрь 2012', u'ноябрь':'ноябрь 2012', u'декабрь':'декабрь 2012'})

data_moth13 = data_moth2.rename(columns={u'январь':'январь 2013', u'февраль':'февраль 2013', u'март':'март 2013', u'апрель':'апрель 2013', u'май':'май 2013', u'июнь':'июнь 2013', u'июль':'июль 2013', u'август':'август 2013', u'сентябрь':'сентябрь 2013', u'октябрь':'октябрь 2013', u'ноябрь':'ноябрь 2013', u'декабрь':'декабрь 2013'})
data_moth14 = data_moth3.rename(columns={u'январь':'январь 2014', u'февраль':'февраль 2014', u'март':'март 2014', u'апрель':'апрель 2014', u'май':'май 2014', u'июнь':'июнь 2014', u'июль':'июль 2014', u'август':'август 2014', u'сентябрь':'сентябрь 2014', u'октябрь':'октябрь 2014', u'ноябрь':'ноябрь 2014', u'декабрь':'декабрь 2014'})
data_moth15 = data_moth4.rename(columns={u'январь':'январь 2015', u'февраль':'февраль 2015', u'март':'март 2015', u'апрель':'апрель 2015', u'май':'май 2015', u'июнь':'июнь 2015', u'июль':'июль 2015', u'август':'август 2015', u'сентябрь':'сентябрь 2015'})
cc = data_moth12.T
cc3 = data_moth13.T
cc4 = data_moth14.T
cc5 = data_moth15.T
#del cc['Экспорт']
#del cc['Импорт']
#del cc3['Экспорт']
#del cc3['Импорт']
#del cc4['Экспорт']
#del cc4['Импорт']
#del cc5['Экспорт']
#del cc5['Импорт']
neo12=cc['Чистые ошибки и пропуски']
neo13=cc3['Чистые ошибки и пропуски']
neo14=cc4['Чистые ошибки и пропуски']
neo15=cc5['Чистые ошибки и пропуски']
url = \
    'http://www.micex.ru/issrpc/marketdata/stock/index/history/' \
    'by_ticker/index_history_MICEXEQRRON.csv?secid=MICEXEQRRON&lang=ru'
micexurl = \
    'http://www.micex.ru/issrpc/marketdata/stock/index/history/' \
    'by_ticker/index_history_MICEXINDEXCF.csv?secid=MICEXINDEXCF&lang=ru'
repo = pd.read_csv(url, sep=';', index_col=2, parse_dates = [2])
micex = pd.read_csv(micexurl, sep=';', index_col=2, parse_dates = [2])
repo = repo[repo.index < datetime(2015, 10, 1)]
repo = repo[repo.index > datetime(2012, 1, 1)]
micex = micex[micex.index < datetime(2015, 10, 1)]
micex = micex[micex.index > datetime(2012, 1, 1)]
#x = pd.date_range('1/1/2005', periods=43, freq='AS')
z = repo['CLOSE']
zz = pd.rolling_mean(z,90)
z1 = z
zzz = z1 / zz
figure()
zzz.plot()
legend()
title('fngn')
show()
rep = z.resample('M', how='min')/5
#rep.columns = ['REPO']
micx = micex['CLOSE'].resample('M', how='min')/500
#micx.columns = ['MICEX']
#data=rep.align(micx)
za = abs(pd.concat([neo12,neo13,neo14,neo15]))
dddd = pd.DataFrame({'Чистые ошибки и пропуски':za, 'РЕПО':rep.values,'ММВБ':micx.values})
#dddd = data.combine_first(za)
#print(dddd)
figure()
plot(za.values, 'r', label='Net errors/omissions(abs)')
plot(rep.values, 'y', label='REPO')
plot(micx.values, 'g', label='MICEX')
legend()
title('INDEXs')
show()
dddd.to_excel('D:\work\data\ббб1.xlsx')