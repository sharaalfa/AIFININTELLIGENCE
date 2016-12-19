import pandas as pd
import numpy as np
aa=pd.read_excel('D:\work\data1\Data_mlv_rost_multireg.xlsx')
def ghgh(u,co):
    pu=aa.loc[u,co]
    pc=aa.loc[u+33,co]
    pbr=aa.loc[u+66,co]
    pb=aa.loc[u+99,co]
    pr=aa.loc[u+132,co]


    return pu,pc,pbr,pb,pr


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
                       ghgh(16,co),
                       ghgh(17,co),
                       ghgh(18,co),
                       ghgh(19,co),
                       ghgh(20,co),
                       ghgh(21,co),
                       ghgh(22,co),
                       ghgh(23,co),
                       ghgh(24,co),
                       ghgh(25,co),
                       ghgh(26,co),
                       ghgh(27,co),
                       ghgh(28,co),
                       ghgh(29,co),
                       ghgh(30,co),
                       ghgh(31,co),
                       ghgh(32,co)])
    return ss