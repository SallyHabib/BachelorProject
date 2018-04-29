from sklearn.svm import SVR
import numpy as np
import pandas as pd
from numpy.ma.core import ravel
from sklearn.model_selection import train_test_split
import csv
from sklearn.metrics import accuracy_score,precision_score

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

X = fvs_lexical
y = ravel(fvs_lexical2)
# print(y)


X_train, X_test, y_train, y_test = train_test_split(X, y)
clf = SVR(C=1.0, epsilon=0.2)
clf.fit(X_train, y_train) 
svr=SVR(C=2000, kernel='rbf', max_iter=5000, shrinking=True, tol=1, verbose=True,gamma=0.5)
svr.fit(X_train, y_train)
predictions=svr.predict(X_test)
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
print(svr.predict(fvs_lexical3))
# print(svr.score(X_test, y_test))
print(y_test)
print(predictions)
predictions_int=predictions.astype(int)
y_test_int=y_test.astype(int)
print(predictions_int)
predictions2=[51,51,51,51,51,51]
print(precision_score(y_test_int, predictions2, average='weighted'))