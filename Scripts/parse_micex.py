# -*- coding: utf-8 -*-
import pandas as pd
from urllib import request
import lxml.html as html
from pandas import DataFrame
import numpy as np
#data = pd.read_csv('C:/Users/admin/Downloads/candles.csv')
myurl = 'http://www.cbr.ru/currency_base/dynamics.aspx?VAL_NM_RQ=R01235&date_req1=01.01.2005&date_req2=31.12.2015&rt=1&mode=1'
#raw_data = request.urlopen(myurl)
data_R = pd.read_html(myurl, flavor='bs4')
#print(data)
#Для удобства дальнейшего парсинга вынесем основные домены в отдельные переменныеЖ
#main_domain_cb = 'http://moex.com/ru/index/MICEXINDEXCF/archive/#/fro
#data.to_html('D:\work\data\рубль.html')
#data.to_excel('D:\work\data\рубль.xlsx')
#micex_close = DataFrame([''])
#data1 = pd.DataFrame(data, index=pd.date_range('1/2005'), columns=['Дата', 'Курс'])
#data = np.loadtxt(raw_data, delimiter=",")

i = 63
for col in RR[2]:
    f = col
    #f.to_excel('D:\work\data\рубль.xlsx')
    #s = pd.read_excel('D:\work\data\рубль.xlsx')
    while i < 2670:
          data2 = f[:i]
          R = data2[-1:]
          i = i + 63
          for row in R.values:
              columns = row[0:41]
              p = columns[:2]
Excel = win32com.client.Dispatch("Excel.Application")
d_R = Excel.Workbooks.Open(u'D:\work\data\Остаткинакоррсчет.xlsx')
sheet = d_R.ActiveSheet
vals = [r[0].value for r in sheet.Range("D3:D2732")]
s = pd.DataFrame(vals)

#d_R.Save()
d_R.Close()
Excel.Quit()
d_r = s[:63]
R = d_r[-1:]
k1 = R.unstack().head()
d_r = s[:126]
R = d_r[-1:]
k2 = R.unstack().head()
d_r = s[:189]
R = d_r[-1:]
k3 = R.unstack().head()
d_r = s[:252]
R = d_r[-1:]
k4 = R.unstack().head()
d_r = s[:315]
R = d_r[-1:]
k5 = R.unstack().head()
d_r = s[:378]
R = d_r[-1:]
k6 = R.unstack().head()
d_r = s[:441]
R = d_r[-1:]
k7 = R.unstack().head()
d_r = s[:504]
R = d_r[-1:]
k8 = R.unstack().head()
d_r = s[:567]
R = d_r[-1:]
k9 = R.unstack().head()
d_r = s[:630]
R = d_r[-1:]
k10 = R.unstack().head()
d_r = s[:693]
R = d_r[-1:]
k11 = R.unstack().head()
d_r = s[:756]
R = d_r[-1:]
k12 = R.unstack().head()
d_r = s[:819]
R = d_r[-1:]
k13 = R.unstack().head()
d_r = s[:882]
R = d_r[-1:]
k14 = R.unstack().head()
d_r = s[:945]
R = d_r[-1:]
k15 = R.unstack().head()
d_r = s[:1008]
R = d_r[-1:]
k16 = R.unstack().head()
d_r = s[:1071]
R = d_r[-1:]
k17 = R.unstack().head()
d_r = s[:1134]
R = d_r[-1:]
k18 = R.unstack().head()
d_r = s[:1197]
R = d_r[-1:]
k19 = R.unstack().head()
d_r = s[:1260]
R = d_r[-1:]
k20 = R.unstack().head()
d_r = s[:1323]
R = d_r[-1:]
k21 = R.unstack().head()
d_r = s[:1386]
R = d_r[-1:]
k22 = R.unstack().head()
d_r = s[:1449]
R = d_r[-1:]
k23 = R.unstack().head()
d_r = s[:1512]
R = d_r[-1:]
k24 = R.unstack().head()
d_r = s[:1575]
R = d_r[-1:]
k25 = R.unstack().head()
d_r = s[:1638]
R = d_r[-1:]
k26 = R.unstack().head()
d_r = s[:1701]
R = d_r[-1:]
k27 = R.unstack().head()
d_r = s[:1764]
R = d_r[-1:]
k28 = R.unstack().head()
d_r = s[:1827]
R = d_r[-1:]
k29 = R.unstack().head()
d_r = s[:1890]
R = d_r[-1:]
k30 = R.unstack().head()
d_r = s[:1953]
R = d_r[-1:]
k31 = R.unstack().head()
d_r = s[:2016]
R = d_r[-1:]
k32 = R.unstack().head()
d_r = s[:2079]
R = d_r[-1:]
k33 = R.unstack().head()
d_r = s[:2142]
R = d_r[-1:]
k34 = R.unstack().head()
d_r = s[:2205]
R = d_r[-1:]
k35 = R.unstack().head()
d_r = s[:2268]
R = d_r[-1:]
k36 = R.unstack().head()
d_r = s[:2331]
R = d_r[-1:]
k37 = R.unstack().head()
d_r = s[:2394]
R = d_r[-1:]
k38 = R.unstack().head()
d_r = s[:2457]
R = d_r[-1:]
k39 = R.unstack().head()
d_r = s[:2520]
R = d_r[-1:]
k40 = R.unstack().head()
d_r = s[:2563]
R = d_r[-1:]
k41 = R.unstack().head()
d_r = s[:2600]
R = d_r[-1:]
k42 = R.unstack().head()
d_r = s[:2630]
R = d_r[-1:]
k43 = R.unstack().head()
d_r = s[:2666]
R = d_r[-1:]
k44 = R.unstack().head()
kk = np.concatenate([k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k13, k14, k15, k16, k17, k18, k19, k20, k21, k22, k23, k24, k25, k26, k27, k28, k29, k30, k31, k32, k33, k34, k35, k36, k37, k38, k39, k40, k41, k42, k43, k44])
v2 = pd.DataFrame({'USD/RUB':kk})
print(v2)


              #columns.to_csv('D:\work\data\рубль2.csv')
