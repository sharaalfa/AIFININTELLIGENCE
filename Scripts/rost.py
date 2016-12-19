import pandas as pd
import numpy as np
a=pd.read_excel('D:/work/data1/Model_mlv_multireg.xlsx')
def bbb(val,i,co):
    pu0=a.loc[i,co]-val
    pu1=a.loc[i+1,co]-a.loc[i,co]
    pu2=a.loc[i+2,co]-a.loc[i+1,co]
    pu3=a.loc[i+3,co]-a.loc[i+2,co]
    pu4=a.loc[i+4,co]-a.loc[i+3,co]
    pu5=a.loc[i+5,co]-a.loc[i+4,co]
    pu6=a.loc[i+6,co]-a.loc[i+5,co]
    pu7=a.loc[i+7,co]-a.loc[i+6,co]
    pu8=a.loc[i+8,co]-a.loc[i+7,co]
    pu9=a.loc[i+9,co]-a.loc[i+8,co]
    pu10=a.loc[i+10,co]-a.loc[i+9,co]
    pu11=a.loc[i+11,co]-a.loc[i+10,co]
    pu12=a.loc[i+12,co]-a.loc[i+11,co]
    pu13=a.loc[i+13,co]-a.loc[i+12,co]
    pu14=a.loc[i+14,co]-a.loc[i+13,co]
    pu15=a.loc[i+15,co]-a.loc[i+14,co]
    pu16=a.loc[i+16,co]-a.loc[i+15,co]
    pu17=a.loc[i+17,co]-a.loc[i+16,co]
    pu18=a.loc[i+18,co]-a.loc[i+17,co]
    pu19=a.loc[i+19,co]-a.loc[i+18,co]
    pu20=a.loc[i+20,co]-a.loc[i+19,co]
    pu21=a.loc[i+21,co]-a.loc[i+20,co]
    pu22=a.loc[i+22,co]-a.loc[i+21,co]
    pu23=a.loc[i+23,co]-a.loc[i+22,co]
    pu24=a.loc[i+24,co]-a.loc[i+23,co]
    pu25=a.loc[i+25,co]-a.loc[i+24,co]
    pu26=a.loc[i+26,co]-a.loc[i+25,co]
    pu27=a.loc[i+27,co]-a.loc[i+26,co]
    pu28=a.loc[i+28,co]-a.loc[i+27,co]
    pu29=a.loc[i+29,co]-a.loc[i+28,co]
    pu30=a.loc[i+30,co]-a.loc[i+29,co]
    pu31=a.loc[i+31,co]-a.loc[i+30,co]
    pu32=a.loc[i+32,co]-a.loc[i+31,co]



    return pu0,pu1,pu2,pu3,pu4,pu5,pu6,\
           pu7,pu8,pu9,pu10,pu11,pu12,\
           pu13,pu14,pu15,pu16,pu17,pu18,\
           pu19,pu20,pu21,pu22,pu23,pu24,\
           pu25,pu26,pu27,pu28,pu29,pu30,\
           pu31,pu32


def b(co):
    ss=np.concatenate([bbb(0,0,co),bbb(0,33,co),bbb(0,66,co),bbb(0,99,co),bbb(0,132,co)])


    return ss


def bbb1(i,co):
    pu0=a.loc[i,co]
    pu1=a.loc[i+1,co]
    pu2=a.loc[i+2,co]
    pu3=a.loc[i+3,co]
    pu4=a.loc[i+4,co]
    pu5=a.loc[i+5,co]
    pu6=a.loc[i+6,co]
    pu7=a.loc[i+7,co]
    pu8=a.loc[i+8,co]
    pu9=a.loc[i+9,co]
    pu10=a.loc[i+10,co]
    pu11=a.loc[i+11,co]
    pu12=a.loc[i+12,co]
    pu13=a.loc[i+13,co]
    pu14=a.loc[i+14,co]
    pu15=a.loc[i+15,co]
    pu16=a.loc[i+16,co]
    pu17=a.loc[i+17,co]
    pu18=a.loc[i+18,co]
    pu19=a.loc[i+19,co]
    pu20=a.loc[i+20,co]
    pu21=a.loc[i+21,co]
    pu22=a.loc[i+22,co]
    pu23=a.loc[i+23,co]
    pu24=a.loc[i+24,co]
    pu25=a.loc[i+25,co]
    pu26=a.loc[i+26,co]
    pu27=a.loc[i+27,co]
    pu28=a.loc[i+28,co]
    pu29=a.loc[i+29,co]
    pu30=a.loc[i+30,co]
    pu31=a.loc[i+31,co]
    pu32=a.loc[i+32,co]



    return pu0,pu1,pu2,pu3,pu4,pu5,pu6,\
           pu7,pu8,pu9,pu10,pu11,pu12,\
           pu13,pu14,pu15,pu16,pu17,pu18,\
           pu19,pu20,pu21,pu22,pu23,pu24,\
           pu25,pu26,pu27,pu28,pu29,pu30,\
           pu31,pu32


def b1(co):
    ss=np.concatenate([bbb1(0,co),bbb1(33,co),bbb1(66,co),bbb1(99,co),bbb1(132,co)])


    return ss



def bbb2(val,i,co):
    pu0=(a.loc[i,co]-val)/val
    pu1=(a.loc[i+1,co]-a.loc[i,co])/a.loc[i,co]
    pu2=(a.loc[i+2,co]-a.loc[i+1,co])/a.loc[i+1,co]
    pu3=(a.loc[i+3,co]-a.loc[i+2,co])/a.loc[i+2,co]
    pu4=(a.loc[i+4,co]-a.loc[i+3,co])/a.loc[i+3,co]
    pu5=(a.loc[i+5,co]-a.loc[i+4,co])/a.loc[i+4,co]
    pu6=(a.loc[i+6,co]-a.loc[i+5,co])/a.loc[i+5,co]
    pu7=(a.loc[i+7,co]-a.loc[i+6,co])/a.loc[i+6,co]
    pu8=(a.loc[i+8,co]-a.loc[i+7,co])/a.loc[i+7,co]
    pu9=(a.loc[i+9,co]-a.loc[i+8,co])/a.loc[i+8,co]
    pu10=(a.loc[i+10,co]-a.loc[i+9,co])/a.loc[i+9,co]
    pu11=(a.loc[i+11,co]-a.loc[i+10,co])/a.loc[i+10,co]
    pu12=(a.loc[i+12,co]-a.loc[i+11,co])/a.loc[i+11,co]
    pu13=(a.loc[i+13,co]-a.loc[i+12,co])/a.loc[i+12,co]
    pu14=(a.loc[i+14,co]-a.loc[i+13,co])/a.loc[i+13,co]
    pu15=(a.loc[i+15,co]-a.loc[i+14,co])/a.loc[i+14,co]
    pu16=(a.loc[i+16,co]-a.loc[i+15,co])/a.loc[i+15,co]
    pu17=(a.loc[i+17,co]-a.loc[i+16,co])/a.loc[i+16,co]
    pu18=(a.loc[i+18,co]-a.loc[i+17,co])/a.loc[i+17,co]
    pu19=(a.loc[i+19,co]-a.loc[i+18,co])/a.loc[i+18,co]
    pu20=(a.loc[i+20,co]-a.loc[i+19,co])/a.loc[i+19,co]
    pu21=(a.loc[i+21,co]-a.loc[i+20,co])/a.loc[i+20,co]
    pu22=(a.loc[i+22,co]-a.loc[i+21,co])/a.loc[i+21,co]
    pu23=(a.loc[i+23,co]-a.loc[i+22,co])/a.loc[i+22,co]
    pu24=(a.loc[i+24,co]-a.loc[i+23,co])/a.loc[i+23,co]
    pu25=(a.loc[i+25,co]-a.loc[i+24,co])/a.loc[i+24,co]
    pu26=(a.loc[i+26,co]-a.loc[i+25,co])/a.loc[i+25,co]
    pu27=(a.loc[i+27,co]-a.loc[i+26,co])/a.loc[i+26,co]
    pu28=(a.loc[i+28,co]-a.loc[i+27,co])/a.loc[i+27,co]
    pu29=(a.loc[i+29,co]-a.loc[i+28,co])/a.loc[i+28,co]
    pu30=(a.loc[i+30,co]-a.loc[i+29,co])/a.loc[i+29,co]
    pu31=(a.loc[i+31,co]-a.loc[i+30,co])/a.loc[i+30,co]
    pu32=(a.loc[i+32,co]-a.loc[i+31,co])/a.loc[i+31,co]



    return pu0,pu1,pu2,pu3,pu4,pu5,pu6,\
           pu7,pu8,pu9,pu10,pu11,pu12,\
           pu13,pu14,pu15,pu16,pu17,pu18,\
           pu19,pu20,pu21,pu22,pu23,pu24,\
           pu25,pu26,pu27,pu28,pu29,pu30,\
           pu31,pu32


def b2(co):
    ss=np.concatenate([bbb2(0,0,co),bbb2(0,33,co),bbb2(0,66,co),bbb2(0,99,co),bbb2(0,132,co)])


    return ss
