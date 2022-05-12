#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
from plotnine import *


# In[6]:


df = pd.read_csv(r'C:\Users\dkswl\Desktop\공공자전거 따릉이\서울 마포구 공공자전거 대여 현황_2007_2012.CSV', 
                 encoding='cp949')
df.shape


# In[7]:


df.head(10)


# In[8]:


df.tail()


# In[9]:


df.info()


# In[10]:


df.columns = df.columns.str.strip("'")


# In[11]:


df = df.apply(lambda x: x.str.strip("'") if x.dtype == np.dtype('object') else x)


# In[12]:


df.head()


# In[13]:


df.tail()


# In[14]:


df.info()


# In[15]:


df.isnull().sum()


# In[22]:


print('# 대여소 수')
print('대여 대여소: ', df['대여 대여소번호'].unique().shape[0])
print('반납 대여소: ', df['반납대여소번호'].unique().shape[0])


# In[23]:


df['대여 대여소명'].value_counts().head(10)


# In[24]:


df['반납대여소명'].value_counts().head(10)


# In[26]:


df['같은대여반납소'] = df['대여 대여소명'] == df['반납대여소명']
df['같은대여반납소']


# In[29]:


df_location_diff = df['같은대여반납소'].value_counts().reset_index()
df_location_diff.columns = ['일치여부', '대여반납수']
df_location_diff


# In[33]:


df_same_loc = df.loc[df['같은대여반납소'] == True]
df_same_loc.head()


# In[36]:


df_same_loc['대여 대여소명'].value_counts().head(10)


# In[37]:


bike_describe = df['자전거번호'].describe()
print('대여된 자전거 수 :', bike_describe[1])
print('가장 많이 대여된 자전거 번호 :', bike_describe[2])
print('가장 많이 대여된 자전거의 대여횟수 :', bike_describe[3])
bike_describe


# In[38]:


bike_rent_counts = df['자전거번호'].value_counts().reset_index()
bike_rent_counts.columns = ['자전거번호', '대여수']
print('해당 기간동안 자전거 하나당 평균 대여 수:', bike_rent_counts['대여수'].mean())
print('자전거 하나당 가장 많이 대여된 횟수:', bike_rent_counts['대여수'].max())
print('자전거 하나당 가장 적게 대여된 횟수:', bike_rent_counts['대여수'].min())


# In[ ]:





# In[ ]:





# In[ ]:




