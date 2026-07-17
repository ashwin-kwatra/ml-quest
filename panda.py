import pandas as pd
import numpy as np
np.set_printoptions(suppress=True)
import time 
#making basic series with arrays

country= ['a','b','c','d','e','f','g','g']
country=(pd.Series(country))
print(country)
marks=[11,34,76,89,11,55,42,60]
marks=(pd.Series(marks,index=country,name="countries ke marks",))
print(marks)

# making basic series with dictionaries
ma2={'maths':10 ,"english":20 , "hindi":30}
ma2=(pd.Series(ma2))
print(ma2)
print(ma2.size)
print(ma2.dtype)
print(ma2.name)
print(ma2.is_unique)
print(country.is_unique)# checks if all elemt r unique
print(type(marks.index))
# ans=pd.read_csv('path',index_column="name of columsn in csv file")
print(ma2.head()) # first 5 elemnt print for preview
print(ma2.sample()) # randomly 1 nikal deta h , default 1
print('')
print(marks.value_counts)
print(marks.sort_values())
print(marks.sort_values(ascending=False).head(1)) # BIGGEST ELEMNET
marks.sort_values(inplace=True) # permanent change
print(marks)

marks=[11,34,76,89,11,55,42,60]
marks=(pd.Series(marks,index=country,name="countries ke marks"))
print(ma2.count)
musclee=pd.read_csv('muscle_progress.csv')
print(musclee)
print(musclee.shape)
print(musclee.dtypes)
print(musclee.columns)
print(musclee.values) # gives numpy array
print(musclee.info())
print(musclee.describe()) # numerical colums ke upar
print(musclee.sample())
print(musclee.isnull().sum())
# musclee.rename(columns={"sleep_hours":"daily_sleep"}) ------- renames the column
# this change is temprory , to make it permament , use INPLACE
# sum , min , max , median etc functions work
print(type(musclee[['sleep_hours','weight_kg']])) # multiple columns = dataframe
print(type(musclee["day"])) # single columns= series




