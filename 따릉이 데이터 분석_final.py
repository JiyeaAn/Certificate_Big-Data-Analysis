#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install plotnine


# In[2]:


import pandas as pd
import numpy as np
from plotnine import *


# In[3]:


df = pd.read_csv('C:/Users/dkswl/K-digital ML/마포구/서울 마포구 공공자전거 대여 현황_2007_2012.CSV', encoding='cp949')
df.shape


# In[4]:


df.head(10)


# In[5]:


df.tail()


# In[6]:


df.info()


# In[7]:


df.columns = df.columns.str.strip("'")


# In[8]:


# !pip uninstall pandas
# !pip install pandas --upgrade


# In[9]:


df = df.apply(lambda x: x.str.strip("'") if x.dtype == np.dtype('object') else x)


# In[10]:


df.head()


# In[11]:


df.tail()


# In[12]:


df.info()


# In[13]:


df.isnull().sum()


# In[14]:


print('# 대여소 수')
print('대여 대여소: ', df['대여 대여소번호'].unique().shape[0])
print('반납 대여소: ', df['반납대여소번호'].unique().shape[0])


# In[15]:


df['대여 대여소명'].value_counts().head(10)


# In[16]:


df['반납대여소명'].value_counts().head(10)


# In[17]:


df['같은대여반납소'] = df['대여 대여소명'] == df['반납대여소명']
df['같은대여반납소']


# In[18]:


df_location_diff = df['같은대여반납소'].value_counts().reset_index()
df_location_diff.columns = ['일치여부', '대여반납수']
df_location_diff


# In[19]:


df_same_loc = df.loc[df['같은대여반납소'] == True]
df_same_loc.head()


# In[20]:


df_same_loc['대여 대여소명'].value_counts().head(10)


# In[21]:


bike_describe = df['자전거번호'].describe()
print('대여된 자전거 수 :', bike_describe[1])
print('가장 많이 대여된 자전거 번호 :', bike_describe[2])
print('가장 많이 대여된 자전거의 대여횟수 :', bike_describe[3])
bike_describe


# In[22]:


bike_rent_counts = df['자전거번호'].value_counts().reset_index()
bike_rent_counts.columns = ['자전거번호', '대여수']
print('해당 기간동안 자전거 하나당 평균 대여 수:', bike_rent_counts['대여수'].mean())
print('자전거 하나당 가장 많이 대여된 횟수:', bike_rent_counts['대여수'].max())
print('자전거 하나당 가장 적게 대여된 횟수:', bike_rent_counts['대여수'].min())


# In[ ]:




