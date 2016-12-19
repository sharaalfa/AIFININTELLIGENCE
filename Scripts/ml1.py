
# -*- coding: utf-8 -*-
from pandas import read_csv, DataFrame
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import RFE
import numpy as np

dataset = read_csv('D:\work\data\dfor_ml1.csv', sep=';', decimal=',')

dataset1 = dataset.drop(['Unnamed: 0'], axis=1)
trg = dataset1[['Y']]
trn = dataset1.drop(['Y'], axis=1)
Y = np.array(trg, dtype=np.float32)
X = np.array(trn, dtype=np.float32)
normalized_X = preprocessing.normalize(trn)
standardized_X = preprocessing.scale(trn)
model = ExtraTreesClassifier()
model.fit(trn, trg)
print(model.feature_importances_)

model = LinearRegression()
# create the RFE model and select 3 attributes
rfe = RFE(model, 3)
rfe = rfe.fit(trn, trg)
# summarize the selection of the attributes
print(rfe.support_)
print(rfe.ranking_)

model = LinearRegression()
model.fit(trn, trg)
print(model)
# make predictions
expected = trg
predicted = model.predict(trn)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))

#models = [LinearRegression(),#метод наименьших квадратов
#          RandomForestRegressor(n_estimators=100, max_features='sqrt'), #случайный лес
#          KNeighborsRegressor(n_neighbors=6),
 #         SVR(kernel='linear'),#метод опорных векторов с линейным ядром
  #        LogisticRegression() # логистическая регрессия
         # ]
#Xtrn, Xtest, Ytrn, Ytest = train_test_split(trn, trg, test_size=0.4)
# создаем временные структуры
#TestModels = DataFrame()
#tmp = {}
# для каждой модели из списка
#for model in models:
    # получаем имя модели
 #   m = str(model)
  #  tmp['Model'] = m[:m.index('(')]
    # для каждого столбцу результирующего набора
   # for i in xrange(Ytrn.shape[1]):
        # обучаем модель
    #    model.fit(Xtrn, Ytrn[:,i])
        # вычисляем коэффициент детерминации
     #   tmp['R2_Y%s'%str(i+1)] = r2_score(Ytest[:,0], model.predict(Xtest))
    # выписываем данные и итоговый DataFrame
    #TestModels = TestModels.append([tmp])
# делаем индекс по названию модели
#TestModels.set_index('Model', inplace=True)
#fig, axes = plt.subplots(ncols=2, figsize=(10,4))
#TestModels.R2_Y.plot(ax=axes[0], kind='bar', title='R2_Y')
