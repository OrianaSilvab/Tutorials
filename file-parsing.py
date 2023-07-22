#!/usr/bin/env python
# coding: utf-8

# ## File Parsing Lesson
# File parsing is looking through a big file of information for one particular fact.

# In[1]:


ethanol_file = 'data/outfiles/ethanol.out'
print(ethanol_file)


# In[2]:


outfile = open(ethanol_file,  'r' )
# every element of the ethanol file will be part of the list
data = outfile.readlines()
outfile.close()


# In[3]:


pwd


# In[4]:


print(data[12])


# In[5]:


length_file = len(data)
print(length_file)


# In[6]:


for line in data:
    if 'Final Energy' in line: 
        energy_line = line
print(energy_line)
type(energy_line)


# In[7]:


split_line = energy_line.split()
print(split_line)


# In[8]:


energy = split_line[3]
print(energy)
# This is the final energy separated as an idividual character
# third spot in the line; therefore, '3'


# In[9]:


type(energy)


# In[10]:


# since it was in quotes it is a string
energy = float(energy)


# In[11]:


type(energy)


# In[12]:


# float = decimal number vs. string= it is just characters


# In[13]:


import glob 


# In[14]:


file_location = 'data/outfiles/*.out'
print(file_location)


# In[15]:


# To use a function from a Library, library_name.function_name
# a library is a group of functions
filenames = glob.glob(file_location)
print(filenames)


# In[16]:


for file in filenames : 
    outfile = open(file, 'r')
    data = outfile.readlines()
    outfile.close()
    for line in data :
        if 'Final Energy' in line : 
            energy_line = line
            split_line = energy_line.split()
            energy = float(split_line[3])
            print(energy)


# In[17]:


first_file = filenames [0] 
print(first_file)


# In[18]:


split_filename = first_file.split('/')
print(split_filename)


# In[19]:


# Do additional parsing, to ultimately pull out just the molecule name 
# Save this in a variable called molecule_name
name = split_filename[2].split('.')
print(name)


# In[20]:


molname = name[0]
print(molname)


# In[21]:


for file in filenames : 
    first_file = file 
    split_filename = first_file.split('/')
    # print(split_filename)
    name = split_filename[2].split('.')
    # print(name)
    molname = name[0]
    # print(molname)
    outfile = open(file, 'r')
    data = outfile.readlines()
    outfile.close()
    for line in data :
        if 'Final Energy' in line : 
            energy_line = line
            split_line = energy_line.split()
            energy = float(split_line[3])
            print(molname, energy)


# In[22]:


datafile = open( 'energy.txt' , 'w+' )
for file in filenames : 
    first_file = file 
    split_filename = first_file.split('/')
    # print(split_filename)
    name = split_filename[2].split('.')
    # print(name)
    molname = name[0]
    # print(molname)
    outfile = open(file, 'r')
    data = outfile.readlines()
    outfile.close()
    for line in data :
        if 'Final Energy' in line : 
            energy_line = line
            split_line = energy_line.split()
            energy = float(split_line[3])
            datafile.write(F' {molname},  {energy: .3F}. \n' )
datafile.close()


# In[ ]:




