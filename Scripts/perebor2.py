import numpy as np
import pandas as pd
aa=pd.read_excel('D:\work\data\Data_mod777.xlsx')
def ghgh(u,co):
    pu=aa.loc[u,co]
    pc=aa.loc[u+16,co]



    return pu,pc


def gh(co):
    ss=np.concatenate([ghgh(0,co),
                       ghgh(1,co),
                       ghgh(2,co),
                       ghgh(3,co),
                       ghgh(4,co),
                       ghgh(5,co),
                       ghgh(6,co),
                       ghgh(7,co),
                       ghgh(8,co),
                       ghgh(9,co),
                       ghgh(10,co),
                       ghgh(11,co),
                       ghgh(12,co),
                       ghgh(13,co),
                       ghgh(14,co),
                       ghgh(15,co),
                       ])
    return ss