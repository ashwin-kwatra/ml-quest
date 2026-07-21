import pandas as pd
import numpy as np
import sys 
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)
import time 
print(plt.get_backend())
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
 
 # to fetch data from dataframes :

print(type(musclee[['sleep_hours','weight_kg']])) # multiple columns = dataframe
print(type(musclee["day"])) # single columns= series
# musclee.set_index("day") ->>>>>>>>>>>>> turns the day column into the index column isntead of default
print(musclee.iloc[0])  # this also gives a series as an answer 
print(musclee.iloc[[0,1,2]]) # this gives dataframe
print(musclee.iloc[0:3,0:3]) # first 2 rows and first 3 columns only
print(musclee.loc[0:2,['day','weight_kg']]) # isme column ka name dena pdta h 
restday=musclee["workout_volume_kg"]==0
print(musclee[restday]) # filtering data
musclee["carbs"]=0          #creates a new column with defualt value =0
print(musclee.head(3))

# this function is sued to get a series 
# if we dont assign column and dont use squeze , it gets a dataframe
vk = pd.read_csv('kohli_ipl.csv',index_col='match_no').squeeze()
print(vk.head())
print(type(vk))
print(sys.getsizeof(vk))
print(sys.getsizeof(vk.astype('Int16'))) # reducing size
print(vk.info)
print(vk[vk.between(51,99)])
temp=pd.Series([1,2,np.nan,1,2,3,np.nan,4,np.nan,5,6,1,2,3,7,8,np.nan,np.nan])
#inplace=True laga skte h
# nan values ka duplicate bhi count karta hai
print(temp.drop_duplicates())
print(temp.duplicated().sum())
print(temp.isnull())
print(temp.fillna(0)) # replaces na with 0
temp.dropna(inplace=True)
print(temp)
print(musclee.value_counts())

# practise questions :

movies=pd.read_csv("movies.csv")
ipl=pd.read_csv("ipl-matches.csv")
print(movies.head(2))
print(ipl.head(2))
print(ipl[~ipl["MatchNumber"].str.isdigit()]["Player_of_Match"].value_counts()) # man of the match amount of matches that are final/semifinal
#ipl["TossDecision"].value_counts().plot(kind="pie") # plot batting/bowling toss descisions
# plt.show()
print(movies.sort_values('year_of_release'))
print(movies.sort_values(['year_of_release','title_x'])) # sorting values
print(ipl.set_index("MatchNumber"))
print(ipl.reset_index) # turns index  into a column and adds a defualt index back
print(movies.rename(columns={"imdb_id":"imdb"},inplace=True))

#a