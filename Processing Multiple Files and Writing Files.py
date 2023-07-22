#!/usr/bin/env python
# coding: utf-8

# # Processing Multiple Files and Writing Files

# In[19]:


# The star is the wildcard character. It will select all the files ending in '.out'
import glob
file_location = os.path.join('data', 'outfiles', '*.out')
print(file_location)


# In[20]:


#library name + function name
filenames = glob.glob(file_location)
print(filenames)


# In[22]:


#Double loop to extract Final Energy from all my files
for file in filenames :
    outfile = open(file, 'r')
    data = outfile.readlines()
    outfile.close()
    for line in data :
        if 'Final Energy' in line :
            energy_line = line
            words = energy_line.split()
            energy = float(words[3])
            print(energy)


# In[23]:


first_file = filenames[0]
print(first_file)


# In[24]:


file_name = os.path.basename(first_file)
print(file_name)


# In[28]:


split_filename = file_name.split('.')
print(split_filename)


# In[29]:


molecule_name = split_filename[0]
print(molecule_name)


# In[30]:


for file in filenames :
    file_name = os.path.basename(file)
    split_filename = file_name.split('.')
    molecule_name = split_filename[0]
    outfile = open(file, 'r')
    data = outfile.readlines()
    outfile.close()
    for line in data :
        if 'Final Energy' in line :
            energy_line = line
            words = energy_line.split()
            energy = float(words[3])
            print( molecule_name, energy)


# In[34]:


filehandle = open('Energy.txt', 'w+')
#W is for writing and the + if it does not exist, we will make the file
for file in filenames :
    file_name = os.path.basename(file)
    split_filename = file_name.split('.')
    molecule_name = split_filename[0]
    outfile = open(file, 'r')
    data = outfile.readlines()
    outfile.close()
    for line in data :
        if 'Final Energy' in line :
            energy_line = line
            words = energy_line.split()
            energy = float(words[3])
            filehandle.write(F' For the molecule {molecule_name} the energy is \t {energy: .4f}\n')
filehandle.close()

# F-String printing



# In[ ]:




