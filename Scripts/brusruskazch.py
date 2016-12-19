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
braz = data_br[:'        Net acquisition of financial assets']
braz_fa=braz[-1:]
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
brazil_fa=braz_fa.unstack().head(44)
kv_3 = np.concatenate(
    [thusa_fa, brazil_fa, kv06, kv07, kv08, kv09, kv10, kv11, kv.values,
     kv3.values, kv4.values, kv5.values, kaz_fa])
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
braz=data_br[:'            Net acquisition of financial assets1']
braz_cda=braz[-1:]
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
brazil_cda=braz_cda.unstack().head(44)
kv_5 = np.concatenate([thusa_cda,
                       brazil_cda,
                       kv06+kv061.values,
                       kv07+kv071.values,
                       kv08+kv081.values,
                       kv09+kv091.values,
                       kv10+kv101.values,
                       kv11+kv111.values,
                       kv+kv1.values,
                       kv3+kv31.values,
                       kv4+kv41.values,
                       kv5+kv51.values,
                       kaz_cda.values])

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
braz=data_br[:'            Net acquisition of financial assets2']
braz_kza=braz[-1:]
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
brazil_kza=braz_kza.unstack().head(44)
kv_7 = np.concatenate(
    [thusa_kza, brazil_kza, kv06, kv07, kv08,
     kv09, kv10, kv11, kv.values, kv3.values,
     kv4.values, kv5.values, kaz_kza.values])
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
braz=data_br[:'            Net acquisition of financial assets3']
braz_tka=braz[-1:]
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
brazil_tka=braz_tka.unstack().head(44)
kv_9 = np.concatenate(
    [thusa_tka, brazil_tka,
     kv06, kv07, kv08,
     kv09, kv10, kv11, kv.values,
     kv3.values, kv4.values,
     kv5.values, kaz_tka.values])
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
braz=data_br[:'Net errors and omissions']
braz_neo=braz[-1:]
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
kv_11 = np.concatenate([thusa_neo, brazil_neo,
                        kv06-kv071.values,
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
braz=data_br[:'        Net incurrence of liabilities']
braz_fp=braz[-1:]
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
brazil_fp=braz_fp.unstack().head(44)
kv_13 = np.concatenate([thusa_fp,
                        brazil_fp,
                        kv06, kv07,
                        kv08, kv09,
                        kv10, kv11,
                        kv.values,
                        kv3.values,
                        kv4.values,
                        kv5.values,
                        kaz_fp.values])
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
braz=data_br[:'            Net incurrence of liabilities1']
braz_cdp=braz[-1:]
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
brazil_cdp=braz_cdp.unstack().head(44)
kv_14 = np.concatenate([thusa_cdp,
                        brazil_cdp,
                        kv06+kv061.values,
                        kv07+kv071.values,
                        kv08+kv081.values,
                        kv09+kv091.values,
                        kv10+kv101.values,
                        kv11+kv111.values,
                        kv+kv1.values,
                        kv3+kv31.values,
                        kv4+kv41.values,
                        kv5+kv51.values,
                        kaz_cdp.values])
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
braz=data_br[:'            Net incurrence of liabilities2']
braz_kzp=braz[-1:]
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
brazil_kzp=braz_kzp.unstack().head(44)
kv_16 = np.concatenate([thusa_kzp,
                        brazil_kzp,
                        kv06, kv07,
                        kv08, kv09,
                        kv10, kv11,
                        kv.values,
                        kv3.values,
                        kv4.values,
                        kv5.values,
                        kaz_kzp.values])
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
kv_23 = np.concatenate([thusa_neo-thusa.values,
                        brazil_neo,
                        kv06, kv07,
                        kv08, kv09,
                        kv10, kv11,
                        kv.values,
                        kv3.values,
                        kv4.values,
                        kv5.values,
                        kaz_neo.values])
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
braz=data_br[:'    Reserve assets']
braz_res=braz[-1:]
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
brazil_res=braz_res.unstack().head(44)
kv_24 = np.concatenate([thusa_res,
                        brazil_res,
                        kv06, kv07,
                        kv08, kv09,
                        kv10, kv11,
                        kv.values,
                        kv3.values,
                        kv4.values,
                        kv5.values,
                        kaz_res.values])
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
braz=data_br[:'            Net incurrence of liabilities3']
braz_tkp=braz[-1:]
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
brazil_tkp=braz_tkp.unstack().head(44)
kv_25 = np.concatenate([thusa_tkp,
                        brazil_tkp,
                        kv06, kv07,
                        kv08, kv09,
                        kv10, kv11,
                        kv.values,
                        kv3.values,
                        kv4.values,
                        kv5.values,
                        kaz_tkp.values])
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
url_ac = 'http://www.micex.ru/issrpc/marketdata/stock/index/history/' \
         'by_ticker/index_history_MICEXEQRRON.csv?secid=MICEXEQRRON&lang=ru'
#url = 'http://www.micex.ru/issrpc/marketdata/stock/index/history/' \
      #'by_ticker/index_history_MOEXREPO.csv?secid=MOEXREPO&lang=ru'
micexurl = \
    'http://www.micex.ru/issrpc/marketdata/stock/index/history/' \
    'by_ticker/index_history_MICEXINDEXCF.csv?secid=MICEXINDEXCF&lang=ru'
url_kzrepo='http://www.kase.kz/ru/repo_indicators/archive/01.01.2005/01.10.2015/40/html'
repo = pd.read_csv(url, sep=';', index_col=2, parse_dates = [2])
repo_ac = pd.read_csv(url_ac, sep=';', index_col=2, parse_dates=[2])
micex = pd.read_csv(micexurl, sep=';', index_col=2, parse_dates = [2])
#repo_kaz=pd.read_csv('D:/work/data/TONIA_160318 (1).csv', sep=';', index_col=0, parse_dates = [0])
repo = repo[repo.index < datetime.datetime(2015, 10, 1)]
repo = repo[repo.index > datetime.datetime(2006, 1, 1)]
repo_ac = repo_ac[repo_ac.index < datetime.datetime(2015, 10, 1)]
repo_ac = repo_ac[repo_ac.index > datetime.datetime(2006, 1, 1)]
micex = micex[micex.index < datetime.datetime(2015, 10, 1)]
micex = micex[micex.index > datetime.datetime(2006, 1, 1)]
#repo_kaz=repo_kaz[repo_kaz.index < datetime(2015, 10, 1)]
#x = pd.date_range('1/1/2005', periods=43, freq='AS')
z = repo['CLOSE']
z1=repo_ac['CLOSE']
#kaz_r=repo_kaz['<close>']
Excel5 = win32com.client.Dispatch("Excel.Application")
kazah = Excel5.Workbooks.Open(u'D:\work\data\kaz.xlsx')
sheet = kazah.ActiveSheet
vals = [r[0].value for r in sheet.Range("A1:A1971")]
kaz_repo = pd.DataFrame(vals)
kazah.Close()
Excel5.Quit()
Excel61 = win32com.client.Dispatch("Excel.Application")
kazahin = Excel61.Workbooks.Open(u'D:\work\data\kaz_index.xlsx')
sheet = kazahin.ActiveSheet
vals1 = [r[0].value for r in sheet.Range("A1:A1971")]
kaz_ind = pd.DataFrame(vals1)
kazahin.Close()
Excel61.Quit()
Excel7 = win32com.client.Dispatch("Excel.Application")
kazahinv = Excel7.Workbooks.Open(u'D:\work\data\kaz_indval.xlsx')
sheet = kazahinv.ActiveSheet
vals2 = [r[0].value for r in sheet.Range("A1:A1971")]
kaz_indval = pd.DataFrame(vals2)
kazahinv.Close()
Excel7.Quit()
Excel4 = win32com.client.Dispatch("Excel.Application")
kazahval = Excel4.Workbooks.Open(u'D:\work\data\kaz_val.xlsx')
sheet = kazahval.ActiveSheet
vals3 = [r[0].value for r in sheet.Range("A1:A1971")]
kaz_value = pd.DataFrame(vals3)
kazahval.Close()
Excel4.Quit()

Excel9 = win32com.client.Dispatch("Excel.Application")
usapr = Excel9.Workbooks.Open(u'D:\work\data\ouss.xlsx')
sheet = usapr.ActiveSheet
vals9 = [r[0].value for r in sheet.Range("A1:A2750")]
usa_pr = pd.DataFrame(vals9)
usapr.Close()
Excel9.Quit()
Excel10 = win32com.client.Dispatch("Excel.Application")
usapr = Excel10.Workbooks.Open(u'D:\work\data\ouss.xlsx')
sheet = usapr.ActiveSheet
vals9 = [r[0].value for r in sheet.Range("B1:B2750")]
usa_pr_treu = pd.DataFrame(vals9)
usapr.Close()
Excel10.Quit()
Excel11 = win32com.client.Dispatch("Excel.Application")
usapr = Excel11.Workbooks.Open(u'D:\work\data\ouss.xlsx')
sheet = usapr.ActiveSheet
vals9 = [r[0].value for r in sheet.Range("C1:C2750")]
usa_pr_agen = pd.DataFrame(vals9)
usapr.Close()
Excel11.Quit()
Excel21 = win32com.client.Dispatch("Excel.Application")
dojo = Excel21.Workbooks.Open(u'D:\work\data\dj.xlsx')
sheet = dojo.ActiveSheet
vals21 = [r[0].value for r in sheet.Range("A1:A2770")]
dojo_val = pd.DataFrame(vals21)
dojo.Close()
Excel21.Quit()
Excel22 = win32com.client.Dispatch("Excel.Application")
dojov = Excel22.Workbooks.Open(u'D:\work\data\dj.xlsx')
sheet = dojov.ActiveSheet
vals22 = [r[0].value for r in sheet.Range("B1:B2770")]
dojo_vol = pd.DataFrame(vals22)
dojov.Close()
Excel22.Quit()
Excel23 = win32com.client.Dispatch("Excel.Application")
bover = Excel23.Workbooks.Open(u'D:\work\data\zin.xlsx')
sheet = bover.ActiveSheet
vals23=[r[0].value for r in sheet.Range("A1:A2862")]
bovespa=pd.DataFrame(vals23)
bover.Close()
Excel23.Quit()
rep_min = z.resample('Q', how='min')
rep_ac_min=z1.resample('Q', how='min')
micx_min = micex['CLOSE'].resample('Q', how='min')
micx_val_min=micex['VALUE'].resample('Q', how='min')
rep = z.resample('Q', how='mean')
rep_ac=z1.resample('Q', how='mean')
micx = micex['CLOSE'].resample('Q', how='mean')
micx_val=micex['VALUE'].resample('Q', how='mean')
rep_max = z.resample('Q', how='max')
rep_ac_max=z1.resample('Q', how='max')
micx_max = micex['CLOSE'].resample('Q', how='max')
micx_val_max=micex['VALUE'].resample('Q', how='max')
b_min=pd.rolling_min(bovespa, 64)
b_mean=pd.rolling_mean(bovespa, 64)
b_max=pd.rolling_max(bovespa, 64)
usa_min =  pd.rolling_min(dojo_val, 62)

usa_mean =  pd.rolling_mean(dojo_val, 62)
usa_max = pd.rolling_max(dojo_val, 62)
kaz_min =  pd.rolling_min(kaz_ind, 50)

kaz_mean =  pd.rolling_mean(kaz_ind, 50)
kaz_max = pd.rolling_max(kaz_ind, 50)
ind_un_min=np.concatenate([usa_min.loc[64],
                            usa_min.loc[128],
                            usa_min.loc[192],
                            usa_min.loc[256],
                            usa_min.loc[320],
                            usa_min.loc[384],
                            usa_min.loc[448],
                            usa_min.loc[512],
                            usa_min.loc[576],
                            usa_min.loc[640],
                            usa_min.loc[704],
                            usa_min.loc[768],
                            usa_min.loc[832],
                            usa_min.loc[898],
                            usa_min.loc[962],
                            usa_min.loc[1026],
                            usa_min.loc[1090],
                            usa_min.loc[1154],
                            usa_min.loc[1218],
                            usa_min.loc[1282],
                            usa_min.loc[1346],
                            usa_min.loc[1410],
                            usa_min.loc[1474],
                            usa_min.loc[1538],
                            usa_min.loc[1602],
                            usa_min.loc[1666],
                           usa_min.loc[1730],
                           usa_min.loc[1796],
                           usa_min.loc[1862],
                           usa_min.loc[1926],
                           usa_min.loc[1990],
                           usa_min.loc[2054],
                            usa_min.loc[2118],
                            usa_min.loc[2182],
                            usa_min.loc[2246],
                            usa_min.loc[2310],
                            usa_min.loc[2374],
                            usa_min.loc[2438],
                            usa_min.loc[2502],
                            usa_min.loc[2566],
                            usa_min.loc[2630],
                            usa_min.loc[2694],
                            usa_min.loc[2758],
                            usa_min.loc[2769],
                           b_min.loc[66],
                            b_min.loc[132],
                            b_min.loc[198],
                            b_min.loc[264],
                            b_min.loc[330],
                            b_min.loc[396],
                            b_min.loc[462],
                            b_min.loc[528],
                            b_min.loc[594],
                            b_min.loc[660],
                            b_min.loc[726],
                            b_min.loc[792],
                            b_min.loc[858],
                            b_min.loc[924],
                            b_min.loc[990],
                            b_min.loc[1056],
                            b_min.loc[1122],
                            b_min.loc[1188],
                            b_min.loc[1254],
                            b_min.loc[1320],
                            b_min.loc[1386],
                            b_min.loc[1452],
                            b_min.loc[1518],
                            b_min.loc[1584],
                            b_min.loc[1650],
                            b_min.loc[1716],
                           b_min.loc[1782],
                           b_min.loc[1848],
                           b_min.loc[1914],
                           b_min.loc[1980],
                           b_min.loc[2046],
                           b_min.loc[2112],
                            b_min.loc[2178],
                            b_min.loc[2244],
                            b_min.loc[2310],
                            b_min.loc[2376],
                            b_min.loc[2442],
                            b_min.loc[2508],
                            b_min.loc[2574],
                            b_min.loc[2640],
                            b_min.loc[2706],
                            b_min.loc[2772],
                            b_min.loc[2838],
                            b_min.loc[2861],
                           micx_min,
                           kaz_min.loc[52],
                            kaz_min.loc[104],
                            kaz_min.loc[156],
                            kaz_min.loc[208],
                            kaz_min.loc[260],
                            kaz_min.loc[312],
                            kaz_min.loc[364],
                            kaz_min.loc[416],
                            kaz_min.loc[468],
                            kaz_min.loc[520],
                            kaz_min.loc[572],
                            kaz_min.loc[624],
                            kaz_min.loc[676],
                            kaz_min.loc[728],
                            kaz_min.loc[780],
                            kaz_min.loc[832],
                            kaz_min.loc[884],
                            kaz_min.loc[936],
                            kaz_min.loc[988],
                            kaz_min.loc[1040],
                            kaz_min.loc[1092],
                            kaz_min.loc[1144],
                            kaz_min.loc[1196],
                            kaz_min.loc[1248],
                            kaz_min.loc[1300],
                            kaz_min.loc[1352],
                           kaz_min.loc[1404],
                           kaz_min.loc[1456],
                           kaz_min.loc[1508],
                           kaz_min.loc[1560],
                           kaz_min.loc[1612],
                           kaz_min.loc[1664]])
ind_un_mean=np.concatenate([usa_mean.loc[64],
                            usa_mean.loc[128],
                            usa_mean.loc[192],
                            usa_mean.loc[256],
                            usa_mean.loc[320],
                            usa_mean.loc[384],
                            usa_mean.loc[448],
                            usa_mean.loc[512],
                            usa_mean.loc[576],
                            usa_mean.loc[640],
                            usa_mean.loc[704],
                            usa_mean.loc[768],
                            usa_mean.loc[832],
                            usa_mean.loc[898],
                            usa_mean.loc[962],
                            usa_mean.loc[1026],
                            usa_mean.loc[1090],
                            usa_mean.loc[1154],
                            usa_mean.loc[1218],
                            usa_mean.loc[1282],
                            usa_mean.loc[1346],
                            usa_mean.loc[1410],
                            usa_mean.loc[1474],
                            usa_mean.loc[1538],
                            usa_mean.loc[1602],
                            usa_mean.loc[1666],
                           usa_mean.loc[1730],
                           usa_mean.loc[1796],
                           usa_mean.loc[1862],
                           usa_mean.loc[1926],
                           usa_mean.loc[1990],
                           usa_mean.loc[2054],
                            usa_mean.loc[2118],
                            usa_mean.loc[2182],
                            usa_mean.loc[2246],
                            usa_mean.loc[2310],
                            usa_mean.loc[2374],
                            usa_mean.loc[2438],
                            usa_mean.loc[2502],
                            usa_mean.loc[2566],
                            usa_mean.loc[2630],
                            usa_mean.loc[2694],
                            usa_mean.loc[2758],
                            usa_mean.loc[2769],
                            b_mean.loc[66],
                            b_mean.loc[132],
                            b_mean.loc[198],
                            b_mean.loc[264],
                            b_mean.loc[330],
                            b_mean.loc[396],
                            b_mean.loc[462],
                            b_mean.loc[528],
                            b_mean.loc[594],
                            b_mean.loc[660],
                            b_mean.loc[726],
                            b_mean.loc[792],
                            b_mean.loc[858],
                            b_mean.loc[924],
                            b_mean.loc[990],
                            b_mean.loc[1056],
                            b_mean.loc[1122],
                            b_mean.loc[1188],
                            b_mean.loc[1254],
                            b_mean.loc[1320],
                            b_mean.loc[1386],
                            b_mean.loc[1452],
                            b_mean.loc[1518],
                            b_mean.loc[1584],
                            b_mean.loc[1650],
                            b_mean.loc[1716],
                           b_mean.loc[1782],
                           b_mean.loc[1848],
                           b_mean.loc[1914],
                           b_mean.loc[1980],
                           b_mean.loc[2046],
                           b_mean.loc[2112],
                            b_mean.loc[2178],
                            b_mean.loc[2244],
                            b_mean.loc[2310],
                            b_mean.loc[2376],
                            b_mean.loc[2442],
                            b_mean.loc[2508],
                            b_mean.loc[2574],
                            b_mean.loc[2640],
                            b_mean.loc[2706],
                            b_mean.loc[2772],
                            b_mean.loc[2838],
                            b_mean.loc[2861],
                            micx,kaz_mean.loc[52],
                            kaz_mean.loc[104],
                            kaz_mean.loc[156],
                            kaz_mean.loc[208],
                            kaz_mean.loc[260],
                            kaz_mean.loc[312],
                            kaz_mean.loc[364],
                            kaz_mean.loc[416],
                            kaz_mean.loc[468],
                            kaz_mean.loc[520],
                            kaz_mean.loc[572],
                            kaz_mean.loc[624],
                            kaz_mean.loc[676],
                            kaz_mean.loc[728],
                            kaz_mean.loc[780],
                            kaz_mean.loc[832],
                            kaz_mean.loc[884],
                            kaz_mean.loc[936],
                            kaz_mean.loc[988],
                            kaz_mean.loc[1040],
                            kaz_mean.loc[1092],
                            kaz_mean.loc[1144],
                            kaz_mean.loc[1196],
                            kaz_mean.loc[1248],
                            kaz_mean.loc[1300],
                            kaz_mean.loc[1352],
                           kaz_mean.loc[1404],
                           kaz_mean.loc[1456],
                           kaz_mean.loc[1508],
                           kaz_mean.loc[1560],
                           kaz_mean.loc[1612],
                           kaz_mean.loc[1664]])
ind_un_max=np.concatenate([usa_max.loc[64],
                            usa_max.loc[128],
                            usa_max.loc[192],
                            usa_max.loc[256],
                            usa_max.loc[320],
                            usa_max.loc[384],
                            usa_max.loc[448],
                            usa_max.loc[512],
                            usa_max.loc[576],
                            usa_max.loc[640],
                            usa_max.loc[704],
                            usa_max.loc[768],
                            usa_max.loc[832],
                            usa_max.loc[898],
                            usa_max.loc[962],
                            usa_max.loc[1026],
                            usa_max.loc[1090],
                            usa_max.loc[1154],
                            usa_max.loc[1218],
                            usa_max.loc[1282],
                            usa_max.loc[1346],
                            usa_max.loc[1410],
                            usa_max.loc[1474],
                            usa_max.loc[1538],
                            usa_max.loc[1602],
                            usa_max.loc[1666],
                           usa_max.loc[1730],
                           usa_max.loc[1796],
                           usa_max.loc[1862],
                           usa_max.loc[1926],
                           usa_max.loc[1990],
                           usa_max.loc[2054],
                            usa_max.loc[2118],
                            usa_max.loc[2182],
                            usa_max.loc[2246],
                            usa_max.loc[2310],
                            usa_max.loc[2374],
                            usa_max.loc[2438],
                            usa_max.loc[2502],
                            usa_max.loc[2566],
                            usa_max.loc[2630],
                            usa_max.loc[2694],
                            usa_max.loc[2758],
                            usa_max.loc[2769],
                           b_max.loc[66],
                            b_max.loc[132],
                            b_max.loc[198],
                            b_max.loc[264],
                            b_max.loc[330],
                            b_max.loc[396],
                            b_max.loc[462],
                            b_max.loc[528],
                            b_max.loc[594],
                            b_max.loc[660],
                            b_max.loc[726],
                            b_max.loc[792],
                            b_max.loc[858],
                            b_max.loc[924],
                            b_max.loc[990],
                            b_max.loc[1056],
                            b_max.loc[1122],
                            b_max.loc[1188],
                            b_max.loc[1254],
                            b_max.loc[1320],
                            b_max.loc[1386],
                            b_max.loc[1452],
                            b_max.loc[1518],
                            b_max.loc[1584],
                            b_max.loc[1650],
                            b_max.loc[1716],
                           b_max.loc[1782],
                           b_max.loc[1848],
                           b_max.loc[1914],
                           b_max.loc[1980],
                           b_max.loc[2046],
                           b_max.loc[2112],
                            b_max.loc[2178],
                            b_max.loc[2244],
                            b_max.loc[2310],
                            b_max.loc[2376],
                            b_max.loc[2442],
                            b_max.loc[2508],
                            b_max.loc[2574],
                            b_max.loc[2640],
                            b_max.loc[2706],
                            b_max.loc[2772],
                            b_max.loc[2838],
                            b_max.loc[2861],
                           micx_max,kaz_max.loc[52],
                            kaz_max.loc[104],
                            kaz_max.loc[156],
                            kaz_max.loc[208],
                            kaz_max.loc[260],
                            kaz_max.loc[312],
                            kaz_max.loc[364],
                            kaz_max.loc[416],
                            kaz_max.loc[468],
                            kaz_max.loc[520],
                            kaz_max.loc[572],
                            kaz_max.loc[624],
                            kaz_max.loc[676],
                            kaz_max.loc[728],
                            kaz_max.loc[780],
                            kaz_max.loc[832],
                            kaz_max.loc[884],
                            kaz_max.loc[936],
                            kaz_max.loc[988],
                            kaz_max.loc[1040],
                            kaz_max.loc[1092],
                            kaz_max.loc[1144],
                            kaz_max.loc[1196],
                            kaz_max.loc[1248],
                            kaz_max.loc[1300],
                            kaz_max.loc[1352],
                           kaz_max.loc[1404],
                           kaz_max.loc[1456],
                           kaz_max.loc[1508],
                           kaz_max.loc[1560],
                           kaz_max.loc[1612],
                           kaz_max.loc[1664]])

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
                    'Индекс сред.':ind_un_mean,
                    'Индекс min.':ind_un_min,
                    'Индекс max.':ind_un_max})
kv2.to_excel('D:/work/data/usbrruskz.xlsx')
figure()
#plot(repval_un_mean/100, 'r', label='ind val')
#plot(abs(kv_11), 'b', label='EO')
#plot(abs(kv_23), 'g', label='abs NEO')
#legend()
#title('INDEXs')
#show()