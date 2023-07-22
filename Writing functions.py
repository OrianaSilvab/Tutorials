#!/usr/bin/env python
# coding: utf-8

# ## Writing Functions

# In[23]:


##def function_name(parameters):
   ## ** function body code **
 ##   return value_to_return


# In[24]:


import numpy
import os

file_location = os.path.join('data', 'water.xyz')
xyz_file = numpy.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
symbols = xyz_file[:, 0]
coordinates = xyz_file[:, 1:]
coordinates = coordinates.astype(numpy.float)
num_atoms = len(symbols)
for num1 in range(0, num_atoms):
    for num2 in range(0, num_atoms):
        if num1 < num2:
            x_distance = coordinates[num1, 0] - coordinates[num2, 0]
            y_distance = coordinates[num1, 1] - coordinates[num2, 1]
            z_distance = coordinates[num1, 2] - coordinates[num2, 2]
            bond_length_12 = numpy.sqrt(x_distance ** 2 + y_distance ** 2 + z_distance ** 2)
            if bond_length_12 > 0 and bond_length_12 <= 1.5:
                print(F'{symbols[num1]} to {symbols[num2]} : {bond_length_12:.3f}')


# In[25]:


def calculate_distance(atom1_coord, atom2_coord):
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    bond_length_12 = numpy.sqrt(x_distance ** 2 + y_distance ** 2 + z_distance ** 2)
    return bond_length_12


# In[26]:


for num1 in range(0, num_atoms):
    for num2 in range(0, num_atoms):
        if num1 < num2:
            bond_length_12 = calculate_distance(coordinates[num1], coordinates[num2])
            if bond_length_12 > 0 and bond_length_12 <= 1.5:
                print(F'{symbols[num1]} to {symbols[num2]} : {bond_length_12:.3f}')


# In[27]:


def bond_check(atom_distance):
    if atom_distance > 0 and atom_distance <= 1.5:
        return True
    else:
        return False


# In[28]:


# Modify the bond_check function to take a minimum length and a maximum length as user input.
def bond_check(atom_distance, minimum_length, maximum_length):
   if atom_distance > minimum_length and atom_distance <= maximum_length:
       return True
   else:
       return False


# In[29]:


help(numpy.genfromtxt)


# In[30]:


def calculate_distance(atom1_coord, atom2_coord):
    """Calculate the distance between two three-dimensional points."""

    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    bond_length_12 = numpy.sqrt(x_distance**2+y_distance**2+z_distance**2)
    return bond_length_12


# In[31]:


def bond_check(atom_distance, minimum_length=0, maximum_length=1.5):
    """
    Check if a distance is a bond based on a minimum and maximum bond length.
    """

    if atom_distance > minimum_length and atom_distance <= maximum_length:
        return True
    else:
        return False


# In[32]:


print(bond_check(1.5))
print(bond_check(1.6))


# In[33]:


print(bond_check(1.6, maximum_length=1.6))


# In[34]:


num_atoms = len(symbols)
for num1 in range(0, num_atoms):
    for num2 in range(0, num_atoms):
        if num1 < num2:
            bond_length_12 = calculate_distance(coordinates[num1], coordinates[num2])
            if bond_check(bond_length_12) is True:
                print(F'{symbols[num1]} to {symbols[num2]} : {bond_length_12:.3f}')


# In[35]:


## We might also want to write a function that opens and processes our xyz file for us. Write a function called open_xyz which takes an xyz file as a parameter and returns the symbols and coordinates.

##Hint: You can return two values from a function by typing return variable1, variable2.

def open_xyz(filename):
     xyz_file = numpy.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
     symbols = xyz_file[:, 0]
     coord = (xyz_file[:, 1:])
     coord = coord.astype(numpy.float)
     return symbols, coord


# In[36]:


import numpy
import os

file_location = os.path.join('data', 'water.xyz')
symbols, coord = open_xyz(file_location)
num_atoms = len(symbols)
for num1 in range(0, num_atoms):
    for num2 in range(0, num_atoms):
        if num1 < num2:
            bond_length_12 = calculate_distance(coord[num1], coord[num2])
            if bond_check(bond_length_12) is True:
                print(F'{symbols[num1]} to {symbols[num2]} : {bond_length_12:.3f}')


# In[37]:


def print_bonds(atom_symbols, atom_coordinates):
    num_atoms = len(atom_symbols)
    for num1 in range(0, num_atoms):
        for num2 in range(0, num_atoms):
            if num1 < num2:
                bond_length_12 = calculate_distance(atom_coordinates[num1], atom_coordinates[num2])
                if bond_check(bond_length_12) is True:
                    print(F'{atom_symbols[num1]} to {atom_symbols[num2]} : {bond_length_12:.3f}')


# In[38]:


import numpy
import os

def calculate_distance(atom1_coord, atom2_coord):
    """
    Calculate the distance between two three-dimensional points.
    """
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    bond_length_12 = numpy.sqrt(x_distance ** 2 + y_distance ** 2 + z_distance ** 2)
    return bond_length_12

def bond_check(atom_distance, minimum_length=0, maximum_length=1.5):
    """Check if a distance is a bond based on a minimum and maximum bond length"""

    if atom_distance > minimum_length and atom_distance <= maximum_length:
        return True
    else:
        return False

def open_xyz(filename):
     """
     Open and read an xyz file. Returns tuple of symbols and coordinates.
     """
     xyz_file = numpy.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
     symbols = xyz_file[:,0]
     coord = (xyz_file[:,1:])
     coord = coord.astype(numpy.float)
     return symbols, coord

def print_bonds(atom_symbols, atom_coordinates):
    """
    Prints atom symbols and bond length for a set of atoms.
    """
    num_atoms = len(atom_symbols)
    for num1 in range(0, num_atoms):
        for num2 in range(0, num_atoms):
            if num1 < num2:
                bond_length_12 = calculate_distance(atom_coordinates[num1], atom_coordinates[num2])
                if bond_check(bond_length_12) is True:
                    print(F'{atom_symbols[num1]} to {atom_symbols[num2]} : {bond_length_12:.3f}')


# In[39]:


water_file_location = os.path.join('data', 'water.xyz')
water_symbols, water_coords = open_xyz(water_file_location)

benzene_file_location = os.path.join('data', 'benzene.xyz')
benzene_symbols, benzene_coords = open_xyz(benzene_file_location)

print(F'Printing bonds for water.')
print_bonds(water_symbols, water_coords)

print(F'Printing bonds for benzene.')
print_bonds(benzene_symbols, benzene_coords)


# In[40]:


## In earlier lessons, we used glob to process multiple files. How could you use glob to print bonds for all the xyz files?
import glob

xyz_files = glob.glob("data/*.xyz")

for xyz_file in xyz_files:
    atom_symbols, atom_coords = open_xyz(xyz_file)
    print("Printing bonds for ", xyz_file)
    print_bonds(atom_symbols, atom_coords)

