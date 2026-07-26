import pandas as pd
import numpy as np
import sys 
import matplotlib.pyplot as plt
import seaborn as sbs
import requests 
np.set_printoptions(suppress=True)
import time 
import mysql.connector

df=pd.read_csv("learning fundamentals/train.csv")

plt.plot([1,2,3],[5,7,2])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("My Graph")
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
sbs.countplot(data=df,x="Pclass")
plt.show()



print(df.head())
sbs.countplot(x=df["Survived"])
plt.show()
sbs.countplot(x=df["Pclass"])
plt.show()
sbs.countplot(data=df, x="Pclass", hue="Survived")
plt.show()
sbs.histplot(data=df, x="Age",bins=10)
plt.show()
plt.hist(df['Age'])
plt.show()
sbs.displot(data=df,x=df["Age"])
plt.show()
sbs.displot(data=df,x="Age",hue="Survived",kind="kde")
plt.show()
corr=df.corr(numeric_only=True)
sbs.heatmap(corr)
plt.show()
sbs.boxplot(data=df, x="Age")
plt.show()
sbs.pairplot(df,hue="Survived")
plt.show()
#sbs.pairplot(df)
#plt.show()      eveerythuing plotted against everything
