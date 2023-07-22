#!/usr/bin/env python
# coding: utf-8

# # Geometry Analysis Project
# ## Water XYZ

# In[5]:


import numpy


# In[6]:


distance_file = 'data/water.xyz'
print(distance_file)
outfile = open(distance_file,  'r' )
# every element of the water file will be part of the list
data = outfile.readlines()
outfile.close()
print(data)


# In[7]:


elements = data[2:]
print(elements)


# In[8]:


type(elements)


# In[9]:


data2 = []
for line in elements:  
    print(line)
    split_line = line.split()
    print(split_line)
    data2.append(split_line)
data2 = numpy.array(data2)
print(data2)
type(data2)


# In[10]:


headers = data2[:,0]
print(headers)


# In[11]:


values = data2[:,1:]
print(values)


# In[14]:


numbers = values.astype(float)
print(numbers)
type(values)
num_columns = len(values[1])
print(num_columns)


# In[15]:


for num in range (0, num_columns) :
    for num2 in range(0, num_columns):
        x = numbers[ num, 0] - numbers[ num2, 0]
        y = numbers[ num, 1] - numbers[ num2, 1]
        z = numbers[ num, 2] - numbers[ num2, 2]
        d = numpy.sqrt(x**2+y**2+z**2)
        print(F' {headers[num]} to {headers[num2]} : {d: .3f}')
   
    

