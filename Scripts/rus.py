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

#data_ch = \
   # pd.read_excel(
       ## '/The+time-series+data+of+Balance+of+Payments+of+China.xlsx?MOD=AJPERES&CACHEID=6d920c804c296c90a415af4393d9cc2e',
   # header=0, parse_cols="A,AD:BT",skip_footer=6,index_col=0)
#data_in115 = pd.read_excel('http://rbidocs.rbi.org.in/rdocs/Bulletin/DOCs/40TABB962C7CDB94933932E058D29839596.XLS',
                        #header=3, parse_cols="H", skip_footer=6, index_col=0)
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
#data_china = data_ch.rename(
    #columns={u''}
#)
#india115 = data_in115(columns={u'Jul-Sep 2015 (P)':'3 кв. 15'})
#транспонируем в столбец определенные строки










#чистое приобретение финансовых активов(РФ)
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
kaz = data_kaz[:232]#net  financial active
kz_fa = kaz[-1:]
usa = data_usa[:'  Other investment assets1']
usa_fa = usa[-1:]
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
kaz_fa=kz_fa.unstack().head(32)
thusa_fa = usa_fa.unstack().head(44)
kv_3 = np.concatenate(
    [kv06, kv07, kv08, kv09, kv10, kv11, kv.values,
     kv3.values, kv4.values, kv5.values])
#наличная инвалюта+текущие счета и депозиты(РФ)
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
kaz = data_kaz[:234]#CASH&DEPOSIT
kz_cda = kaz[-1:]
usa = data_usa[:'    Currency and deposits1']
usa_cda = usa[-1:]
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
kaz_cda=kz_cda.unstack().head(32)
thusa_cda=usa_cda.unstack().head(44)
kv_5 = np.concatenate([kv06+kv061.values,
                       kv07+kv071.values,
                       kv08+kv081.values,
                       kv09+kv091.values,
                       kv10+kv101.values,
                       kv11+kv111.values,
                       kv+kv1.values,
                       kv3+kv31.values,
                       kv4+kv41.values,
                       kv5+kv51.values])

#ссуды и займы
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
kaz = data_kaz[:252]#CREDIT
kz_kza = kaz[-1:]
usa = data_usa[:'    Loans1']
usa_kza = usa[-1:]
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
kaz_kza = kz_kza.unstack().head(32)
thusa_kza=usa_kza.unstack().head(44)
kv_7 = np.concatenate(
    [kv06, kv07, kv08, kv09, kv10,
     kv11, kv.values, kv3.values,
     kv4.values, kv5.values])
#торговые кредиты и авансы(РФ)
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
kaz = data_kaz[:278]#TRADE CREDIT
kz_tka = kaz[-1:]
usa = data_usa[:'    Trade credit and advances1']
usa_tka=usa[-1:]
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
kaz_tka = kz_tka.unstack().head(32)
thusa_tka=usa_tka.unstack().head(44)
kv_9 = np.concatenate(
    [kv06, kv07, kv08,
     kv09, kv10, kv11, kv.values,
     kv3.values, kv4.values,
     kv5.values])
#чистые ошибки и пропуски(+сомнительные операции по России)
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
kv_11 = np.concatenate([kv06,
                        kv07,
                        kv08,
                        kv09,
                        kv10,
                        kv11,
                        kv,
                        kv3,
                        kv4,
                        kv5])
#чистое принятие обязательств(РФ)
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
kaz = data_kaz[:312]#NET FINANCIAL PASSIVE
kz_fp = kaz[-1:]
usa = data_usa[:'  Other investment liabilities']
usa_fp=usa[-1:]
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
kaz_fp = kz_fp.unstack().head(32)
thusa_fp=usa_fp.unstack().head(44)
kv_13 = np.concatenate([kv06, kv07,
                        kv08, kv09,
                        kv10, kv11,
                        kv.values,
                        kv3.values,
                        kv4.values,
                        kv5.values])
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
kaz = data_kaz[:314]#CASH$DEPOSIT(PASSIVE)
kz_cdp = kaz[-1:]
usa = data_usa[:'    Currency and deposits']
usa_cdp=usa[-1:]
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
kaz_cdp = kz_cdp.unstack().head(32)
thusa_cdp=usa_cdp.unstack().head(44)
kv_14 = np.concatenate([kv06+kv061.values,
                        kv07+kv071.values,
                        kv08+kv081.values,
                        kv09+kv091.values,
                        kv10+kv101.values,
                        kv11+kv111.values,
                        kv+kv1.values,
                        kv3+kv31.values,
                        kv4+kv41.values,
                        kv5+kv51.values])
#ссуды и займы(РФ) (пассив)
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
kaz = data_kaz[:332]#CREDIT(P)
kz_kzp = kaz[-1:]
usa = data_usa[:'    Loans']
usa_kzp=usa[-1:]
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
kaz_kzp = kz_kzp.unstack().head(32)
thusa_kzp=usa_kzp.unstack().head(44)
kv_16 = np.concatenate([kv06, kv07,
                        kv08, kv09,
                        kv10, kv11,
                        kv.values,
                        kv3.values,
                        kv4.values,
                        kv5.values])
#ЧИСТЫЕ ОШИБКИ И ПРОПУСКИ(РФ)
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
kv_23 = np.concatenate([kv06, kv07,
                        kv08, kv09,
                        kv10, kv11,
                        kv.values,
                        kv3.values,
                        kv4.values,
                        kv5.values])
#резервные активы(РФ)
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
kaz = data_kaz[:393]#reserve active
kz_res = kaz[-1:]
usa = data_usa[:'  Reserve assets']
usa_res=usa[-1:]
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
kaz_res = kz_res.unstack().head(32)
thusa_res=usa_res.unstack().head(44)
kv_24 = np.concatenate([kv06, kv07,
                        kv08, kv09,
                        kv10, kv11,
                        kv.values,
                        kv3.values,
                        kv4.values,
                        kv5.values])
#торговые кредиты и авансы(РФ)(пассив)
data_05_63 = c05[:59]
data_052 = (data_05_63[-1:])
data_06_63 = c06[:59]
data_062 = (data_06_63[-1:])
data_07_63 = c07[:59]
data_072 = (data_07_63[-1:])
data_08_63 = c08[:59]
data_082 = (data_08_63[-1:])
data_09_63 = c09[:59]
data_092 = (data_09_63[-1:])
data_10_63 = c10[:59]
data_102 = (data_10_63[-1:])
data_11_63 = c11[:59]
data_112 = (data_11_63[-1:])
data63 = c[:59]
data2 = (data63[-1:])
data_13_63 = c3[:59]
data_132 = (data_13_63[-1:])
data_14_63 = c4[:59]
data_142 = (data_14_63[-1:])
data_15_63 = c5[:59]
data_152 = (data_15_63[-1:])
kaz = data_kaz[:393]#reserve active
kz_res = kaz[-1:]
kaz = data_kaz[:358]#TRADE CREDIT(P)
kz_tkp = kaz[-1:]
usa = data_usa[:'    Trade credit and advances']
usa_tkp=usa[-1:]
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
kaz_res = kz_res.unstack().head()
kaz_tkp = kz_tkp.unstack().head(32)
thusa_tkp=usa_tkp.unstack().head(44)
kv_25 = np.concatenate([kv06, kv07,
                        kv08, kv09,
                        kv10, kv11,
                        kv.values,
                        kv3.values,
                        kv4.values,
                        kv5.values])
#подготовка данных по остаткам на коррсчетах РФ
#Excel2 = win32com.client.Dispatch("Excel.Application")
#ost = Excel2.Workbooks.Open(u'D:\work\data\Платежный баланс_расширенный5.xlsx')
#sheet = ost.ActiveSheet
#vals2 = [r[0].value for r in sheet.Range("R6:R44")]
#ost_o = pd.DataFrame(vals2)
#d_R.Save()
#ost.Close()
#Excel2.Quit()
url = 'http://www.micex.ru/issrpc/marketdata/stock/index/history/' \
      'by_ticker/index_history_MICEXBORRON.csv?secid=MICEXBORRON&lang=ru'
#url = 'http://www.micex.ru/issrpc/marketdata/stock/index/history/' \
      #'by_ticker/index_history_MOEXREPO.csv?secid=MOEXREPO&lang=ru'
micexurl = \
    'http://www.micex.ru/issrpc/marketdata/stock/index/history/' \
    'by_ticker/index_history_MICEXINDEXCF.csv?secid=MICEXINDEXCF&lang=ru'
url_kzrepo='http://www.kase.kz/ru/repo_indicators/archive/01.01.2005/01.10.2015/40/html'
repo = pd.read_csv(url, sep=';', index_col=2, parse_dates = [2])
micex = pd.read_csv(micexurl, sep=';', index_col=2, parse_dates = [2])
#repo_kaz=pd.read_csv('D:/work/data/TONIA_160318 (1).csv', sep=';', index_col=0, parse_dates = [0])
repo = repo[repo.index < datetime.datetime(2015, 10, 1)]
repo = repo[repo.index > datetime.datetime(2006, 1, 1)]
micex = micex[micex.index < datetime.datetime(2015, 10, 1)]
micex = micex[micex.index > datetime.datetime(2006, 1, 1)]
#repo_kaz=repo_kaz[repo_kaz.index < datetime(2015, 10, 1)]
#x = pd.date_range('1/1/2005', periods=43, freq='AS')
z = repo['CLOSE']
#kaz_r=repo_kaz['<close>']

rep_min = z.resample('Q', how='min')
rep_val_min=repo['VALUE'].resample('Q', how='min')
micx_min = micex['CLOSE'].resample('Q', how='min')
micx_val_min=micex['VALUE'].resample('Q', how='min')
rep = z.resample('Q', how='mean')
rep_val=repo['VALUE'].resample('Q', how='mean')
micx = micex['CLOSE'].resample('Q', how='mean')
micx_val=micex['VALUE'].resample('Q', how='mean')
rep_max = z.resample('Q', how='max')
rep_val_max=repo['VALUE'].resample('Q', how='max')
micx_max = micex['CLOSE'].resample('Q', how='max')
micx_val_max=micex['VALUE'].resample('Q', how='max')
ind_un_min=np.concatenate([micx_min])
ind_un_mean=np.concatenate([micx])
ind_un_max=np.concatenate([micx_max])
repo_un_min=np.concatenate([rep_min])
repo_un_mean=np.concatenate([rep])
repo_un_max=np.concatenate([rep_max])
repval_un_min=np.concatenate([rep_val_min])
repval_un_mean=np.concatenate([rep_val])
repval_un_max=np.concatenate([rep_val_max])
indval_un_min=np.concatenate([micx_val_min])
indval_un_mean=np.concatenate([micx_val])
indval_un_max=np.concatenate([micx_val_max])

kv2 = pd.DataFrame({'Чистое приобретение ф.а.':kv_3,
                    'Наличная инвалюта и депозиты':kv_5,
                    'Ссуды и займы':kv_7,
                    'Торг. кредиты и авансы':kv_9,
                    'Чистые ошибки и пропуски(С)':kv_11,
                    'Чистое принятие обяз-в':kv_13,
                    'Наличная инвалюта и депозиты(П)':kv_14,
                    'Ссуды и займы(П)':kv_16,
                    'Торг. кредиты и авансы(П)':kv_25,
                    'Чистые ошибки и пропуски':kv_23,
                    'Резервные активы':kv_24,
                    'Ошибки и пропуски': abs(kv_11),
                    'Ошибки и пропуски без резервов': abs(kv_11)+abs(kv_24),
                    'Абс. чоп':abs(kv_23),
                    'Ошибки и пропуски без ссуд и депозитов и резервов':
                        abs(kv_5+kv_7-kv_14-kv_16)+abs(kv_11)+abs(kv_24),
                    'РЕПО сред.':repo_un_mean,
                    'Индекс сред.':ind_un_mean,
                    'РЕПО min.':repo_un_min,
                    'Индекс min.':ind_un_min,
                    'РЕПО max.':repo_un_max,
                    'Индекс max.':ind_un_max,
                    'РЕПО сред.об.':repval_un_mean,
                    'Индекс сред.об.':indval_un_mean,
                    'РЕПО min val':repval_un_min,
                    'Индекс min val':indval_un_min,
                    'РЕПО max val':repval_un_max,
                    'Индекс max val':indval_un_max})
#kv2.to_excel('D:/work/data/russ.xlsx')
figure()
#plot(repval_un_mean/100, 'r', label='ind val')
plot(kv_11, 'b', label='fictitious transaction')
plot(kv_25, 'g', label='Trade credit and advances (passive)')
legend()
title('CORR')
show()
def polyfit(x, y, degree):
    results={}

    coeffs=np.polyfit(x, y, degree)
     # Polynominal Coefficients
    results['polynominal']=coeffs.tolist()

    # r-squared
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot


    return results
x = ind_un_max
y = kv_11
print(polyfit(x, y, 2))
pt = kv2.corr()
pt.to_excel('D:/work/data/fg.xlsx')