import win32com.client
import pandas as pd
import numpy as np
url = 'http://www.cbr.ru/statistics/credit_statistics/direct_investment/dir_inv_instrum.xlsx'
data_kor = pd.read_excel(url, header=13, parse_cols="Z:AD,AF:AI,AK:AN,AP:AS,AU:AX,AZ:BC,BE:BH,BJ:BM,BO:BR,BT:BW,BY:CA",skip_footer=6, index_col=0)
pdkr = pd.DataFrame(data_kor)
i = 1
p = data_kor[:2130.7354].T
p.to_excel('D:\work\data\dep.xlsx')

Excel1 = win32com.client.Dispatch("Excel.Application")
d_dep = Excel1.Workbooks.Open(u'D:\work\data\dep.xlsx')
sheet = d_dep.ActiveSheet
vals1 = [r[0].value for r in sheet.Range("A2:A44")]
dep_v = pd.DataFrame(vals1)
#d_R.Save()
d_dep.Close()
Excel1.Quit()



