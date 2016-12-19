import pandas as pd

import numpy as np
from datetime import *
import win32com.client
from pylab import *


#выделяем колонки в платежных балансах стран и иных документах
data_usa = pd.read_excel('D:/work/data/USA.xlsx', skeep_footer=6, index_col=0)






# функция извлечение данных с готовых эксель-файлов по США, Казахстану др.
# по национальным биржам и ошибкам и пропускам платежных балансов стран
def dfdf(data_e, b):
    Excel = win32com.client.Dispatch("Excel.Application")
    kazah = Excel.Workbooks.Open(data_e)
    sheet = kazah.ActiveSheet
    vals = [r[0].value for r in sheet.Range(b)]
    return pd.DataFrame(vals)
    kazah.Close()
    Excel.Quit()

# USA, 2005-2015
usa_min =  pd.rolling_min(dfdf(u'D:\work\data\dj1.xlsx',"A1:A2770"), 62)
c_min=0.28*(pd.rolling_min(dfdf(u'D:\work\data\zin.xlsx', "A1:A2862"), 64)/7.4)
def abcde(a,c):
    ind_un=np.concatenate([a.loc[64],
                           a.loc[128],
                           a.loc[192],
                           a.loc[256],
                           a.loc[320],
                           a.loc[384],
                           a.loc[448],
                           a.loc[512],
                           a.loc[576],
                           a.loc[704],
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
                           a.loc[2769],
                           c.loc[62],
                           c.loc[124],
                           c.loc[186],
                           c.loc[248],
                           c.loc[310],
                            c.loc[372],
                            c.loc[434],
                            c.loc[496],
                            c.loc[558],
                            c.loc[620],
                            c.loc[682],
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
                           ])
    return ind_un
print(pd.DataFrame({'dd':abcde(usa_min,c_min)}))