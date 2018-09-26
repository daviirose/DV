
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from matplotlib import pyplot as plt


# In[14]:


data = pd.read_csv('countries.csv')


# In[15]:


data


# In[35]:


# Compare the population growth in the US and China


# In[39]:


data[data.country == 'United States']


# In[36]:


us = data[data.country == 'United States']


# In[40]:


china = data[data.country == 'China']


# In[41]:


china


# In[42]:


plt.plot(us.year, us.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population')
plt.show()


# In[43]:


us.population


# In[45]:


us.population / us.population.iloc[0] * 100


# In[46]:


plt.plot(us.year,us.population / us.population.iloc[0] * 100)
plt.plot(china.year, china.population / china.population.iloc[0] * 100)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population growth (first year = 100)')
plt.show()

