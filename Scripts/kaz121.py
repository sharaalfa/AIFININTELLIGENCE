# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from datetime import *
from pylab import *
#прочие инвестиции(РФ)
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

#data_ch = \
   # pd.read_excel(
       ## '/The+time-series+data+of+Balance+of+Payments+of+China.xlsx?MOD=AJPERES&CACHEID=6d920c804c296c90a415af4393d9cc2e',
   # header=0, parse_cols="A,AD:BT",skip_footer=6,index_col=0)
#data_in115 = pd.read_excel('http://rbidocs.rbi.org.in/rdocs/Bulletin/DOCs/40TABB962C7CDB94933932E058D29839596.XLS',
                        #header=3, parse_cols="H", skip_footer=6, index_col=0)
#переименуем колонки, котроые затем транспонируем" в строки
c05 = data_05.rename(
    columns={u'I квартал 2005 г.':'1 КВ. 05(РФ)',
                              u'II квартал 2005 г.':'2 КВ. 05(РФ)',
                              u'III квартал 2005 г.':'3 КВ. 05(РФ)',
                              u'IV квартал 2005 г.':'4 КВ. 05(РФ)'})
c06 = data_06.rename(
    columns={u'I квартал 2006 г.':'1 КВ. 06(РФ)',
                              u'II квартал 2006 г.':'2 КВ. 06(РФ)',
                              u'III квартал 2006 г.':'3 КВ. 06(РФ)',
                              u'IV квартал 2006 г.':'4 КВ. 06(РФ)'})
c07 = data_07.rename(
    columns={u'I квартал 2007 г.':'1 КВ. 07(РФ)',
                              u'II квартал 2007 г.':'2 КВ. 07(РФ)',
                              u'III квартал 2007 г.':'3 КВ. 07(РФ)',
                              u'IV квартал 2007 г.':'4 КВ. 07(РФ)'})
c08 = data_08.rename(
    columns={u'I квартал 2008 г.':'1 КВ. 08(РФ)',
                              u'II квартал 2008 г.':'2 КВ. 08(РФ)',
                              u'III квартал 2008 г.':'3 КВ. 08(РФ)',
                              u'IV квартал 2008 г.':'4 КВ. 08(РФ)'})
c09 = data_09.rename(
    columns={u'I квартал 2009 г.':'1 КВ. 09(РФ)',
                              u'II квартал 2009 г.':'2 КВ. 09(РФ)',
                              u'III квартал 2009 г.':'3 КВ. 09(РФ)',
                              u'IV квартал 2009 г.':'4 КВ. 09(РФ)'})
c10 = data_10.rename(
    columns={u'I квартал 2010 г.':'1 КВ. 10(РФ)',
             u'II квартал 2010 г.':'2 КВ. 10(РФ)',
             u'III квартал 2010 г.':'3 КВ. 10(РФ)',
             u'IV квартал 2010 г.':'4 КВ. 10(РФ)'})
c11 = data_11.rename(
    columns={u'I квартал 2011 г.':'1 КВ. 11(РФ)',
             u'II квартал 2011 г.':'2 КВ. 11(РФ)',
             u'III квартал 2011 г.':'3 КВ. 11(РФ)',
             u'IV квартал 2011 г.':'4 КВ. 11(РФ)'})
c = data.rename(
    columns={u'I квартал 2012 г.':'1 КВ.12(РФ)',
             u'II квартал 2012 г.':'2 КВ. 12(РФ)',
             u'III квартал 2011 г.':'3 КВ. 12(РФ)',
             u'IV квартал 2011 г.':'4 КВ. 12(РФ)'})
c3 = data_13.rename(
    columns={u'I квартал 2013 г.':'1 КВ. 13(РФ)',
             u'II квартал 2013 г.':'2 КВ. 13(РФ)',
             u'III квартал 2013 г.':'3 КВ. 13(РФ)',
             u'IV квартал 2013 г.':'4 КВ. 13(РФ)'})
c4 = data_14.rename(
    columns={ u'I квартал 2014 г.':'1 КВ. 14(РФ)',
              u'II квартал 2014 г.':'2 КВ. 14(РФ)',
              u'III квартал 2014 г.':'3 КВ. 14(РФ)',
              u'IV квартал 2014 г.':'4 КВ. 14(РФ)'})
c5 = data_15.rename(
    columns={u'I квартал 2015 г.':'1 КВ. 15(РФ)',
             u'II квартал 2015 г.':'2 КВ. 15(РФ)',
             u'III квартал 2015 г.':'3 КВ. 15(РФ)'})
c6 = data_14_A.rename(
    columns={ u'I квартал':'1 КВ. 14(РФ)',
              u'II квартал':'2 КВ. 14(РФ)',
              u'III квартал':'3 КВ. 14(РФ)',
              u'IV квартал':'4 КВ 14(РФ)'})
c7 = data_15_A.rename(
    columns={u'I квартал 2015 г.':'1 КВ. 15(РФ)',
             u'II квартал 2015 г.':'2 КВ. 15(РФ)',
             u'III квартал 2015 г.':'3 КВ. 15(РФ)'})
#транспонируем в столбец определенные строки
kaz = data_kaz[:'Чистые ошибки и пропуски']
kz_neo = kaz[-1:].T
kaz = data_kaz[:393]#reserve active
kz_res = kaz[-1:].T
kaz = data_kaz[:231]#another invest
kz_inv = kaz[-1:].T
kaz = data_kaz[:232]#net  financial active
kz_fa = kaz[-1:].T
kaz = data_kaz[:312]#NET FINANCIAL PASSIVE
kz_fp = kaz[-1:].T
kaz = data_kaz[:234]#CASH&DEPOSIT
kz_cda = kaz[-1:].T
kaz = data_kaz[:252]#CREDIT
kz_kza = kaz[-1:].T
kaz = data_kaz[:278]#TRADE CREDIT
kz_tka = kaz[-1:].T
kaz = data_kaz[:314]#CASH$DEPOSIT(PASSIVE)
kz_cdp = kaz[-1:].T
kaz = data_kaz[:332]#CREDIT(P)
kz_kzp = kaz[-1:].T
kaz = data_kaz[:358]#TRADE CREDIT(P)
kz_tkp = kaz[-1:].T
data_05_42 = c05[:42]
data_0542 = (data_05_42[-1:])
data_06_42 = c06[:42]
data_0642 = (data_06_42[-1:])
data_07_42 = c07[:42]
data_0742 = (data_07_42[-1:])
data_08_42 = c08[:42]
data_0842 = (data_08_42[-1:])
data_09_42 = c09[:42]
data_0942 = (data_09_42[-1:])
data_10_42 = c10[:42]
data_1042 = (data_10_42[-1:])
data_11_42 = c11[:42]
data_1142 = (data_11_42[-1:])
data42 = c[:42]
data242 = (data42[-1:])
data_13_42 = c3[:42]
data_1342 = (data_13_42[-1:])
data_14_42 = c4[:42]
data_1442 = (data_14_42[-1:])
data_15_42 = c5[:42]
data_1542 = (data_15_42[-1:])

#сомнительные операции(РФ)
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
#чистые ошибки и пропуски
data_05_63 = c05[:63]
data_053 = (data_05_63[-1:])
data_06_63 = c06[:63]
data_063 = (data_06_63[-1:])
data_07_63 = c07[:63]
data_073 = (data_07_63[-1:])
data_08_63 = c08[:63]
data_083 = (data_08_63[-1:])
data_09_63 = c09[:63]
data_093 = (data_09_63[-1:])
data_10_63 = c10[:63]
data_103 = (data_10_63[-1:])
data_11_63 = c11[:63]
data_113 = (data_11_63[-1:])
data63 = c[:63]
data23 = (data63[-1:])
data_13_63 = c3[:63]
data_133 = (data_13_63[-1:])
data_14_63 = c6[:'Чистые ошибки и пропуски']
data_143 = (data_14_63[-1:])
data_15_63 = c7[:'Чистые ошибки и пропуски']
data_153 = (data_15_63[-1:])
rus = (-data_053+data_052.values).T.append(
    (-data_063+data_062.values).T.append(
        (-data_073+data_072.values).T.append(
            (-data_083+data_082.values).T.append(
                (-data_093+data_092.values).T.append(
                    (-data_103+data_102.values).T.append(
                        (-data_113+data_112.values).T.append(
                            (-data23+data2.values).T.append(
                                (-data_133+data_132.values).T.append(
                                    (-data_143+data_142.values).T.append(
                                        (-data_153+data_152.values).T))))))))))
rus1 = (-data_053+data_0542.values).T.append(
    (-data_063+data_0642.values).T.append(
        (-data_073+data_0742.values).T.append(
            (-data_083+data_0842.values).T.append(
                (-data_093+data_0942.values).T.append(
                    (-data_103+data_1042.values).T.append(
                        (-data_113+data_1142.values).T.append(
                            (-data23+data242.values).T.append(
                                (-data_133+data_1342.values).T.append(
                                    (-data_143+data_1442.values).T.append(
                                        (-data_153+data_1542.values).T))))))))))

print(pd.DataFrame({'qdswd':rus.values, 'ass':rus1.values}))