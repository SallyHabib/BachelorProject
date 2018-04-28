from sklearn.svm import SVR
import numpy as np
import pandas as pd
from numpy.ma.core import ravel
from sklearn.model_selection import train_test_split
import csv
from sklearn.metrics import accuracy_score,precision_score


n_samples, n_features = 10, 5
np.random.seed(0)
y = np.random.randn(n_samples)
X = np.random.randn(n_samples, n_features)
wine = pd.read_csv('user.csv')
yy=pd.read_csv('cons.csv')
X = wine
y = ravel(yy)
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
print(fvs_lexical3)
print(svr.predict(fvs_lexical3))
print(svr.score(X_test, y_test))
print(y_test)
print(predictions)
# precision=precision_score(y_test, predictions,average=None)