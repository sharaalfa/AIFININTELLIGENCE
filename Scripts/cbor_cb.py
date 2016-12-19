
# -*- coding: utf-8 -*-
import urllib
import pandas as pd
import numpy as np
url_12 = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_monthly_2012.xlsx'
url_13 = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_monthly_2013.xlsx'
url_14 = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_monthly_2014.xlsx'
url_15 = 'http://www.cbr.ru/statistics/credit_statistics/bop/bop_monthly_2015.xlsx'
data_12 = pd.read_excel(url_12, header=3, parse_cols="A:Q", skip_footer=6, index_col=0)
c_12 = data_12.rename(columns={u'январь':'', u'февраль':'', u'март':'', u'апрель':'', u'май':'', u'июнь':'', u'июль':'', u'август':'', u'сентябрь':'', u'октябрь':'', u'ноябрь':'', u'декабрь':''})
data_13 = pd.read_excel(url_13, header=3, parse_cols="A:Q", skip_footer=6, index_col=0)
c_13 = data_13.rename(columns={u'январь':'', u'февраль':'', u'март':'', u'апрель':'', u'май':'', u'июнь':'', u'июль':'', u'август':'', u'сентябрь':'', u'октябрь':'', u'ноябрь':'', u'декабрь':''})
data_14 = pd.read_excel(url_14, header=3, parse_cols="A:Q", skip_footer=6, index_col=0)
c_14 = data_14.rename(columns={u'январь':'', u'февраль':'', u'март':'', u'апрель':'', u'май':'', u'июнь':'', u'июль':'', u'август':'', u'сентябрь':'', u'октябрь':'', u'ноябрь':'', u'декабрь':''})
data_15 = pd.read_excel(url_15, header=3, parse_cols="A:M", skip_footer=6, index_col=0)
c_15 = data_15.rename(columns={u'январь':'', u'февраль':'', u'март':'', u'апрель':'', u'май':'', u'июнь':'', u'июль':'', u'август':'', u'сентябрь':''})
data21 = c_12[:17]
data2 = (data21[-1:])
data_13_21 = c_13[:17]
data_132 = (data_13_21[-1:])
data_14_21 = c_14[:17]
data_142 = (data_14_21[-1:])
data_15_21 = c_15[:17]
data_152 = (data_15_21[-1:])
kv = data2.unstack().head(18)
kv3 = data_132.unstack().head(18)
kv4 = data_142.unstack().head(18)
kv5 = data_152.unstack().head(13)
kv_1 = np.concatenate([kv.values, kv3.values, kv4.values, kv5.values])
data27 = c_12[:23]
data2 = (data27[-1:])
data_13_27 = c_13[:23]
data_132 = (data_13_27[-1:])
data_14_27 = c_14[:23]
data_142 = (data_14_27[-1:])
data_15_27 = c_15[:23]
data_152 = (data_15_27[-1:])
kv = data2.unstack().head(19)
kv3 = data_132.unstack().head(18)
kv4 = data_142.unstack().head(18)
kv5 = data_152.unstack().head(13)
kv_2 = np.concatenate([kv.values, kv3.values, kv4.values, kv5.values])



kv2 = pd.DataFrame({
    'Чистое принятие обязательств':kv_1,
    'Чистое приобретение активов': kv_2},index=['январь 2012','февраль 2012',
                                                'март 2012','I квартал','апрель 2012','май 2012',
                                                'июнь 2012','II квартал','июль 2012','август 2012','сентябрь 2012',
                                                'III квартал','октябрь 2012','ноябрь2012','декабрь 2012','IV квартал','январь 2013',
                                                'февраль 2013','март 2013','I квартал','апрель 2013','май 2013','июнь 2013',
                                                'II квартал','июль 2013','август 2013','сентябрь 2013','III квартал','октябрь 2013',
                                                'ноябрь2013','декабрь 2013','IV квартал','январь 2014','февраль 2014','март 2014',
                                                'I квартал','апрель 2014','май 2014','июнь 2014','II квартал','июль 2014','август 2014',
                                                'сентябрь 2014','III квартал','октябрь 2014','ноябрь2014','декабрь 2014',
                                                'IV квартал','январь 2015','февраль 2015','март 2015','I квартал',
                                                'апрель 2015','май 2015','июнь 2015','II квартал','июль 2015','август 2015','сентябрь 2015','III квартал'])


kv2.to_excel('D:\work\data\Платежный.xlsx')
print(kv2)