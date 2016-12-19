import pandas as pd
import fg as mmmm
import dfdf
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
data_usa = pd.read_excel('D:/work/data/USA1.xlsx', skeep_footer=6, index_col=0)
data_kz = pd.read_excel(url_kazah, header=2, index_col=0,
                        parse_cols="A,P,R:U,W:Z,AB:AE,AG:AJ,AL:AO,AQ:AT,AV:AY,BA:BC")
data_br=pd.read_excel('D:/work/data/braz1.xlsx', index_col=0, parse_cols="A:AS")
data_ch=pd.read_excel('D:/work/data/maych1.xlsx', index_col=0, parse_cols="A:AR")
data_05 = pd.read_excel(url_05, header=3, parse_cols="A:E",skip_footer=6,index_col=0)
data_06 = pd.read_excel(url_06, header=3, parse_cols="A:E",skip_footer=6,index_col=0)
data_07 = pd.read_excel(url_07, header=3, parse_cols="A,E",skip_footer=6,index_col=0)
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
thusa_neo= usa_neo.unstack().head(32)
brazil_neo=braz_neo.unstack().head(32)
china_neo=ch_neo.unstack().head(32)
fran=dfdf.dfdf('D:/work/data/fran.xlsx',"A1:A37").unstack().head(32)
brit=dfdf.dfdf('D:/work/data/brit1.xlsx',"A12:A43").unstack().head(32)
kv_11 = np.concatenate([thusa_neo, china_neo*100,
                        brit,
                        brazil_neo,
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
thusa=usa_se.unstack().head(32)
fran=dfdf.dfdf('D:/work/data/fran.xlsx',"A1:A37").unstack().head(32)
brit=dfdf.dfdf('D:/work/data/brit1.xlsx',"A12:A43").unstack().head(32)
kv_23 = np.concatenate([(thusa_neo-thusa.values),
                        china_neo*100,
                        brit,
                        brazil_neo,
                        kv07,
                        kv08, kv09,
                        kv10, kv11,
                        kv.values,
                        kv3.values,
                        kv4.values,
                        kv5.values,
                        kaz_neo.values])







def kv2():
    kv2 = pd.DataFrame({'Чистые ошибки и пропуски(С)':kv_11,
                    'Чистые ошибки и пропуски':kv_23,
                    'Ошибки и пропуски': abs(kv_11),
                    'Абс. чоп':abs(kv_23),
                    'Индекс сред.':mmmm.mmmm(pd.rolling_mean,'mean'),
                    'Индекс мин':mmmm.mmmm(pd.rolling_min,'min'),
                    'Индекс макс':mmmm.mmmm(pd.rolling_max,'max'),
                    'Индекс медиана':mmmm.mmmm(pd.rolling_median,'median'),
                    })
    return kv2

p=kv2()
p.to_excel('D:/work/data/Model_ml.xlsx')




#print(kv2)
#kv2.to_excel('D:/work/data/Model_ml.xlsx')




