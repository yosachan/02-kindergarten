#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[39]:


df_population_data = pd.read_csv('c01.csv', encoding='shift-jis')


# In[40]:


df_population_data


# In[8]:


type(df_population_data)


# In[10]:


pd.set_option('display.max_rows', 1000)


# In[11]:


df_population_data


# In[13]:


pd.reset_option('display.max_rows')


# In[14]:


df_population_data


# In[15]:


pd.set_option('display.max_columns', 5)


# In[16]:


df_population_data


# In[17]:


pd.reset_option('display.max_columns')


# In[18]:


df_population_data


# In[19]:


df_population_data.head(10)


# In[20]:


df_population_data.tail(10)


# In[21]:


df_population_data.sample(10)


# In[22]:


df_population_data.info()


# In[41]:


df_population_data.describe()


# In[32]:


df_population_data.describe().round(0)


# In[31]:


df_population_data.groupby(by='都道府県名').mean()[['人口（総数）', '人口（男）', '人口（女）']].round(0)
# 人口（総数）、人口（男）、人口（女）はキーではないので、エラーとなる。


# In[36]:


df_population_data.groupby(by='都道府県名').mean()[['人口（男）', '人口（女）']].round(0)


# In[35]:


df_population_data.groupby(by='都道府県名').mean()[['和暦（年）', '西暦（年）']].round(0)


# In[ ]:


df_population_mean = df_population_data.groupby(by='都道府県名').mean()[['人口（総数）', '人口（男）', '人口（女）']].round(0)


# In[ ]:


df_population_mean


# In[ ]:


df_population_mean.sort_values(by='都道府県名', ascending=False)


# In[44]:


left=pd.DataFrame({'name':['aaa', 'bbb', 'ccc', 'ddd'], 'age':[24, 33, 27, 42]})
right=pd.DataFrame({'name':['eee', 'bbb', 'aaa', 'fff', 'ddd'], 'group':['x', 'y', 'y', 'x', 'x']})


# In[45]:


left


# In[46]:


right


# In[47]:


pd.merge(left, right)


# In[48]:


pd.merge(left, right, how='outer')


# In[50]:


pd.concat([left, right])


# In[51]:


pd.concat([left, right], axis=1)


# In[52]:


import matplotlib
matplotlib.rcParams['font.family']='Arial Unicode MS'


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




