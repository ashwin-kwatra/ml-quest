import pandas as pd
import numpy as np
import sys 
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)
import time 
print(plt.get_backend())

movies=pd.read_csv("imdb-top-1000.csv")
print(movies.head(1))
genres=movies.groupby("Genre")
print(genres.sum())
print(genres.first()) # first elemnt of every group
print(genres.get_group('Horror'))
print(genres.groups) # index of each item of each group
print(genres.describe())