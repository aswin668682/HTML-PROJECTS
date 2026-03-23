#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\aswin\OneDrive\Documents\loan_default_prediction.csv")
print(df.head())
print(df.info())


# In[18]:


print(df.isnull().sum())


# In[19]:


print(df.duplicated().sum())


# In[20]:


df = df.drop_duplicates()


# In[21]:


df['income'] = df['income'].astype(int)
df['loan_amount'] = df['loan_amount'].astype(int)
df['default'] = df['default'].astype(int)


# In[22]:


df['employment_status'] = df['employment_status'].map({
    'Employed': 1,
    'Unemployed': 0
})


# In[23]:


df['loan_income_ratio'] = df['loan_amount'] / df['income']


# In[24]:


print(df.describe())


# In[25]:


high_risk = df[df['loan_income_ratio'] > 3]
print(high_risk.head())


# In[26]:


plt.hist(df['income'])
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()


# In[27]:


plt.scatter(df['income'], df['loan_amount'])
plt.xlabel("Income")
plt.ylabel("Loan Amount")
plt.title("Income vs Loan Amount")
plt.show()


# In[28]:


df['default'].value_counts().plot(kind='bar')
plt.title("Default vs Non-Default")
plt.show()


# In[ ]:




