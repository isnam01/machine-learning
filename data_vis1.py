#!/usr/bin/python
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("student.csv")
plt.pie(df.iloc[0:,1],labels=df.iloc[0:,0],autopct="%1.1f%%")
plt.legend()
plt.show()
