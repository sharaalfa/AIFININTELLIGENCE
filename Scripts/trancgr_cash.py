# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from grab import Grab

url_5 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_05.xlsx'
url_6 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_06.xlsx'
url_7 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_07.xlsx'
url_8 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_08.xlsx'
url_9 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_09.xlsx'
url_10 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_10.xlsx'
url_11 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_11.xlsx'
url_12 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_12.xlsx'
url_13 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_13.xlsx'
url_14 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_14.xlsx'
url_15 = 'http://www.cbr.ru/statistics/CrossBorder/C-b_trans_15.xlsx'

data_R5 = pd.read_excel(url_5, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R6 = pd.read_excel(url_6, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R7 = pd.read_excel(url_7, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R8 = pd.read_excel(url_8, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R9 = pd.read_excel(url_9, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R10 = pd.read_excel(url_10, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R11 = pd.read_excel(url_11, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R12 = pd.read_excel(url_12, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R13 = pd.read_excel(url_13, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R14 = pd.read_excel(url_14, header=3, parse_cols="A:E",skip_footer=6, index_col=0)
data_R15 = pd.read_excel(url_15, header=3, parse_cols="A:D",skip_footer=6, index_col=0)

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
gf = pd.DataFrame({'Перечисления из России': df})
        #gf.to_excel('D:\work\data\Трансграничные_по странам1.xlsx')
print(gf)



