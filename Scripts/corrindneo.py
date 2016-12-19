import pandas as pd
import dfdf
a=dfdf.dfdf('D:/work/data/Model_net.xlsx',"B2:B284" ).unstack().head(284)
b=dfdf.dfdf('D:/work/data/Model_net.xlsx',"C2:C284" ).unstack().head(284)
c=dfdf.dfdf('D:/work/data/Model_net.xlsx',"D2:D284" ).unstack().head(284)
d=dfdf.dfdf('D:/work/data/Model_net.xlsx',"E2:E284" ).unstack().head(284)
e=dfdf.dfdf('D:/work/data/Model_net.xlsx',"F2:F284" ).unstack().head(284)
f=dfdf.dfdf('D:/work/data/Model_net.xlsx',"G2:G284" ).unstack().head(284)
g=dfdf.dfdf('D:/work/data/Model_net.xlsx',"H2:H284" ).unstack().head(284)
h=dfdf.dfdf('D:/work/data/Model_net.xlsx',"I2:I284" ).unstack().head(284)
kv2=pd.DataFrame({'Чистые ошибки и пропуски(С)':h,
                    'Чистые ошибки и пропуски':g,
                    'Ошибки и пропуски':f,
                    'Абс. чоп':a,
                    'Индекс сред':e,
                    'Индекс мин':d,
                    'Индекс макс':b,
                    'Индекс медиана':c})
pp=kv2.corr()
pp.to_excel('D:/work/data/Model_corr_table3_net.xlsx')
