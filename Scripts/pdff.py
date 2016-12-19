import pyPdf
        for col6 in data_R6:
            f6 = col6
            for col7 in data_R7:
                f7 = col7
                for col8 in data_R8:
                    f8 = col8
                    for col9 in data_R9:
                        f9 = col9
                        for col10 in data_R10:
                            f10 = col10
                            for col11 in data_R11:
                                f11 = col11
                                for col12 in data_R12:
                                    f12 = col12
                                    for col13 in data_R13:
                                        f13 = col13
                                        for col14 in data_R14:
                                            f14 = col14
                                            for col15 in data_R15:
                                                f15 = col15
                                                sdf = f13.values
                                                d5 = f5[:4]
                                                d6 = f6[:4]
                                                d7 = f7[:4]
                                                d8 = f8[:4]
                                                d9 = f9[:4]
                                                d10 = f10[:4]
                                                d11 = f11[:4]
                                                d12 = f12[:4]
                                                d13 = f13[:4]
                                                d14 = f14[:4]
                                                d15 = f15[:4]
                                                p5 = d5[-1:]
                                                p6 = d6[-1:]
                                                p7 = d7[-1:]
                                                p8 = d8[-1:]
                                                p9 = d9[-1:]
                                                p10 = d10[-1:]
                                                p11 = d11[-1:]
                                                p12 = d12[-1:]
                                                p13 = d13[-1:]
                                                p14 = d14[-1:]
                                                p15 = d15[-1:]
                                                #s5 = p5.loc[:,[2,4,6,8]]
                                                s6 = p6.loc[:,[2,4,6,8]]
                                                s7 = p7.loc[:,[2,4,6,8]]
                                                s8 = p8.loc[:,[2,4,6,8]]
                                                s9 = p9.loc[:,[2,4,6,8]]
                                                s10 = p10.loc[:,[2,4,6,8]]
                                                s11 = p11.loc[:,[2,4,6,8]]
                                                s12 = p12.loc[:,[2,4,6,8]]
                                                s13 = p13.loc[:,[2,4,6,8]]
                                                s14 = p14.loc[:,[2,4,6,8]]
                                                #s15 = p15.loc[:,[2,4,6,8]]
                                                k6 = s6.unstack().head()
                                                k7 = s7.unstack().head()
                                                k8 = s8.unstack().head()
                                                k9 = s9.unstack().head()
                                                k10 = s10.unstack().head()
                                                k11 = s11.unstack().head()
                                                k12 = s12.unstack().head()
                                                k13 = s13.unstack().head()
                                                k14 = s14.unstack().head()
                                                #k15 = s15.unstack().head()
                                                Excel = win32com.client.Dispatch("Excel.Application")
d_mex = Excel.Workbooks.Open(u'D:\work\data\Consulta_Banxico (3).xls')
sheet = d_mex.ActiveSheet
vals_mx = [r[0].value for r in sheet.Range("AH59:AH101")]
i = 1

d_mex.Save()
d_mex.Close()
Excel.Quit()

#N_er_om = kz.append(rus.append(vals_mx))
#z = pd.concat([N_er_om, vals_mx.values])
#print(N_er_om)
#N_er_om.to_excel('D:\work\data\sss.xlsx')
#print(vals_mx)
data_mex = pd.read_excel('D:\work\data\Consulta_Banxico (3).xls', header=58, parse_cols="A,AH", index_col=0)
N_er_om = kz.append(rus.append(data_mex))
#z = pd.concat([N_er_om,data_mex])
#z = data_mex.append(N_er_om)
#data_mex.to_excel('D:\work\data\sd.xlsx')
#zz = N_er_om.combineAdd(N_er_om)
#d_r = s[:63]
#R = d_r[-1:]
#k1 = R.unstack().head()
#d_r = s[:126]
#R = d_r[-1:]
#k2 = R.unstack().head()
#d_r = s[:189]
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
repo = pd.read_csv('D:\work\data\ol_RUB.csv', sep=';', index_col=2, parse_dates = [2])
print(repo)
#x = pd.date_range('1/1/2005', periods=43, freq='AS')
y = repo['<VOL>']
figure()
plot(y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()
#repo_only = repo[['CLOSE']]
#print(repo_only)
#repo_only.to_excel('D:\work\data\Репо.xlsx')