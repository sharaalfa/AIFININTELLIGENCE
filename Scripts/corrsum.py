import pandas as pd


pc=pd.read_excel('D:\work\data1\Data_mlv_rost_multireg_perebor.xlsx')



pp=pc.corr()


pp.to_excel('D:\work\data1\Data_corr_mlv_rost_multireg_perebor.xlsx')