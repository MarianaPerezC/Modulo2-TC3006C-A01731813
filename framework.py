#!/usr/bin/env python
# coding: utf-8

# In[93]:


import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


datos=pd.read_csv("GDP.csv")
for i in range(len(datos)):
    datos['DATE'][i]=datos['DATE'][i][0:4]
datos = datos.drop_duplicates(subset=['DATE'])
datos['DATE']=pd.to_numeric(datos['DATE'], errors='coerce')
X=datos['DATE'].values
y=datos['GDP'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)
X_train=X_train.reshape(-1,1)
X_test=X_test.reshape(-1,1)
regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)
print('Coeficiente X_1: \n', regr.coef_)
print('Intercepto: \n', regr.intercept_)
y_pred=regr.predict(X_test)
print("Error cuadratico medio: %.2f" % mean_squared_error(y_test, y_pred))
print("Año",X_test[1],"Valor real ", y_test[1],"Valor Predicho ",y_pred[1])
