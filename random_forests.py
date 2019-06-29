
# coding: utf-8

# In[42]:


import pandas as pd
df=pd.read_csv("http://13.234.66.67/summer19/datasets/social.csv")


# In[43]:


df.info()


# In[44]:


df.head(5)


# In[45]:


filterdata=df.iloc[0:,2:].values


# In[46]:


features=filterdata[0:,0:2]


# In[47]:


label=filterdata[0:,2]


# In[48]:


from sklearn.model_selection import train_test_split 


# In[49]:


X,x,Y,y=train_test_split(features,label,test_size=0.2)


# In[50]:


from sklearn.preprocessing import StandardScaler


# In[51]:


sc=StandardScaler()


# In[52]:


X=sc.fit_transform(X)


# In[53]:


x=sc.transform(x)


# In[54]:


#calling random forest classifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


# In[88]:


Rclf=RandomForestClassifier(n_estimators=20)
#10 by default


# In[89]:


#training data
trained=Rclf.fit(X,Y)


# In[90]:


#now predicting 
output=trained.predict(x)


# In[91]:


from sklearn.metrics import accuracy_score


# In[92]:


accuracy_score(output,y)

