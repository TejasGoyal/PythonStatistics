import pandas as pd
import numpy as np

#Basic Pandas Operation

url = "../Cartwheeldata.csv"
df = pd.read_csv(url)

a = df.head()   #five rows
b = df.iloc[6:10,2:4]   #matlab syntax , 6 included but not 10, 2 included but not 4
c = df.Score.unique()
d = df.groupby(['Gender','GenderGroup']).size()

print("Head", a)
print("IntegerLocation", b)
print("\n")
print("Score Unique",c)
print("\n")
print("Grouping\n",d)
