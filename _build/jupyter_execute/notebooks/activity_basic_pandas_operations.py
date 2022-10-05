#!/usr/bin/env python
# coding: utf-8

# # Basic Pandas Operations
# 
# ## Why do we use Pandas?
# 
# Pandas is a powerful Python library that supports creation, storage, and manipulation of data frames. As a psychologist or data scientist, you will inevitably deal with some kind of datasets. Pandas stores and represents data in a streamlined fashion that makes things simple for you - either you are planning on directly analyzing the data in Python or exporting the data to CSV files and analyze them in other statistical softwares such as R.
# 
# It also has other advantages such as simplifying coding writing, handling large data more efficiently, and making data more flexible and customizable. More importantly, Pandas has features such as handling missing data, cleaning up the data, and it also supports multiple file formats including CSV, Excel, SQL, etc.
# 
# In this activity, we will learn some of the basic oprations to get you started with Pandas.
# 
# ## Storing data frames in a CSV file
# 
# First we will create a dictionary containing the data. Then we can convert the dictionary to a pandas data frame and store it as a csv file.

# In[2]:


import numpy as np
import pandas as pd

name_dict = {
    'Name':['Adam','Becky','Charlie','Daniel','Emily','Frank','Greta','Helen','Ian','Jack','Klaus','Lucy'],
    'Class ID':list(range(1,13)),
    'Age':[int(i) for i in (np.round(np.random.uniform(18,30,12),0))],
    'Score':[int(i) for i in (np.round(np.random.uniform(60,100,12),0))]
}

df = pd.DataFrame(name_dict)

df.to_csv('ClassList.csv',index=False)


# ## Loading in data from a CSV file
# 
# After loading in the data, we can do some quick checks using `head()` and `tail()`

# In[3]:


df = pd.read_csv('ClassList.csv')
df.head() # This will give you the first 5 rows of data


# In[4]:


df.tail() # This will give you the last 5 rows of data


# ## Accessing a particular row, column, or cell
# 
# In some cases, we want to access a particular row of the data.

# In[5]:


df.loc[0,:] # Accessing the first row of data, the first value points to the row(s) and the second value points to the column(s)


# We can select a particular column by its name

# In[6]:


df.Score # Accessing the Score column


# Or you can select a column by its index

# In[8]:


df.iloc[:,2] # This will also access the Score column


# It's also possible to select a particular cell

# In[9]:


df.iloc[0]['Score'] # This will access the first row ([0]) of the Score column


# ## Iterate through rows and accessing a particular column of that row
# 
# In some cases, we need to iterate through all the rows and do some computation with a particular column of that row

# In[10]:


# Printing everything of each row
for row in df.iterrows():
    print(row)


# In[11]:


# Iterate through all rows and select only the Score column
for index,row in df.iterrows():
    print(row['Score'])

