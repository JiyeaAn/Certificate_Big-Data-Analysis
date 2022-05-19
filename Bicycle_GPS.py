#!/usr/bin/env python
# coding: utf-8

# ## 1건만 돌린 경우

# In[1]:


# !pip install haversine


# In[2]:


import pandas as pd
df = pd.read_csv('./BicycleTracking_Pilot.csv', encoding='cp949')


# In[3]:


df


# In[4]:


lines = df[['위도', '경도']].values.tolist()
lines


# In[5]:


import folium
folium.__version__
from folium import plugins


# In[6]:


# 연남동 중앙점 기반 지도 로드
center = [37.561020, 126.923472]
m = folium.Map(location=center, zoom_start=15)


# In[11]:


my_PolyLine=folium.PolyLine(locations=lines,weight=5)
m.add_child(my_PolyLine)


# ## 여러 건을 돌린 경우

# In[12]:


import pandas as pd
df = pd.read_csv('./BicycleTracking_Pilot2.csv', encoding='cp949')


# In[30]:


df.head(10)


# In[28]:


lines = df[['위도', '경도']].values.tolist()
lines


# In[15]:


import folium
folium.__version__
from folium import plugins


# In[16]:


# 연남동 중앙점 기반 지도 로드
center = [37.561020, 126.923472]
m = folium.Map(location=center, zoom_start=15)


# In[17]:


my_PolyLine=folium.PolyLine(locations=lines,weight=5)
m.add_child(my_PolyLine)

