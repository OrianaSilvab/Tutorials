#!/usr/bin/env python
# coding: utf-8

# ## File Parsing Lesson 2
# File parsing is looking through a big file of information for one particular fact.

# In[1]:


#ethanol_file = '/home/jovyan/work/python-data-and-scripting/data/outfiles/ethanol.out'
ethanol_file = 'data/outfiles/ethanol.out'
print(ethanol_file)


# In[2]:


outfile = open(ethanol_file,  'r' )
# every element of the ethanol file will be part of the list
data = outfile.readlines()
outfile.close()


# In[3]:


import os


# In[4]:


os.getcwd()


# In[5]:


os.listdir('data/outfiles')


# In[ ]:





# In[ ]:




