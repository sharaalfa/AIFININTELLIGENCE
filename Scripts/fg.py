import pandas as pd
from pylab import *
import dfdf



# получение данных по ММВБ за 01.01.2006-01.10.2015
micexurl = \
    'http://www.micex.ru/issrpc/marketdata/stock/index/history/' \
    'by_ticker/index_history_MICEXINDEXCF.csv?secid=MICEXINDEXCF&lang=ru'

micex = pd.read_csv(micexurl, sep=';', index_col=2, parse_dates = [2])
micex = micex[micex.index < datetime.datetime(2015, 10, 1)]
micex = micex[micex.index > datetime.datetime(2007, 10, 1)]
# расчет max, min, mean, median значений индексов за квартал в рамках 2007-2015

def mmmm(oo,t):
    m=0.014777*(micex['CLOSE'].resample('Q', how=t)/9.36)
    c=0.125*(oo(dfdf.dfdf(u'D:\work\data\shan.xlsx',"A1:A2636"), 60)/1.7)
    c_m=1.41*(oo(dfdf.dfdf(u'D:\work\data\gbr.xlsx',"A1:A3071"), 68)/5.92)
    b=0.28*(oo(dfdf.dfdf(u'D:\work\data\zin.xlsx', "A1:A2862"), 64)/7.4)
    a=oo(dfdf.dfdf(u'D:\work\data\dj1.xlsx',"A1:A2770"), 62)
    k=0.00365*(oo(dfdf.dfdf(u'D:\work\data\kaz_index.xlsx',"A1:A1971"), 50)/11.5)
    ind_un=np.concatenate([
                           a.loc[768],
                           a.loc[832],
                           a.loc[898],
                           a.loc[962],
                           a.loc[1026],
                           a.loc[1090],
                           a.loc[1154],
                           a.loc[1218],
                           a.loc[1282],
                           a.loc[1346],
                           a.loc[1410],
                           a.loc[1474],
                           a.loc[1538],
                           a.loc[1602],
                           a.loc[1666],
                           a.loc[1730],
                           a.loc[1796],
                           a.loc[1862],
                           a.loc[1926],
                           a.loc[1990],
                           a.loc[2054],
                           a.loc[2118],
                           a.loc[2182],
                           a.loc[2246],
                           a.loc[2310],
                           a.loc[2374],
                           a.loc[2438],
                           a.loc[2502],
                           a.loc[2566],
                           a.loc[2630],
                           a.loc[2694],
                           a.loc[2758],
                            c.loc[744],
                            c.loc[806],
                            c.loc[870],
                            c.loc[932],
                            c.loc[994],
                            c.loc[1056],
                            c.loc[1118],
                            c.loc[1180],
                            c.loc[1242],
                            c.loc[1304],
                            c.loc[1366],
                            c.loc[1428],
                            c.loc[1490],
                            c.loc[1552],
                            c.loc[1614],
                           c.loc[1676],
                           c.loc[1740],
                           c.loc[1804],
                           c.loc[1866],
                           c.loc[1928],
                           c.loc[1990],
                            c.loc[2052],
                            c.loc[2114],
                            c.loc[2176],
                            c.loc[2238],
                            c.loc[2300],
                            c.loc[2362],
                            c.loc[2428],
                            c.loc[2490],
                            c.loc[2552],
                            c.loc[2614],
                            c.loc[2635],
                            c_m.loc[840],
                            c_m.loc[910],
                            c_m.loc[980],
                            c_m.loc[1050],
                            c_m.loc[1120],
                            c_m.loc[1190],
                            c_m.loc[1260],
                            c_m.loc[1330],
                            c_m.loc[1400],
                            c_m.loc[1470],
                            c_m.loc[1540],
                            c_m.loc[1610],
                            c_m.loc[1680],
                            c_m.loc[1750],
                            c_m.loc[1820],
                           c_m.loc[1890],
                           c_m.loc[1960],
                           c_m.loc[2030],
                           c_m.loc[2100],
                           c_m.loc[2170],
                           c_m.loc[2240],
                            c_m.loc[2300],
                            c_m.loc[2370],
                            c_m.loc[2440],
                            c_m.loc[2510],
                            c_m.loc[2580],
                            c_m.loc[2650],
                            c_m.loc[2720],
                            c_m.loc[2790],
                            c_m.loc[2860],
                            c_m.loc[2930],
                            c_m.loc[3000],
                            b.loc[792],
                            b.loc[858],
                            b.loc[924],
                            b.loc[990],
                            b.loc[1056],
                            b.loc[1122],
                            b.loc[1188],
                            b.loc[1254],
                            b.loc[1320],
                            b.loc[1386],
                            b.loc[1452],
                            b.loc[1518],
                            b.loc[1584],
                            b.loc[1650],
                            b.loc[1716],
                           b.loc[1782],
                           b.loc[1848],
                           b.loc[1914],
                           b.loc[1980],
                           b.loc[2046],
                           b.loc[2112],
                            b.loc[2178],
                            b.loc[2244],
                            b.loc[2310],
                            b.loc[2376],
                            b.loc[2442],
                            b.loc[2508],
                            b.loc[2574],
                            b.loc[2640],
                            b.loc[2706],
                            b.loc[2772],
                            b.loc[2838],
                           m,
                           k.loc[52],
                            k.loc[104],
                            k.loc[156],
                            k.loc[208],
                            k.loc[260],
                            k.loc[312],
                            k.loc[364],
                            k.loc[416],
                            k.loc[468],
                            k.loc[520],
                            k.loc[572],
                            k.loc[624],
                            k.loc[676],
                            k.loc[728],
                            k.loc[780],
                            k.loc[832],
                            k.loc[884],
                            k.loc[936],
                            k.loc[988],
                            k.loc[1040],
                            k.loc[1092],
                            k.loc[1144],
                            k.loc[1196],
                            k.loc[1248],
                            k.loc[1300],
                            k.loc[1352],
                           k.loc[1404],
                           k.loc[1456],
                           k.loc[1508],
                           k.loc[1560],
                           k.loc[1612],
                           k.loc[1664]])

    return ind_un




