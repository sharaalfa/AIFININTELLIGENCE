import pandas as pd
import numpy as np
aa=pd.read_excel('D:\work\data\Model_ml.xlsx')
def ghgh(u,co):
    pu=aa.loc[u,co]
    pc=aa.loc[u+1,co]
    pbr=aa.loc[u+2,co]
    pb=aa.loc[u+3,co]
    pr=aa.loc[u+4,co]
    pk=aa.loc[u+5,co]
    pu1=aa.loc[u+96,co]
    pc1=aa.loc[u+97,co]
    pbr1=aa.loc[u+98,co]
    pb1=aa.loc[u+99,co]
    pr1=aa.loc[u+100,co]
    pk1=aa.loc[u+101,co]


    return pu,pc,pbr,pb,pr,pk,\
           pu1,pc1,pbr1,pb1,pr1,pk1


def gh(co):
    ss=np.concatenate([ghgh(0,co),
                       ghgh(4,co),
                       ghgh(8,co),
                       ghgh(12,co),
                       ghgh(16,co),
                       ghgh(20,co),
                       ghgh(24,co),
                       ghgh(28,co),
                       ghgh(32,co),
                       ghgh(36,co),
                       ghgh(40,co),
                       ghgh(44,co),
                       ghgh(48,co),
                       ghgh(52,co),
                       ghgh(56,co),
                       ghgh(60,co),
                       ghgh(5,co),
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
                       ghgh(31,co)])
    return ss