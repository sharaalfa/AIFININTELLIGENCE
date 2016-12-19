import pandas as pd

import numpy as np
from datetime import *
import win32com.client
from pylab import *
#казахстан
url_kazah = 'http://www.nationalbank.kz/cont/publish253291_30855.xls'
#россия
url_05 = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_np-mc_2005.xlsx'
url_06 = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_np-mc_2006.xlsx'
url_07 = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_np-mc_2007.xlsx'
url_08 = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_np-mc_2008.xlsx'
url_09 = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_np-mc_2009.xlsx'
url_10 = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_np-mc_2010.xlsx'
url_11 = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_np-mc_2011.xlsx'
url = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_np-mc_2012.xlsx'
url_13 = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_np-mc_2013.xlsx'
url_14 = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_np-mc_2014.xlsx'
url_15 = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_np-mc_2015.xlsx'
url_14_A = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_ap_2014.xlsx'
url_15_A = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_ap_2015.xlsx'

url_5 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_05.xlsx'
url_6 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_06.xlsx'
url_7 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_07.xlsx'
url_8 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_08.xlsx'
url_9 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_09.xlsx'
url_100 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_10.xlsx'
url_110 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_11.xlsx'
url_120 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_12.xlsx'
url_130 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_13.xlsx'
url_140 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_14.xlsx'
url_150 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_15.xlsx'

url_dep1 = 'http://www.cbr.ru/statistics/credit_statistics/direct_investment/dir_inv_instrum.xlsx'


#выделяем колонки в платежных балансах стран и иных документах
data_usa = pd.read_excel('D:/work/data/USA.xlsx', skeep_footer=6, index_col=0)
data_kz = pd.read_excel(url_kazah, header=2, index_col=0,
                        parse_cols="A,P,R:U,W:Z,AB:AE,AG:AJ,AL:AO,AQ:AT,AV:AY,BA:BC")
data_br=pd.read_excel('D:/work/data/braz.xlsx', index_col=0, parse_cols="A:AS")
data_ch=pd.read_excel('D:/work/data/maych.xlsx', index_col=0, parse_cols="A:AR")
data_05 = pd.read_excel(url_05, header=3, parse_cols="A:E",skip_footer=6,index_col=0)
data_06 = pd.read_excel(url_06, header=3, parse_cols="A:E",skip_footer=6,index_col=0)
data_07 = pd.read_excel(url_07, header=3, parse_cols="A:E",skip_footer=6,index_col=0)
data_08 = pd.read_excel(url_08, header=3, parse_cols="A:E",skip_footer=6,index_col=0)
data_09 = pd.read_excel(url_09, header=3, parse_cols="A:E",skip_footer=6,index_col=0)
data_10 = pd.read_excel(url_10, header=3, parse_cols="A:E",skip_footer=6,index_col=0)
data_11 = pd.read_excel(url_11, header=3, parse_cols="A:E",skip_footer=6,index_col=0)
data = pd.read_excel(url, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_13 = pd.read_excel(url_13, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_14 = pd.read_excel(url_14, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_15 = pd.read_excel(url_15, header=3, parse_cols="A:D",skip_footer=6, index_col=0)
data_14_A = pd.read_excel(url_14_A, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_15_A = pd.read_excel(url_15_A, header=3, parse_cols="A:D",skip_footer=6, index_col=0)
data_kor = pd.read_excel(
    url_dep1, header=13,
                         parse_cols="Z:AD,AF:AI,AK:AN,AP:AS,AU:AX,AZ:BC,BE:BH,BJ:BM,BO:BR,BT:BW,BY:CA",
    skip_footer=6, index_col=0)
pdkr = pd.DataFrame(data_kor)
i = 1
p = data_kor[:2130.7354].T
p.to_excel('D:\work\data\dep1.xlsx')

data_R5 = pd.read_excel(url_5, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R6 = pd.read_excel(url_6, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R7 = pd.read_excel(url_7, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R8 = pd.read_excel(url_8, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R9 = pd.read_excel(url_9, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R10 = pd.read_excel(url_100, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R11 = pd.read_excel(url_110, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R12 = pd.read_excel(url_120, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R13 = pd.read_excel(url_130, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R14 = pd.read_excel(url_140, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R15 = pd.read_excel(url_150, header=3, parse_cols="A:D",skip_footer=6, index_col=0)

#переименуем колонки, котроые затем транспонируем" в строки

data_kaz = data_kz.rename(
    columns={u'1 квартал':'',
             u'2 квартал':'',
             u'3 квартал':'',
             u'4 квартал':''})

c05 = data_05.rename(columns={u'I квартал 2005 г.':'',
                              u'II квартал 2005 г.':'',
                              u'III квартал 2005 г.':'',
                              u'IV квартал 2005 г.':''})
c06 = data_06.rename(columns={u'I квартал 2006 г.':'',
                              u'II квартал 2006 г.':'',
                              u'III квартал 2006 г.':'',
                              u'IV квартал 2006 г.':''})
c07 = data_07.rename(columns={u'I квартал 2007 г.':'',
                              u'II квартал 2007 г.':'',
                              u'III квартал 2007 г.':'',
                              u'IV квартал 2007 г.':''})
c08 = data_08.rename(columns={u'I квартал 2008 г.':'',
                              u'II квартал 2008 г.':'',
                              u'III квартал 2008 г.':'',
                              u'IV квартал 2008 г.':''})
c09 = data_09.rename(columns={u'I квартал 2009 г.':'',
                              u'II квартал 2009 г.':'',
                              u'III квартал 2009 г.':'',
                              u'IV квартал 2009 г.':''})
c10 = data_10.rename(columns={u'I квартал 2010 г.':'',
                              u'II квартал 2010 г.':'',
                              u'III квартал 2010 г.':'',
                              u'IV квартал 2010 г.':''})
c11 = data_11.rename(columns={u'I квартал 2011 г.':'',
                              u'II квартал 2011 г.':'',
                              u'III квартал 2011 г.':'',
                              u'IV квартал 2011 г.':''})
c = data.rename(columns={ u'I квартал 2012 г.':'',
                          u'II квартал 2012 г.':'',
                          u'III квартал 2011 г.':'',
                          u'IV квартал 2011 г.':''})
c3 = data_13.rename(columns={u'I квартал 2013 г.':'',
                             u'II квартал 2013 г.':'',
                             u'III квартал 2013 г.':'',
                             u'IV квартал 2013 г.':''})
c4 = data_14.rename(columns={ u'I квартал 2014 г.':'',
                              u'II квартал 2014 г.':'',
                              u'III квартал 2014 г.':'',
                              u'IV квартал 2014 г.':''})
c5 = data_15.rename(columns={u'I квартал 2015 г.':'',
                             u'II квартал 2015 г.':'',
                             u'III квартал 2015 г.':''})
c6 = data_14_A.rename(columns={ u'I квартал':'',
                                u'II квартал':'',
                                u'III квартал':'',
                                u'IV квартал':''})
c7 = data_15_A.rename(columns={u'I квартал 2015 г.':'',
                               u'II квартал 2015 г.':'',
                               u'III квартал 2015 г.':''})

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

#чистые ошибки и пропуски(+сомнительные операции по России), по США+сезонность
data_05_51 = c05[:51]
data_052 = (data_05_51[-1:])
data_06_51 = c06[:51]
data_062 = (data_06_51[-1:])
data_07_51 = c07[:51]
data_072 = (data_07_51[-1:])
data_08_51 = c08[:51]
data_082 = (data_08_51[-1:])
data_09_51 = c09[:51]
data_092 = (data_09_51[-1:])
data_10_51 = c10[:51]
data_102 = (data_10_51[-1:])
data_11_51 = c11[:51]
data_112 = (data_11_51[-1:])
data51 = c[:51]
data2 = (data51[-1:])
data_13_51 = c3[:51]
data_132 = (data_13_51[-1:])
data_14_51 = c4[:51]
data_142 = (data_14_51[-1:])
data_15_51 = c5[:51]
data_152 = (data_15_51[-1:])
kv05 = data_052.unstack().head()
kv06 = data_062.unstack().head()
kv07 = data_072.unstack().head()
kv08 = data_082.unstack().head()
kv09 = data_092.unstack().head()
kv10 = data_102.unstack().head()
kv11 = data_112.unstack().head()
kv = data2.unstack().head()
kv3 = data_132.unstack().head()
kv4 = data_142.unstack().head()
kv5 = data_152.unstack().head()
data_05_63 = c05[:63]
data_052 = (data_05_63[-1:])
data_06_63 = c06[:63]
data_062 = (data_06_63[-1:])
data_07_63 = c07[:63]
data_072 = (data_07_63[-1:])
data_08_63 = c08[:63]
data_082 = (data_08_63[-1:])
data_09_63 = c09[:63]
data_092 = (data_09_63[-1:])
data_10_63 = c10[:63]
data_102 = (data_10_63[-1:])
data_11_63 = c11[:63]
data_112 = (data_11_63[-1:])
data63 = c[:63]
data2 = (data63[-1:])
data_13_63 = c3[:63]
data_132 = (data_13_63[-1:])
data_14_63 = c6[:'Чистые ошибки и пропуски']
data_142 = (data_14_63[-1:])
data_15_63 = c7[:'Чистые ошибки и пропуски']
data_152 = (data_15_63[-1:])
kaz = data_kaz[:'Чистые ошибки и пропуски']
kz_neo = kaz[-1:]
usa = data_usa[:'Statistical discrepancy /4/']
usa_neo=usa[-1:]
braz=data_br[:'Net errors and omissions']
braz_neo=braz[-1:]
china=data_ch[:'3.Net errors and omissions']
ch_neo=china[-1:]
kv051 = data_052.unstack().head()
kv061 = data_062.unstack().head()
kv071 = data_072.unstack().head()
kv081 = data_082.unstack().head()
kv091 = data_092.unstack().head()
kv101 = data_102.unstack().head()
kv111 = data_112.unstack().head()
kv1 = data2.unstack().head()
kv31 = data_132.unstack().head()
kv41 = data_142.unstack().head()
kv51 = data_152.unstack().head()
kaz_neo = kz_neo.unstack().head(32)
thusa_neo= usa_neo.unstack().head(44)
brazil_neo=braz_neo.unstack().head(44)
china_neo=ch_neo.unstack().head(43)
fran=dfdf('D:/work/data/fran.xlsx',"A1:A37").unstack().head(37)
brit=dfdf('D:/work/data/brit1.xlsx',"A1:A44").unstack().head(44)
kv_11 = np.concatenate([thusa_neo, china_neo*100,
                        brit,
                        fran,
                        brazil_neo,
                        kv06-kv061.values,
                        kv07-kv071.values,
                        kv08-kv081.values,
                        kv09-kv091.values,
                        kv10-kv101.values,
                        kv11-kv111.values,
                        kv-kv1.values,
                        kv3-kv31.values,
                        kv4-kv41.values,
                        kv5-kv51.values,
                        kaz_neo.values])

# ЧИСТЫЕ ОШИБКИ И ПРОПУСКИ БЕЗ СОМНИТЕЛЬНЫХ ОПЕРАЦИЙ ПО РОССИИ
# И БЕЗ СЕЗОННОСТИ В США
data_05_63 = c05[:63]
data_052 = (data_05_63[-1:])
data_06_63 = c06[:63]
data_062 = (data_06_63[-1:])
data_07_63 = c07[:63]
data_072 = (data_07_63[-1:])
data_08_63 = c08[:63]
data_082 = (data_08_63[-1:])
data_09_63 = c09[:63]
data_092 = (data_09_63[-1:])
data_10_63 = c10[:63]
data_102 = (data_10_63[-1:])
data_11_63 = c11[:63]
data_112 = (data_11_63[-1:])
data63 = c[:63]
data2 = (data63[-1:])
data_13_63 = c3[:63]
data_132 = (data_13_63[-1:])
data_14_63 = c6[:'Чистые ошибки и пропуски']
data_142 = (data_14_63[-1:])
data_15_63 = c7[:'Чистые ошибки и пропуски']
data_152 = (data_15_63[-1:])
kaz = data_kaz[:'Чистые ошибки и пропуски']
kz_neo = kaz[-1:]
usa = data_usa[:'  Of which: Seasonal adjustment discrepancy']
usa_se = usa[-1:]
kv05 = data_052.unstack().head()
kv06 = data_062.unstack().head()
kv07 = data_072.unstack().head()
kv08 = data_082.unstack().head()
kv09 = data_092.unstack().head()
kv10 = data_102.unstack().head()
kv11 = data_112.unstack().head()
kv = data2.unstack().head()
kv3 = data_132.unstack().head()
kv4 = data_142.unstack().head()
kv5 = data_152.unstack().head()
kaz_neo = kz_neo.unstack().head(32)
thusa=usa_se.unstack().head(44)
fran=dfdf('D:/work/data/fran.xlsx',"A1:A37").unstack().head(37)
brit=dfdf('D:/work/data/brit1.xlsx',"A1:A44").unstack().head(44)
kv_23 = np.concatenate([(thusa_neo-thusa.values),
                        china_neo*100,
                        brit,
                        fran,
                        brazil_neo,
                        kv06, kv07,
                        kv08, kv09,
                        kv10, kv11,
                        kv.values,
                        kv3.values,
                        kv4.values,
                        kv5.values,
                        kaz_neo.values])





# получение данных по ММВБ за 01.01.2006-01.10.2015
micexurl = \
    'http://www.micex.ru/issrpc/marketdata/stock/index/history/' \
    'by_ticker/index_history_MICEXINDEXCF.csv?secid=MICEXINDEXCF&lang=ru'

micex = pd.read_csv(micexurl, sep=';', index_col=2, parse_dates = [2])
micex = micex[micex.index < datetime.datetime(2015, 10, 1)]
micex = micex[micex.index > datetime.datetime(2006, 1, 1)]
# расчет max, min, mean, median значений индексов за квартал в рамках 2005-2015

#Russia, 2006-2015(III)
micx_min = micex['CLOSE'].resample('Q', how='min')
micx = micex['CLOSE'].resample('Q', how='mean')
micx_median=micex['CLOSE'].resample('Q', how='median')
micx_max = micex['CLOSE'].resample('Q', how='max')
#China, Shanchai, 2005-2015
c_min=pd.rolling_min(dfdf(u'D:\work\data\shan.xlsx',"A1:A2636"), 60)
c_mean=pd.rolling_mean(dfdf(u'D:\work\data\shan.xlsx',"A1:A2636"), 60)
c_median=pd.rolling_median(dfdf(u'D:\work\data\shan.xlsx',"A1:A2636"), 60)
c_max=pd.rolling_max(dfdf(u'D:\work\data\shan.xlsx',"A1:A2636"), 60)
# GBr 2005-2015
br_min=pd.rolling_min(dfdf(u'D:\work\data\gbr.xlsx',"A1:A3071"), 68)
br_mean=pd.rolling_mean(dfdf(u'D:\work\data\gbr.xlsx',"A1:A3071"), 68)
br_median=pd.rolling_median(dfdf(u'D:\work\data\gbr.xlsx',"A1:A3071"), 68)
br_max=pd.rolling_max(dfdf(u'D:\work\data\gbr.xlsx',"A1:A3071"), 68)
#Brazil, 2005-2015
b_min=pd.rolling_min(dfdf(u'D:\work\data\zin.xlsx', "A1:A2862"), 64)
b_mean=pd.rolling_mean(dfdf(u'D:\work\data\zin.xlsx', "A1:A2862"), 64)
b_median=pd.rolling_median(dfdf(u'D:\work\data\zin.xlsx', "A1:A2862"), 64)
b_max=pd.rolling_max(dfdf(u'D:\work\data\zin.xlsx', "A1:A2862"), 64)
# USA, 2005-2015
usa_min =  pd.rolling_min(dfdf(u'D:\work\data\dj1.xlsx',"A1:A2770"), 62)
usa_mean =  pd.rolling_mean(dfdf(u'D:\work\data\dj1.xlsx',"A1:A2770"), 62)
usa_median = pd.rolling_median(dfdf(u'D:\work\data\dj1.xlsx',"A1:A2770"), 62)
usa_max =  pd.rolling_max(dfdf(u'D:\work\data\dj1.xlsx',"A1:A2770"), 62)
# France, 2005-2014
f_min = pd.rolling_min(dfdf(u'D:\work\data\kkr.xlsx',"A1:A2345"), 62)
f_mean =  pd.rolling_mean(dfdf(u'D:\work\data\kkr.xlsx',"A1:A2345"), 62)
f_median = pd.rolling_median(dfdf(u'D:\work\data\kkr.xlsx',"A1:A2345"), 62)
f_max =  pd.rolling_max(dfdf(u'D:\work\data\kkr.xlsx',"A1:A2345"), 62)
#Kazachstan, 2007(IV)-2015(III)
kaz_min =  pd.rolling_min(dfdf(u'D:\work\data\kaz_index.xlsx',"A1:A1971"), 50)
kaz_mean = pd.rolling_mean(dfdf(u'D:\work\data\kaz_index.xlsx',"A1:A1971"), 50)
kaz_median=pd.rolling_median(dfdf(u'D:\work\data\kaz_index.xlsx',"A1:A1971"), 50)
kaz_max = pd.rolling_max(dfdf(u'D:\work\data\kaz_index.xlsx',"A1:A1971"), 50)
def acbmk(a,c,c_m,f,b,m,k):
    ind_un=np.concatenate([a.loc[64],
                           a.loc[128],
                           a.loc[192],
                           a.loc[256],
                           a.loc[320],
                           a.loc[384],
                           a.loc[448],
                           a.loc[512],
                           a.loc[576],
                           a.loc[640],
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
                           c_m.loc[70],
                           c_m.loc[140],
                            c_m.loc[210],
                            c_m.loc[280],
                            c_m.loc[350],
                            c_m.loc[420],
                            c_m.loc[490],
                            c_m.loc[560],
                            c_m.loc[630],
                            c_m.loc[700],
                            c_m.loc[770],
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
                           c_m.loc[3070],
                           f.loc[64],
                           f.loc[128],
                           f.loc[192],
                           f.loc[256],
                           f.loc[320],
                           f.loc[384],
                           f.loc[448],
                           f.loc[512],
                           f.loc[576],
                           f.loc[640],
                           f.loc[704],
                           f.loc[768],
                           f.loc[832],
                           f.loc[898],
                           f.loc[962],
                           f.loc[1026],
                           f.loc[1090],
                           f.loc[1154],
                           f.loc[1218],
                           f.loc[1282],
                           f.loc[1346],
                           f.loc[1410],
                           f.loc[1474],
                           f.loc[1538],
                           f.loc[1602],
                           f.loc[1666],
                           f.loc[1730],
                           f.loc[1796],
                           f.loc[1862],
                           f.loc[1926],
                           f.loc[1990],
                           f.loc[2054],
                           f.loc[2118],
                           f.loc[2182],
                           f.loc[2246],
                           f.loc[2310],
                           f.loc[2344],
                           b.loc[66],
                            b.loc[132],
                            b.loc[198],
                            b.loc[264],
                            b.loc[330],
                            b.loc[396],
                            b.loc[462],
                            b.loc[528],
                            b.loc[594],
                            b.loc[660],
                            b.loc[726],
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
                            b.loc[2861],
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
# Создание таблицы данных
kv2 = pd.DataFrame({'Чистые ошибки и пропуски(С)':kv_11,
                    'Чистые ошибки и пропуски':kv_23,
                    'Ошибки и пропуски': abs(kv_11),
                    'Абс. чоп':abs(kv_23),
                    'Индекс сред.':acbmk(usa_mean,c_mean,br_mean,f_mean,b_mean,micx,kaz_mean),
                    'Индекс мин':acbmk(usa_min,c_min,br_min,f_min,b_min,micx_min,kaz_min),
                    'Индекс макс':acbmk(usa_max,c_max,br_max,f_max,b_max,micx_max,kaz_max),
                    'Индекс медиана':acbmk(usa_max,c_median,br_median,f_median,b_median,micx_median,kaz_median)
                    })

kv2.to_excel('D:/work/data/Model_net.xlsx')
