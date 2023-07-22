#!/usr/bin/env python
# coding: utf-8

# # MolSSI Workshop
# ## Introduction Lesson
# This is the introductory lesson to the MolSSI python workshop.

# In[1]:


7+3


# In[2]:


deltaH = -541.5
deltaS = 10.4
temperature = 298 
deltaG = deltaH - temperature*deltaS


# In[3]:


print(deltaG)


# print is a mechanism that will operate the actual function.

# In[4]:


type(deltaG)


# Float is a data point that is has decimals. Int is an integer.

# In[5]:


deltaG + 50 


# In[6]:


deltaG_string = str(deltaG)


# In[7]:


print(deltaG_string)


# In[8]:


deltaG_string + 50 


# In[9]:


type(deltaG_string)


# String is something that is just characters, that is why we cannot do operations. 

# In[10]:


sentence = 'this is a string'


# In[11]:


print (sentence)


# In[12]:


#  this is how you set up a list data structure
energy_kcal  = [ -13.4,  -2.7,  5.4,  42.1]


# In[13]:


print(energy_kcal)


# In[14]:


# type the list name : list_name[index] 
# Python you always start counting at 0. The first negative number belongs to 0 (-13.4 = index 0). 


# In[15]:


print(energy_kcal[1])


# In[16]:


len(energy_kcal)


# In[17]:


length_list = len(energy_kcal)
print(length_list)


# This is how to find the length of the list and to create a function with it.

# In[18]:


print(F'The length of my list is length_list')


# In[19]:


print(F'The length of my list is {length_list}. ')


# In[20]:


# Taking a slice - when you make a list that is a subset of another list. 
# new_list = old_list [start:end]
# It is going to start from 0 up to 2 (excluding 2)
short_list = energy_kcal[0:2] 
print(short_list)


# In[21]:


short_list = energy_kcal[:2] 
print(short_list)


# In[22]:


slice1 = energy_kcal[1:]
slice2 = energy_kcal[:3] 


# In[23]:


print(F'slice 2 is {slice2}. ')


# In[24]:


print(F' slice 1 is, {slice1}. ')


# In[25]:


print(energy_kcal)


# In[26]:


print(energy_kcal[2])


# In[27]:


energy_kcal[2]*4.184


# In[28]:


#need a colon to create indentation
for number in energy_kcal : 
    kj = number * 4.184
    print(kj)


# In[30]:


#make a  new list with the kj values (get rid of the indent before printing)
energy_kj = []
for number in energy_kcal :
    kj = number * 4.184
    energy_kj.append(kj)
print(energy_kj)


# In[32]:


negative_energy = []
for number in energy_kcal : 
    if number < 0 :
        negative_energy.append(number)
print(negative_energy)


# In[ ]:




