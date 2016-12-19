import pandas as pd
import win32com.client

def dfdf(data_e, b):
    Excel = win32com.client.Dispatch("Excel.Application")
    kazah = Excel.Workbooks.Open(data_e)
    sheet = kazah.ActiveSheet
    vals = [r[0].value for r in sheet.Range(b)]
    return pd.DataFrame(vals)
    kazah.Close()
    Excel.Quit()