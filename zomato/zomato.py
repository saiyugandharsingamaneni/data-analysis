#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv('zomato.csv', encoding='latin-1')
df.head()


# In[3]:


df.tail()


# In[4]:


df.shape


# In[5]:


df.columns


# In[6]:


df.duplicated().sum()


# In[7]:


df=df.drop_duplicates()


# In[8]:


df.info()


# In[36]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[32]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(12,6)
sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[9]:


df.describe()


# In[10]:


df.nunique()


# In[11]:


df_country=pd.read_excel("Country-code.xlsx")
df_country


# In[12]:


final_df=pd.merge(df,df_country,on='Country Code')
final_df


# In[13]:


final_df.dtypes


# In[14]:


country_names=final_df.Country.value_counts().index
country_names


# In[15]:


country_values=final_df.Country.value_counts().values
country_values


# In[16]:


plt.figure(figsize=(9,9))
plt.pie(country_values[:3],labels=country_names[:3],autopct='%.2f%%')


# In[17]:


final_df.columns


# In[24]:


rating=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating count'})
rating.head()


# In[19]:


final_df.head()


# In[20]:


Table_booking=final_df.groupby(['Has Table booking','Country']).size().reset_index().rename(columns={0:'orders_per_country'})
Table_booking.head()


# In[21]:


Online_booking=final_df.groupby(['Has Online delivery','Country']).size().reset_index().rename(columns={0:'orders_per_country'})
Online_booking.head()


# In[22]:


total_table_booking=final_df[final_df['Has Table booking']=='Yes'].Country.value_counts()
total_table_booking


# In[23]:


total_online_bookings=final_df[final_df['Has Online delivery']=='Yes'].Country.value_counts()
total_online_bookings


# In[29]:


plt.figure(figsize=(12,6))
sns.barplot(x='Aggregate rating',y='Rating count',data=rating)


# In[39]:


sns.barplot(x='Aggregate rating',y='Rating count',data=rating,hue='Rating color',palette=['gray','red','yellow','green','orange','violet','blue'])


# ### Observation:
# 
# 1.Not Rated count is very high
# 
# 2.Maximum number of rating are between 2.5 to 3.4

# In[42]:


sns.countplot(x="Rating color",data=rating)


# In[43]:


rating


# In[51]:


### Find the countries name that has given 0 rating 
Zero_rating=final_df[final_df["Rating color"]=="White"].groupby("Country").size().reset_index().rename(columns={0:'count_zeros'})


# In[52]:


Zero_rating


# ## Observation
# #### maximum zero rating given in india

# In[64]:


#find out currency used by country
currency=final_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()
currency


# In[71]:


#which country have online delivery option

online_delivery=final_df[['Country','Has Online delivery']].groupby(['Country','Has Online delivery']).size().reset_index()
online_delivery


# In[93]:


#city having more orders
city_values=final_df.City.value_counts().values
city_values


# In[94]:


city_index=final_df.City.value_counts().index
city_index


# In[95]:


plt.pie(city_values[:5],labels=city_index[:5])


# In[98]:


final_df.head()


# In[105]:


#Top 10 cuisines
cuisines=final_df.Cuisines.value_counts()
cuisines.head(10)


# In[ ]:




