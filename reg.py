import csv
import numpy as np
import numpy
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from numpy.ma.core import ravel

results=np.zeros([23,31])
results2=[]
data=[]
i=0
j=1
with open("user.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        data.append(row)
fvs_lexical = np.zeros((23, 3), np.float64)
k=0
z=0
while(k<23):
    while(z<3):
        fvs_lexical[k, z] = data[k][z]
        z+=1
    z=0
    k+=1

# data2=[]
# with open("ch.csv") as csvfile2:
#     reader2 = csv.reader(csvfile2) # change contents to floats
#     for row in reader2: # each row is a list
#         data2.append(row)
# # print(data2)
# fvs_lexical2 = np.zeros((23, 1), np.float64)
# kk=0
# zz=0
# while(kk<23):
#     while(zz<1):
#         fvs_lexical2[kk, zz] = data2[kk][zz]
#         zz+=1
#     zz=0
#     kk+=1
# print(fvs_lexical2)

# print(fvs_lexical)
wine = pd.read_csv('user.csv')
yy=pd.read_csv('ch.csv')
X = wine
y = ravel(yy)
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y)
scaler = StandardScaler()
scaler.fit(X_train)
StandardScaler(copy=True, with_mean=True, with_std=True)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
mlp = MLPRegressor(hidden_layer_sizes=(13,13,13),max_iter=5000)
print(mlp.fit(X_train,y_train))
predictions = mlp.predict(X_test)
print(predictions)
