import pandas as pd
import numpy as np
import sys 
import matplotlib.pyplot as plt
import seaborn as sbs
import requests 
np.set_printoptions(suppress=True)
import time 
import mysql.connector
print(plt.get_backend())


#                         SQL FILES :

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college"
)
curr=conn.cursor() # cursor
print("Connected successfully!")


query = "SELECT * FROM students"
df = pd.read_sql(query, conn)
print(df)
 # we print exisating table in sql
 # now we store table in sql
df = pd.DataFrame({
    "id": [101, 102, 103],
    "name": ["Alice", "Bob", "Charlie"],
    "age": [20, 21, 19],
    "cgpa": [9.2, 8.8, 9.5]
})
print(df)
curr.execute("""
CREATE TABLE IF NOT EXISTS pandas_students (
    id INT,
    name VARCHAR(50),
    age INT,
    cgpa FLOAT
)
""")
query = """
INSERT INTO pandas_students (id, name, age, cgpa)
VALUES (%s, %s, %s, %s)
"""

for row in df.itertuples(index=False):
    curr.execute(query, tuple(row))
# putting values from pd dataframe to sql row by row
# conn.commit()                        commiting changes is important
conn.close()

#                       json files;

df = pd.read_json("learning fundamentals\students.json")
print(df)



# now we work with apis :

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
print(response.status_code)
print(response.text)
data = response.json()
print(type(data))

print(data[0].keys())
print(data[0]["address"])
print(data[0]["address"]["geo"])

 # by doing this we get 1 big file and nested json files have columns with dictionaries

df = pd.DataFrame(data)
print(df.head())
print(df.columns)
# but with this nested jsons turn into column.column type of data

df = pd.json_normalize(data)
print(df.head())
print(df.columns)
