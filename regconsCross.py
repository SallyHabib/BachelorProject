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
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import LeaveOneOut 

results=np.zeros([24,31])
results2=[]
data=[]
i=0
j=1
with open("user.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        data.append(row)
fvs_lexical = np.zeros((24, 56), np.float64)
k=0
z=0
while(k<24):
    while(z<56):
        fvs_lexical[k, z] = data[k][z]
        z+=1
    z=0
    k+=1

data2=[]
with open("cons.csv") as csvfile2:
    reader2 = csv.reader(csvfile2) # change contents to floats
    for row in reader2: # each row is a list
        data2.append(row)
# print(data2)
fvs_lexical2 = np.zeros((24, 1), np.float64)
kk=0
zz=0
while(kk<24):
    while(zz<1):
        fvs_lexical2[kk, zz] = data2[kk][zz]
        zz+=1
    zz=0
    kk+=1
# print(fvs_lexical2)

# print(fvs_lexical)
data3=[]
with open("test.csv") as csvfile3:
    reader3 = csv.reader(csvfile3) # change contents to floats
    for row in reader3: # each row is a list
        data3.append(row)
        # print(row)
fvs_lexical3 = np.zeros((1, 56), np.float64)
kkk=0
zzz=0
while(kkk<1):
    while(zzz<56):
        fvs_lexical3[kkk, zzz] = data3[kkk][zzz]
        zzz+=1
    zzz=0
    kkk+=1
# print(fvs_lexical3)
wine = pd.read_csv('user.csv')
yy=pd.read_csv('cons.csv')
X = fvs_lexical
y = ravel(fvs_lexical2)
# print(y)
# X_train, X_test, y_train, y_test = train_test_split(X, y)
loo = LeaveOneOut()
loo.get_n_splits(X)
for train_index, test_index in loo.split(X):
    # print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

scaler = StandardScaler()
scaler.fit(X_train)
StandardScaler(copy=True, with_mean=True, with_std=True)
X_train = scaler.transform(X_train)
# print(X_train)
X_test = scaler.transform(X_test)
mlp = MLPRegressor(hidden_layer_sizes=(8,8,8),max_iter=5000,solver='lbfgs')
mlp.fit(X_train,y_train)
# predictions = mlp.predict(X_test)
# print(X_test)
# print(mlp.n_iter_)
testing_scalar=scaler.transform(fvs_lexical3)
testing=mlp.predict(testing_scalar)
print(testing)
print(mlp.score(X_test, y_test))
