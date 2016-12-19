# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
#import statsmodels.api as sm
#from sklearn.metrics import r2_score
#import ml_metrics as metrics
import xlrd
import win32com.client
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

#выделаем колонки
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
data_kor = pd.read_excel(url_dep1, header=13, parse_cols="Z:AD,AF:AI,AK:AN,AP:AS,AU:AX,AZ:BC,BE:BH,BJ:BM,BO:BR,BT:BW,BY:CA",skip_footer=6, index_col=0)
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


c05 = data_05.rename(columns={u'I квартал 2005 г.':'', u'II квартал 2005 г.':'', u'III квартал 2005 г.':'', u'IV квартал 2005 г.':''})
c06 = data_06.rename(columns={u'I квартал 2006 г.':'', u'II квартал 2006 г.':'', u'III квартал 2006 г.':'', u'IV квартал 2006 г.':''})
c07 = data_07.rename(columns={u'I квартал 2007 г.':'', u'II квартал 2007 г.':'', u'III квартал 2007 г.':'', u'IV квартал 2007 г.':''})
c08 = data_08.rename(columns={u'I квартал 2008 г.':'', u'II квартал 2008 г.':'', u'III квартал 2008 г.':'', u'IV квартал 2008 г.':''})
c09 = data_09.rename(columns={u'I квартал 2009 г.':'', u'II квартал 2009 г.':'', u'III квартал 2009 г.':'', u'IV квартал 2009 г.':''})
c10 = data_10.rename(columns={u'I квартал 2010 г.':'', u'II квартал 2010 г.':'', u'III квартал 2010 г.':'', u'IV квартал 2010 г.':''})
c11 = data_11.rename(columns={u'I квартал 2011 г.':'', u'II квартал 2011 г.':'', u'III квартал 2011 г.':'', u'IV квартал 2011 г.':''})
c = data.rename(columns={ u'I квартал 2012 г.':'', u'II квартал 2012 г.':'', u'III квартал 2011 г.':'', u'IV квартал 2011 г.':''})
c3 = data_13.rename(columns={u'I квартал 2013 г.':'', u'II квартал 2013 г.':'', u'III квартал 2013 г.':'', u'IV квартал 2013 г.':''})
c4 = data_14.rename(columns={ u'I квартал 2014 г.':'', u'II квартал 2014 г.':'', u'III квартал 2014 г.':'', u'IV квартал 2014 г.':''})
c5 = data_15.rename(columns={u'I квартал 2015 г.':'', u'II квартал 2015 г.':'', u'III квартал 2015 г.':''})
c6 = data_14_A.rename(columns={ u'I квартал':'', u'II квартал':'', u'III квартал':'', u'IV квартал':''})
c7 = data_15_A.rename(columns={u'I квартал 2015 г.':'', u'II квартал 2015 г.':'', u'III квартал 2015 г.':''})
#выделяем строки, начинаем снизу
data_051 = c05[:31]
data_052 = (data_051[-1:])
data_061 = c06[:31]
data_062 = (data_061[-1:])
data_071 = c07[:31]
data_072 = (data_071[-1:])
data_081 = c08[:31]
data_082 = (data_081[-1:])
data_091 = c09[:31]
data_092 = (data_091[-1:])
data_101 = c10[:31]
data_102 = (data_101[-1:])
data_111 = c11[:31]
data_112 = (data_111[-1:])

data1 = c[:31]
data2 = (data1[-1:])
data_131 = c3[:31]
data_132 = (data_131[-1:])
data_141 = c4[:31]
data_142 = (data_141[-1:])
data_151 = c5[:31]
data_152 = (data_151[-1:])
#kv = data2.stack()
#data12 = c[:'Резервные активы']
#data22 = (data1[-1:])
#kv3 = data22.stack()
#data_131 = c1[:'Чистые ошибки и пропуски']
#data_132 = (data_131[-1:])
#kv1 = data_132.stack()
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
kv_ = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values]) #соединаем в одну колонку кварталы по годам, только значения
data_05_32 = c05[:32]
data_052 = (data_05_32[-1:])
data_06_32 = c06[:32]
data_062 = (data_06_32[-1:])
data_07_32 = c07[:32]
data_072 = (data_07_32[-1:])
data_08_32 = c08[:32]
data_082 = (data_08_32[-1:])
data_09_32 = c09[:32]
data_092 = (data_09_32[-1:])
data_10_32 = c10[:32]
data_102 = (data_10_32[-1:])
data_11_32 = c11[:32]
data_112 = (data_11_32[-1:])
data32 = c[:32]
data2 = (data32[-1:])
data_13_32 = c3[:32]
data_132 = (data_13_32[-1:])
data_14_32 = c4[:32]
data_142 = (data_14_32[-1:])
data_15_32 = c5[:32]
data_152 = (data_15_32[-1:])
#kv = data2.stack()
#data12 = c[:'Резервные активы']
#data22 = (data1[-1:])
#kv3 = data22.stack()
#data_131 = c1[:'Чистые ошибки и пропуски']
#data_132 = (data_131[-1:])
#kv1 = data_132.stack()
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
kv_1 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values]) #соединаем в одну колонку кварталы по годам, только значения

data_05_42 = c05[:42]
data_052 = (data_05_42[-1:])
data_06_42 = c06[:42]
data_062 = (data_06_42[-1:])
data_07_42 = c07[:42]
data_072 = (data_07_42[-1:])
data_08_42 = c08[:42]
data_082 = (data_08_42[-1:])
data_09_42 = c09[:42]
data_092 = (data_09_42[-1:])
data_10_42 = c10[:42]
data_102 = (data_10_42[-1:])
data_11_42 = c11[:42]
data_112 = (data_11_42[-1:])
data42 = c[:42]
data2 = (data42[-1:])
data_13_42 = c3[:42]
data_132 = (data_13_42[-1:])
data_14_42 = c4[:42]
data_142 = (data_14_42[-1:])
data_15_42 = c5[:42]
data_152 = (data_15_42[-1:])
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
kv_2 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values]) #соединаем в одну колонку кварталы по годам, только значения

data_05_43 = c05[:43]
data_052 = (data_05_43[-1:])
data_06_43 = c06[:43]
data_062 = (data_06_43[-1:])
data_07_43 = c07[:43]
data_072 = (data_07_43[-1:])
data_08_43 = c08[:43]
data_082 = (data_08_43[-1:])
data_09_43 = c09[:43]
data_092 = (data_09_43[-1:])
data_10_43 = c10[:43]
data_102 = (data_10_43[-1:])
data_11_43 = c11[:43]
data_112 = (data_11_43[-1:])
data43 = c[:43]
data2 = (data43[-1:])
data_13_43 = c3[:43]
data_132 = (data_13_43[-1:])
data_14_43 = c4[:43]
data_142 = (data_14_43[-1:])
data_15_43 = c5[:43]
data_152 = (data_15_43[-1:])
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
kv_3 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values])
data_05_44 = c05[:44]
data_052 = (data_05_44[-1:])
data_06_44 = c06[:44]
data_062 = (data_06_44[-1:])
data_07_44 = c07[:44]
data_072 = (data_07_44[-1:])
data_08_44 = c08[:44]
data_082 = (data_08_44[-1:])
data_09_44 = c09[:44]
data_092 = (data_09_44[-1:])
data_10_44 = c10[:44]
data_102 = (data_10_44[-1:])
data_11_44 = c11[:44]
data_112 = (data_11_44[-1:])
data44 = c[:44]
data2 = (data44[-1:])
data_13_44 = c3[:44]
data_132 = (data_13_44[-1:])
data_14_44 = c4[:44]
data_142 = (data_14_44[-1:])
data_15_44 = c5[:44]
data_152 = (data_15_44[-1:])
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
kv_4 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values])
data_05_45 = c05[:45]
data_052 = (data_05_45[-1:])
data_06_45 = c06[:45]
data_062 = (data_06_45[-1:])
data_07_45 = c07[:45]
data_072 = (data_07_45[-1:])
data_08_45 = c08[:45]
data_082 = (data_08_45[-1:])
data_09_45 = c09[:45]
data_092 = (data_09_45[-1:])
data_10_45 = c10[:45]
data_102 = (data_10_45[-1:])
data_11_45 = c11[:45]
data_112 = (data_11_45[-1:])
data45 = c[:45]
data2 = (data45[-1:])
data_13_45 = c3[:45]
data_132 = (data_13_45[-1:])
data_14_45 = c4[:45]
data_142 = (data_14_45[-1:])
data_15_45 = c5[:45]
data_152 = (data_15_45[-1:])
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
kv_5 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values])
data_05_46 = c05[:46]
data_052 = (data_05_46[-1:])
data_06_46 = c06[:46]
data_062 = (data_06_46[-1:])
data_07_46 = c07[:46]
data_072 = (data_07_46[-1:])
data_08_46 = c08[:46]
data_082 = (data_08_46[-1:])
data_09_46 = c09[:46]
data_092 = (data_09_46[-1:])
data_10_46 = c10[:46]
data_102 = (data_10_46[-1:])
data_11_46 = c11[:46]
data_112 = (data_11_46[-1:])
data46 = c[:46]
data2 = (data46[-1:])
data_13_46 = c3[:46]
data_132 = (data_13_46[-1:])
data_14_46 = c4[:46]
data_142 = (data_14_46[-1:])
data_15_46 = c5[:46]
data_152 = (data_15_46[-1:])
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
kv_6 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values])
data_05_47 = c05[:47]
data_052 = (data_05_47[-1:])
data_06_47 = c06[:47]
data_062 = (data_06_47[-1:])
data_07_47 = c07[:47]
data_072 = (data_07_47[-1:])
data_08_47 = c08[:47]
data_082 = (data_08_47[-1:])
data_09_47 = c09[:47]
data_092 = (data_09_47[-1:])
data_10_47 = c10[:47]
data_102 = (data_10_47[-1:])
data_11_47 = c11[:47]
data_112 = (data_11_47[-1:])
data47 = c[:47]
data2 = (data47[-1:])
data_13_47 = c3[:47]
data_132 = (data_13_47[-1:])
data_14_47 = c4[:47]
data_142 = (data_14_47[-1:])
data_15_47 = c5[:47]
data_152 = (data_15_47[-1:])
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
kv_7 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values])
data_05_48 = c05[:48]
data_052 = (data_05_48[-1:])
data_06_48 = c06[:48]
data_062 = (data_06_48[-1:])
data_07_48 = c07[:48]
data_072 = (data_07_48[-1:])
data_08_48 = c08[:48]
data_082 = (data_08_48[-1:])
data_09_48 = c09[:48]
data_092 = (data_09_48[-1:])
data_10_48 = c10[:48]
data_102 = (data_10_48[-1:])
data_11_48 = c11[:48]
data_112 = (data_11_48[-1:])
data48 = c[:48]
data2 = (data48[-1:])
data_13_48 = c3[:48]
data_132 = (data_13_48[-1:])
data_14_48 = c4[:48]
data_142 = (data_14_48[-1:])
data_15_48 = c5[:48]
data_152 = (data_15_48[-1:])
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
kv_8 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values])
data_05_49 = c05[:49]
data_052 = (data_05_49[-1:])
data_06_49 = c06[:49]
data_062 = (data_06_49[-1:])
data_07_49 = c07[:49]
data_072 = (data_07_49[-1:])
data_08_49 = c08[:49]
data_082 = (data_08_49[-1:])
data_09_49 = c09[:49]
data_092 = (data_09_49[-1:])
data_10_49 = c10[:49]
data_102 = (data_10_49[-1:])
data_11_49 = c11[:49]
data_112 = (data_11_49[-1:])
data49 = c[:49]
data2 = (data49[-1:])
data_13_49 = c3[:49]
data_132 = (data_13_49[-1:])
data_14_49 = c4[:49]
data_142 = (data_14_49[-1:])
data_15_49 = c5[:49]
data_152 = (data_15_49[-1:])
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
kv_9 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values])
data_05_50 = c05[:50]
data_052 = (data_05_50[-1:])
data_06_50 = c06[:50]
data_062 = (data_06_50[-1:])
data_07_50 = c07[:50]
data_072 = (data_07_50[-1:])
data_08_50 = c08[:50]
data_082 = (data_08_50[-1:])
data_09_50 = c09[:50]
data_092 = (data_09_50[-1:])
data_10_50 = c10[:50]
data_102 = (data_10_50[-1:])
data_11_50 = c11[:50]
data_112 = (data_11_50[-1:])
data50 = c[:50]
data2 = (data50[-1:])
data_13_50 = c3[:50]
data_132 = (data_13_50[-1:])
data_14_50 = c4[:50]
data_142 = (data_14_50[-1:])
data_15_50 = c5[:50]
data_152 = (data_15_50[-1:])
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
kv_10 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values])
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
kv_11 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values])
data_05_52 = c05[:52]
data_052 = (data_05_52[-1:])
data_06_52 = c06[:52]
data_062 = (data_06_52[-1:])
data_07_52 = c07[:52]
data_072 = (data_07_52[-1:])
data_08_52 = c08[:52]
data_082 = (data_08_52[-1:])
data_09_52 = c09[:52]
data_092 = (data_09_52[-1:])
data_10_52 = c10[:52]
data_102 = (data_10_52[-1:])
data_11_52 = c11[:52]
data_112 = (data_11_52[-1:])
data52 = c[:52]
data2 = (data52[-1:])
data_13_52 = c3[:52]
data_132 = (data_13_52[-1:])
data_14_52 = c4[:52]
data_142 = (data_14_52[-1:])
data_15_52 = c5[:52]
data_152 = (data_15_52[-1:])
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
kv_12 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values])
data_05_53 = c05[:53]
data_052 = (data_05_53[-1:])
data_06_53 = c06[:53]
data_062 = (data_06_53[-1:])
data_07_53 = c07[:53]
data_072 = (data_07_53[-1:])
data_08_53 = c08[:53]
data_082 = (data_08_53[-1:])
data_09_53 = c09[:53]
data_092 = (data_09_53[-1:])
data_10_53 = c10[:53]
data_102 = (data_10_53[-1:])
data_11_53 = c11[:53]
data_112 = (data_11_53[-1:])
data53 = c[:53]
data2 = (data53[-1:])
data_13_53 = c3[:53]
data_132 = (data_13_53[-1:])
data_14_53 = c4[:53]
data_142 = (data_14_53[-1:])
data_15_53 = c5[:53]
data_152 = (data_15_53[-1:])
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
kv_13 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values])
data_05_53 = c05[:55]
data_052 = (data_05_53[-1:])
data_06_53 = c06[:55]
data_062 = (data_06_53[-1:])
data_07_53 = c07[:55]
data_072 = (data_07_53[-1:])
data_08_53 = c08[:55]
data_082 = (data_08_53[-1:])
data_09_53 = c09[:55]
data_092 = (data_09_53[-1:])
data_10_53 = c10[:55]
data_102 = (data_10_53[-1:])
data_11_53 = c11[:55]
data_112 = (data_11_53[-1:])
data53 = c[:55]
data2 = (data53[-1:])
data_13_53 = c3[:55]
data_132 = (data_13_53[-1:])
data_14_53 = c4[:55]
data_142 = (data_14_53[-1:])
data_15_53 = c5[:55]
data_152 = (data_15_53[-1:])
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
kv_14 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values])
data_05_53 = c05[:56]
data_052 = (data_05_53[-1:])
data_06_53 = c06[:56]
data_062 = (data_06_53[-1:])
data_07_53 = c07[:56]
data_072 = (data_07_53[-1:])
data_08_53 = c08[:56]
data_082 = (data_08_53[-1:])
data_09_53 = c09[:56]
data_092 = (data_09_53[-1:])
data_10_53 = c10[:56]
data_102 = (data_10_53[-1:])
data_11_53 = c11[:56]
data_112 = (data_11_53[-1:])
data53 = c[:56]
data2 = (data53[-1:])
data_13_53 = c3[:56]
data_132 = (data_13_53[-1:])
data_14_53 = c4[:56]
data_142 = (data_14_53[-1:])
data_15_53 = c5[:56]
data_152 = (data_15_53[-1:])
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
kv_15 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values])
data_05_53 = c05[:57]
data_052 = (data_05_53[-1:])
data_06_53 = c06[:57]
data_062 = (data_06_53[-1:])
data_07_53 = c07[:57]
data_072 = (data_07_53[-1:])
data_08_53 = c08[:57]
data_082 = (data_08_53[-1:])
data_09_53 = c09[:57]
data_092 = (data_09_53[-1:])
data_10_53 = c10[:57]
data_102 = (data_10_53[-1:])
data_11_53 = c11[:57]
data_112 = (data_11_53[-1:])
data53 = c[:57]
data2 = (data53[-1:])
data_13_53 = c3[:57]
data_132 = (data_13_53[-1:])
data_14_53 = c4[:57]
data_142 = (data_14_53[-1:])
data_15_53 = c5[:57]
data_152 = (data_15_53[-1:])
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
kv_16 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values])
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
kv_23 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values])
data_05_63 = c05[:62]
data_052 = (data_05_63[-1:])
data_06_63 = c06[:62]
data_062 = (data_06_63[-1:])
data_07_63 = c07[:62]
data_072 = (data_07_63[-1:])
data_08_63 = c08[:62]
data_082 = (data_08_63[-1:])
data_09_63 = c09[:62]
data_092 = (data_09_63[-1:])
data_10_63 = c10[:62]
data_102 = (data_10_63[-1:])
data_11_63 = c11[:62]
data_112 = (data_11_63[-1:])
data63 = c[:62]
data2 = (data63[-1:])
data_13_63 = c3[:62]
data_132 = (data_13_63[-1:])
data_14_63 = c4[:62]
data_142 = (data_14_63[-1:])
data_15_63 = c5[:62]
data_152 = (data_15_63[-1:])
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
kv_24 = np.concatenate([kv05, kv06, kv07, kv08, kv09, kv10, kv11, kv.values, kv3.values, kv4.values, kv5.values])
c5 = data_R5[:3]
c6 = data_R6[:3]
c7 = data_R7[:3]
c8 = data_R8[:3]
c9 = data_R9[:3]
c10 = data_R10[:3]
c11 = data_R11[:3]
c12 = data_R12[:3]
c13 = data_R13[:3]
c14 = data_R14[:3]
c15 = data_R15[:3]


p5 = c5[-1:]
p6 = c6[-1:]
p7 = c7[-1:]
p8 = c8[-1:]
p9 = c9[-1:]
p10 = c10[-1:]
p11 = c11[-1:]
p12 = c12[-1:]
p13 = c13[-1:]
p14 = c14[-1:]
p15 = c15[-1:]

k5 = p5.unstack().head()
k6 = p6.unstack().head()
k7 = p7.unstack().head()
k8 = p8.unstack().head()
k9 = p9.unstack().head()
k10 = p10.unstack().head()
k11 = p11.unstack().head()
k12 = p12.unstack().head()
k13 = p13.unstack().head()
k14 = p14.unstack().head()
k15 = p15.unstack().head()


df = np.concatenate([k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15])
#подготовка данных по остаткам на коррсчетах РФ
Excel2 = win32com.client.Dispatch("Excel.Application")
ost = Excel2.Workbooks.Open(u'D:\work\data\Платежный баланс_расширенный5.xlsx')
sheet = ost.ActiveSheet
vals2 = [r[0].value for r in sheet.Range("R2:R44")]
ost_o = pd.DataFrame(vals2)
#d_R.Save()
ost.Close()
Excel2.Quit()
kv2 = pd.DataFrame({'Cальдо сч.т.о.и сч.о.к.':kv_,
                    'Сальдо фин.сч.': kv_1,
                    'Прочие инвестиции': kv_2,
                    'Чистое приобретение ф.а.':kv_3,
                    'Прочее участие в капитале':kv_4,
                    'Наличная инвалюта':kv_5,
                    'Текущие сч. и депозиты': kv_6,
                    'Ссуды и займы':kv_7,
                    'Гарантии':kv_8,
                    'Торг. кредиты и авансы':kv_9,
                    'Задолж. по тов. пост.':kv_10,
                    'Сомнит. операции':kv_11,
                    'Прочая деб. задолж.':kv_12,
                    'Чистое принятие обяз-в':kv_13,
                    'Наличная инвалюта(П)':kv_14,
                    'Текущие сч. и депозиты(П)':kv_15,
                    'Ссуды и займы(П)':kv_16,
                    'Чистые ошибки и пропуски':kv_23,
                    'Резервные активы':kv_24,
                    'Остатки на коррсчетах РФ':vals2,
                    'Ошибки и пропуски': kv_11+abs(kv_23),
                    'Ошибки и пропуски без резервов': kv_11+abs(kv_23)+abs(kv_24),
                    'Абс. чоп':abs(kv_23),
                    'Ошибки и пропуски без ссуд и депозитов и резервов': abs(kv_7-kv_16)+abs(kv_6-kv_15)+kv_11+abs(kv_23)+abs(kv_24)})
kv2.to_excel('D:\work\data\Платежный баланс_специальный7.xlsx')
#print(kv2)
x = pd.date_range('1/1/2005', periods=43, freq='AS')
y = kv2['Абс. чоп']
figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()


plot(gg,'y')
legend()
show()
#y = pd.rolling_mean(z,90)
#figure()
#plot(z, 'r')
#xlabel('x')
#ylabel('y')

#title('REPO Index')
#show()
repo = repo[['CLOSE']]
repo.columns = ['REPO']

#y = micex['CLOSE']
#mix = y.resample('Q', how='mean')
s = kv2['Ошибки и пропуски']/1000
figure()
dr = gg.values
#plot(mix, 'g', label='MICEX')
plot(gg.values, 'r', label='REPO')
plot(s, 'y', label='ЧОП')
f = pd.DataFrame({'NEO':s, 'REPO':dr}).plot()
pd.rolling_corr(s, dr, window=5)
f.legend(['REPO', 'NEO'], 'corr').plot(style='.')
show()

#repo_only.to_excel('D:\work\data\Репо.xlsx')