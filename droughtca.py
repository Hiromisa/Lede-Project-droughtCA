#!/usr/bin/env python
# coding: utf-8

# In[69]:


import pandas as pd


# In[70]:


df = pd.read_csv("droughtCAnow.csv")
df.head()


# In[71]:


df.shape


# In[72]:


df.columns


# In[73]:


df.dtypes


# In[74]:


df.describe()


# In[76]:


df['E'] = df['D3'] + df['D4']
df.tail()


# In[77]:


df.sort_values(by = 'E', ascending= False)
df.head()


# In[79]:


round(df.E.value_counts( normalize= True)*100, 1)


# In[80]:


df[df.E == 0.00]


# In[81]:


df.E.mean()


# In[84]:


df[df.D4 == 100.00]


# In[85]:


df[(df.E == 100.00) & (df.D4 != 100.00)].shape


# In[86]:


worst_df = df.sort_values(by='D4', ascending= False)
worst = worst_df.head(10)


# In[87]:


worst.head(10)


# In[88]:


worst.to_csv('worst10.csv')


# In[89]:


df.D4.mean()


# In[90]:


df.value_counts(df['D4'] > 0.0, normalize= True)*100


# In[91]:


df['None'].value_counts()


# In[92]:


df['D0'].value_counts()


# In[93]:


new_df = df.drop(columns = ['State','None','ValidStart','ValidEnd','StatisticFormatID','MapDate','D0','D1','D2','D3','D4']) 


# In[94]:


new_df.tail()


# In[95]:


new_df.to_csv('fdrought.csv')


# In[96]:


cadf = pd.read_csv("ca.csv")
cadf.head()


# In[97]:


cadf.shape


# In[98]:


cadf['other'] = cadf['None'] + cadf['D0']
cadf.tail()


# In[99]:


cadf.columns


# In[100]:


ncadf = cadf.rename(columns={'D1':'Moderate', 'D2': 'Severe', 'D3':'Extreme', 'D4':'Exceptional'})


# In[103]:


new_cadf = ncadf.drop(columns = ['StateAbbreviation', 'None', 'D0', 'ValidStart', 'ValidEnd', 'StatisticFormatID']) 


# In[104]:


new_cadf.head()


# In[105]:


new_cadf.to_csv('fca.csv')


# In[ ]:




