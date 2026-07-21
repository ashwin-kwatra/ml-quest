import pandas as pd
import numpy as np
import sys 
import matplotlib.pyplot as plt
import sklearn
from  sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

df=pd.read_csv("toy project\placement.csv")
print(df.head())
# steps 1 : pre process the data and define the work + eda + data selection
print(df.info())
df=df.iloc[:,1:]

# removing useless column
print(df.info())
plt.scatter(df['cgpa'],df['iq'],c=df['placement'])
plt.show()
# viewing how thew data looks 

X=df.iloc[:,0:2] # defining input columns
Y=df.iloc[:,-1] # defining outrput columns

# splitting training size ans scaling

xtrain, xtest, ytrain, ytest = train_test_split(X, Y, test_size=0.1)
scaler=StandardScaler()
xtrain=scaler.fit_transform(xtrain)  # compresswed data between -1 and 1
print(xtrain)
xtest=scaler.transform(xtest)

# working :
lf=LogisticRegression()
lf.fit(xtrain,ytrain)
# hogya model train ;D
ypred=lf.predict(xtest)
# loji hogyi predicition

print(ypred)
print(ytest)
print( accuracy_score(ypred,ytest))

# now we export our model with pickle
with open('toy project\model.pkl','wb') as f:
    pickle.dump(lf, f)

# also export the scaler
with open('toy project\scaler.pkl','wb') as f:
    pickle.dump(scaler, f)



