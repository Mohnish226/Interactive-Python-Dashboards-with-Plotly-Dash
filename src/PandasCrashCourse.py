import pandas as pd
import numpy as np

df = pd.read_csv("Data/salaries.csv")
print(df['Salary'].mean())
print(df[['Name','Salary']])

print(df['Age'] > 30)
print(df[df['Age']>30])

print(df['Age'].unique())
print(df['Age'].nunique())

print(df.columns)

print(df.info())
print(df.describe())

mat = np.arange(0,10).reshape(5,2)

df1 = pd.DataFrame(data=mat,columns=['A','B'])
print(df1)