import csv
import numpy as np
import numpy
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

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

data2=[]
with open("ch.csv") as csvfile2:
    reader2 = csv.reader(csvfile2) # change contents to floats
    for row in reader2: # each row is a list
        data2.append(row)
# print(data2)
fvs_lexical2 = np.zeros((23, 1), np.float64)
kk=0
zz=0
while(kk<23):
    while(zz<1):
        fvs_lexical2[kk, zz] = data2[kk][zz]
        zz+=1
    zz=0
    kk+=1
# print(fvs_lexical2)

# print(fvs_lexical)

# Load the diabetes dataset
# diabetes = datasets.load_diabetes()

tips=pd.read_csv("user.csv")
# Use only one feature
diabetes_X = fvs_lexical[:, np.newaxis, 1]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = fvs_lexical2[:-20]
diabetes_y_test = fvs_lexical2[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)
# print(diabetes_y_pred)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()