#!/usr/bin/env python
# coding: utf-8

# ## Lesson 3
# # Tabular Data Lesson
# This lesson covers how to analyze data in rows and columns.

# In[1]:


import numpy


# In[2]:


distance_file = 'data/distance_data_headers.csv'
print(distance_file)


# In[3]:


help(numpy.genfromtxt)


# In[4]:


distances = numpy.genfromtxt(fname= distance_file, delimiter=',', dtype = 'unicode')
# excluding the ',' from my csv file and adding the headings


# In[5]:


print(distances)


# In[6]:


#numbers in quotes are strings. We need to take two slices of this data: convert string into float. Headers remind string
headers = distances[0]
print(headers)


# In[7]:


# Take a slice of the distances array that is just the numbers. Call this data.
data = distances [1:]
print(data)


# In[8]:


data = data.astype(float)
print(data)


# In[9]:


# array_name[row, column]
point1 = data [0,1]
point2 = data [1,0]
print(point1)


# In[10]:


print(point2)


# In[11]:


print(F'The data points 1 and 2 are {point1} and {point2}, respectively')


# In[12]:


#subset of another array: new_array_name = old_array[start_row:end_row, start_columns:end_columns]
small_data = data[0:10, 0:3]
print(small_data)


# In[13]:


array1 = small_data[5,:] 
array2 = small_data[:, 1:] 
print(array1)
print(array2) 


# In[14]:


# ':' will cover all columns/rows. Only the 'number' will cover that index for the row/column. 


# In[15]:


thr4_atp = data[:,1]
print(thr4_atp)


# In[16]:


avg_thr4_atp = numpy.mean(thr4_atp)
print(avg_thr4_atp)


# In[17]:


print(F' {avg_thr4_atp:.4f}') 
# 4 decimals response


# In[18]:


print(F' The average distance over the simulation is {avg_thr4_atp:.4f} angstroms. ') 


# In[19]:


#Range-for loop
num_columns = len(headers)
print(num_columns)


# In[20]:


num_columns = len(data[1,:])
print(num_columns)


# In[21]:


for num in range(1, num_columns):
    data_column = data[:, num]
    avg_column = numpy.mean(data_column)
    print(F' {headers[num]} {avg_column: .4f}')


# In[22]:


# num will average all the values
# Easier path:
# axis 1---> horizontally , counts over columns
# axis 0 --> vertically, counts over rows


# In[23]:


averages = numpy.mean(data, axis=0)
print(averages)


# ## Plotting 
# Now we will learn how to create o=plot using matplotlib.

# In[24]:


import matplotlib.pyplot as plt 
# plt will load matplotli.pyplot


# In[25]:


plt.figure()  # creates a figure
plt.plot(data[:, 1])  # plot only with y values


# In[26]:


# to plot with X and Y, use plt.plot (x_values, y_values)
plt.figure()
plt.plot(data[:,0], data [:,1]) # x values are the frame number and y values are the same set of data from the previous plot


# In[27]:


small_data = data[0:1000:100, :] 
print(small_data)
# 0 to 1000 every 100 rows (interval)


# In[35]:


# labels and legends 
plt.figure()
plt.xlabel("Frame Number")
plt.ylabel("Distance (Anstrom)")
plt.plot(data[::100, 0], data[:: 100, 1], label =  headers[1])
plt.legend() #make the legend appear 
plt.savefig(F"{headers [1]}.png", dpi = 300)
#save the graph


# In[46]:


# plotting more than one set of data
plt.figure()
plt.xlabel("Frame")
plt.ylabel("Distance (Angstrom)")
plt.plot(data[::100, 0], data[::100, 1:], label=headers[1:])
plt.legend()
plt.savefig(F"All_data.png", dpi = 300)
#save the graph


# In[59]:


# Use a  for loop to create a plot for each column of data
for column in range(1, num_columns):
    plt.figure()
    plt.xlabel("Frame")
    plt.ylabel("Distance (\u212B)")
    plt.plot(data[::100, 0], data[:: 100, column], label =  headers[column], marker = "+",  color= "#00853E" )
    plt.legend()
    plt.savefig(F"{headers[column]}", dpi = 300)


# In[ ]:




