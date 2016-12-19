
# -*- coding: utf-8 -*-
import numpy as np
from sklearn.utils import shuffle
from sklearn.cross_validation import train_test_split
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import dfdf
from sklearn import preprocessing
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model
from pylab import load
def model(f,g,h,j):
    # Загрузка данных
    a=dfdf.dfdf(f,g ).unstack().head(165)
    b=dfdf.dfdf(h,j).unstack().head(165)
    y=np.concatenate([a.loc[a.index]])
    X=np.concatenate([b.loc[b.index]])
    X=X.reshape(165,1)
    y=y.reshape(165,1)

    # Load the diabetes dataset
    #  Use only one feature

    # Split the data into training/testing sets
    X_train = X[:-70]
    X_test = X[-95:]
    # Split the targets into training/testing sets
    y_train = y[:-70]
    y_test = y[-95:]
    # Create linear regression object
    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    regr.fit(X_train, y_train)
    # The coefficients
    plt.scatter(X_test, y_test,  color='black')
    plt.plot(X_test, regr.predict(X_test), color='blue',
         linewidth=3)

    plt.xticks(())
    plt.yticks(())
    return (plt.show(),'Coefficients: \n', regr.coef_,
            "Residual sum of squares: %.2f" % np.mean((regr.predict(X_test) - y_test) ** 2),
            'Variance score: %.2f' % regr.score(X_test, y_test))



print(model('D:\work\data1\Data_mlv_rost_multireg_perebor_double.xlsx',
            "H2:H166",'D:\work\data1\Data_mlv_rost_multireg_perebor_double.xlsx',"G2:G166"))