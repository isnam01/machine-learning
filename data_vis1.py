#!/usr/bin/python
import matplotlib.pyplot as plt1
import pandas as pd
df=pd.read_csv("student.csv")
plt1.pie(df.iloc[0:,1],labels=df.iloc[0:,0],autopct="%1.1f%%")
plt1.legend()
plt1.show()
