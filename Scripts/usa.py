import pandas as pd
import numpy as np
from datetime import *
import win32com.client
from pylab import *

Excel21 = win32com.client.Dispatch("Excel.Application")
dojo = Excel21.Workbooks.Open(u'D:\work\data\dj.xlsx')
sheet = dojo.ActiveSheet
vals21 = [r[0].value for r in sheet.Range("A1:A2770")]
dojo_val = pd.DataFrame(vals21)
dojo.Close()
Excel21.Quit()

print(pd.rolling_mean(dojo_val, 62))