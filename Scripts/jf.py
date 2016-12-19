import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor
from sklearn.grid_search import GridSearchCV
from sklearn.svm import SVC, SVR
from sklearn import ensemble
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score



from pylab import *
plt.style.use('ggplot')
a = pd.read_excel('D:\work\data1\Data_mlv_rost_multireg_perebor.xlsx')
# Переменование колонок на факторы и классы (для простоты)
a.columns=\
    ['A1']+['A2']+['classA3']+['A4']+['classA5']\
    +['A6']+['A7']+['classA8'] +['classA9']+['A10']+['classA11']\
    +['classA12']+['B13']+['B14']+['B15']+['B16']+['B17']+['B18']\
    +['classB19']+['classB20']+['classB21']+['classB22']+['A23']\
    +['A24']+['classB25']+['classB26']

# Перевод из количественых значений -1 и 1 к категориям полжительное и отрицательное
# Для бинарных факторов и классов
a.at[a['B13']==-1,'B13']='negative'
a.at[a['B13']==1,'B13']='positive'
a.at[a['B14']==-1,'B14']='negative'
a.at[a['B14']==1,'B14']='positive'
a.at[a['B15']==-1,'B15']='negative'
a.at[a['B15']==1,'B15']='positive'
a.at[a['B16']==-1,'B16']='negative'
a.at[a['B16']==1,'B16']='positive'
a.at[a['B17']==-1,'B17']='negative'
a.at[a['B17']==1,'B17']='positive'
a.at[a['B18']==-1,'B18']='negative'
a.at[a['B18']==1,'B18']='positive'
a.at[a['classB19']==-1,'classB19']='negative'
a.at[a['classB19']==1,'classB19']='positive'
a.at[a['classB20']==-1,'classB20']='negative'
a.at[a['classB20']==1,'classB20']='positive'
a.at[a['classB21']==-1,'classB21']='negative'
a.at[a['classB21']==1,'classB21']='positive'
a.at[a['classB22']==-1,'classB22']='negative'
a.at[a['classB22']==1,'classB22']='positive'
a.at[a['classB25']==-1,'classB25']='negative'
a.at[a['classB25']==1,'classB25']='positive'
a.at[a['classB26']==-1,'classB26']='negative'
a.at[a['classB26']==1,'classB26']='positive'
#a.to_excel('D:\work\data1\Data.xlsx')
# С помощью метода describe() по умолчанию получим для количественных признаков
# их количество(count), среднее значение(mean), стандартное отклонение(std),
# минимальное, максимальное, медиана, значения нижнего и верхнего квартилей
#print(a.describe())
#a.to_excel('D:\work\data1\Data.xlsx')
#a.describe().to_excel('D:\work\data1\Data_describe.xlsx')
# Выделяем количественные и категориальные признаки
categorical_columns=[c for c in a.columns if a[c].dtype.name=='object']
numerical_columns=[c for c in a.columns if a[c].dtype.name !='object']
# Получаем информацию по катеогриальным признакам: общее число заполненных
# ячеек(count), количество значений, которые принимает данный признак(unique),
# самое популярное значение(top), кол-во объектов,
# в к-х встречается самое частое значение данного признака(freq)
#print(a[categorical_columns].describe())
#a[categorical_columns].describe().to_excel('D:\work\data1\Data_describe_categorical.xlsx')
#print(a[numerical_columns])
#a.describe(include=[object])
#for c in categorical_columns:
    #print(a[c].unique())
# Гистограмма и диаграммы рассеяния для количественных
#figure()
#scatter_matrix(a,alpha=0.05,figsize=(10,10))
#show()
#print(a.corr())
#a.corr().to_excel('D:\work\data1\Data_describe_corr.xlsx')
#col1='A2'
#col2='A4'
#figure()
#plt.figure(figsize=(10,6))

#plt.scatter(a[col1][a['classA3']=='+'],
 #           a[col2][a['classA3']=='+'],
  #          alpha=0.75,
   #         color='red',
    #        label='+')
#plt.scatter(a[col1][a['classA5']=='-'],
 #           a[col2][a['classA5']=='-'],
 #           alpha=0.75,
  #          color='blue',
   #         label='-')

#plt.xlabel(col1)
#plt.ylabel(col2)
#plt.legend(loc='best');
#plt.show()
# Заполним пропущенные медианными значениями для количественных
# Для категориальным наиболее популярным значением признака

a=a.fillna(a.median(axis=0),axis=0)

#Wprint(a.count(axis=0))
a['B13']=a['B13'].fillna('negative')
a_describe=a.describe(include=[object])
for c in categorical_columns:
    a[c]=a[c].fillna(a_describe[c]['top'])
#print(a.describe(include=[object]))
#a.describe(include=[object]).to_excel('D:\work\data1\Data_describe_categorical_noNaN.xlsx')
#a.to_excel('D:\work\data1\Data_noNaN.xlsx')

# выделим бинарные признаки и переводим в ноль и единицу
binary_columns=[c for c in categorical_columns if a_describe[c]['unique']==2]
a.at[a['B13']=='negative', 'B13']=0
a.at[a['B13']=='positive', 'B13']=1
a_describe=a.describe(include=[object])
for c in binary_columns[1:]:
    top=a_describe[c]['top']
    top_items=a[c]==top
    a.loc[top_items,c]=0
    a.loc[np.logical_not(top_items),c]=1
#a = pd.DataFrame(a, dtype=float)

#print(a[binary_columns].describe())
#a[binary_columns].describe().to_excel('D:\work\data1\Data_describe_categorical_noNaN_zero_one.xlsx')
# Приведем количественные признаки к нулевому среднему и единичному
# среднеквадратичному отклонению
a_numerical=a[numerical_columns]
a_numerical=(a_numerical-a_numerical.mean())/a_numerical.std()
#a_numerical.describe().to_excel('D:\work\data1\Data_describe_normal.xlsx')
#a_numerical.to_excel('D:\work\data1\Data_describe_normal.xlsx')
a=pd.concat((a_numerical,a[binary_columns]),axis=1)
a = pd.DataFrame(a, dtype=float)
#a.to_excel('D:\work\data1\Data_normal.xlsx')
# Разграничим X и y
X=a.drop(['classA3'],axis=1)
X=X.drop(['classA5'],axis=1)
X=X.drop(['classA8'],axis=1)
X=X.drop(['classA9'],axis=1)
X=X.drop(['classA11'],axis=1)
X=X.drop(['classA12'],axis=1)
X=X.drop(['classB19'],axis=1)
X=X.drop(['classB20'],axis=1)
X=X.drop(['classB21'],axis=1)
X=X.drop(['classB22'],axis=1)
X=X.drop(['classB25'],axis=1)
X=X.drop(['classB26'],axis=1)
X=X.drop(['A1'],axis=1)
X=X.drop(['A2'],axis=1)
X=X.drop(['A6'],axis=1)
X=X.drop(['A7'],axis=1)
X=X.drop(['A4'],axis=1)
X=X.drop(['A10'],axis=1)
X=X.drop(['A23'],axis=1)
X=X.drop(['A24'],axis=1)
#X=X.drop(['B13'],axis=1)
#X=X.drop(['B14'],axis=1)
#X=X.drop(['B15'],axis=1)
#X=X.drop(['B16'],axis=1)
#X=X.drop(['B17'],axis=1)
#X=X.drop(['B18'],axis=1)

neo=a['classA3']
err=a['classA5']
y2=a['classA8']
y3=a['classA9']
#y4=a['classA11']
#y5=a['classA12']
y6=a['classB19']
y7=a['classB20']
y8=a['classB21']
y9=a['classB22']
y10=a['classB25']
y11=a['classB26']
feature_names=X.columns
#print(feature_names)
# k-ближайших соседей для категриальных признаков
# и бинарного ряда отток/приток(+ либо -), рост/падение
#  по чистым ошибкам и пропускам и и не только
# платежного баланса в будущем по известным данным
# биржевых индексов и РЕПО
def k_neighbor(y):



    X_train,X_test,y_train,y_test=\
        train_test_split(X,y,test_size=0.3,random_state=11)
    testModels=DataFrame()
    tmp={}
    try:
        n_neighbors_array=[1,3,5]
        knn=KNeighborsClassifier()
        grid=GridSearchCV(knn,param_grid={'neighbors':n_neighbors_array})
        grid.fit(X_train,y_train)
        best_cv_err=1-grid.best_score_
        best_n_neighbors=grid.best_estimator_.n_neighbors
        knn=KNeighborsClassifier()
        knn.fit(X_train,y_train)
        models=[KNeighborsClassifier(algorithm='auto',
                     leaf_size=30,metric='minkowski',
                     metric_params=None,n_neighbors= best_n_neighbors,
                     p=2,weights='uniform')]
        y_train_predict=knn.predict(X_train)
        y_test_predict=knn.predict(X_test)

        err_train=np.mean(y_train!=y_train_predict)
        err_test=np.mean(y_test!=y_test_predict)
        return err_train, err_test, knn.predict(X_test)
    except ValueError:
        def reg(a,b):
            m = str(a)
            tmp['Model'] = m
            n=b
            n.fit(X_train,y_train)
            tmp['Коэффициент детерминации'] = r2_score(y_test, n.predict(X_test))
            return tmp
        #s1=reg('LinearRegression',LinearRegression())
        #s2=reg('RandomForestRegressor',RandomForestRegressor(n_estimators=100, max_features ='sqrt'))
        #s3=reg('KNeighborsRegressor',KNeighborsRegressor(n_neighbors=6))
        #s4=reg('SVR)',SVR(kernel='linear'))
    print(reg('LinearRegression',LinearRegression()),
              reg('RandomForestRegressor',RandomForestRegressor(n_estimators=100, max_features ='sqrt')))






# уменьшение ошибки k ближайших соседей с помощью класса
# GridSearchCV-поиск наилучшего набора параметров
# Найдем наилучшее значение основого параметра k-
# число соседей с минимальной ошибкой на тестовой выборке
def p(y): ## a-перечисляем значения в []-скобках, н-р,
    # [1,3,5,7,10,14]
    n_neighbors_array=[2]
    X_train,X_test,y_train,y_test=\
        train_test_split(X,y,test_size=0.3,random_state=11)

    knn=KNeighborsClassifier()


    grid=GridSearchCV(knn,param_grid={'neighbors':n_neighbors_array})
    grid.fit(X_train,y_train)
    best_cv_err=1-grid.best_score_
    best_n_neighbors=grid.best_estimator_.n_neighbors
    return best_cv_err, best_n_neighbors

print(k_neighbor(y11))







