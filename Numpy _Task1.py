#!/usr/bin/env python
# coding: utf-8

# # Reading Recipes 
# 
# Note: Data file is recipes.csv Attached with jupyter notebook
1. Start by importing NumPy as np
# In[3]:


#type your code here
import numpy as np


# 2. All of Alize’s recipes call for milk, eggs, sugar, flour, and butter. For example, her cupcake recipe calls for:
# 
# Flour Sugar Eggs Milk Butter 2 cups 0.75 cups 2 eggs 1 cups 0.5 cups Create a NumPy array that represents this data. Each element should be a number (i.e., 2 for “2 cups”). Save this array as cupcakes.

# In[4]:


#type your code here 
##creating array for ingrediants of cupcakes :
import numpy as np
cupcakes = np.array([2, 0.75, 2, 1, 0.5])
cupcakes


# 3. Alize’s assistant has compiled all of her recipes into a csv (comma-separated variable) file called recipes.csv. Load this file into a variable called recipes.
# 
# ###########Explore yourselves how to load a csv file in numpy#######

# In[6]:


#type your code here

import pandas as pd
recipes = pd.read_table('recipes.csv', sep=',',header=None)   


# 4.Display recipes using print.
# Display recipes using print.
# 
# 
# Each row represents a different recipe. Each column represents a different ingredient.
# 
# Recipe	       Cups of Flour	Cups of Sugar	Eggs	Cups of Milk	Cups of Butter
# 
# Cupcakes	         …	              …	          …	         …	              …
# 
# Pancake	             …                …	          …	         …	              …
# 
# Cookie	             …	              …	          …	         …	              …
# 
# Bread	             …	              …	          …	         …	              …

# In[7]:


#type your code here
recipes


# 5.The 3rd column represents the number of eggs that each recipe needs.
# 
# Select all elements from the 3rd column and save them to the variable eggs.

# In[8]:


#type your code here
## here eacheggs contains al elements of 3rd coloumn :
eggs= recipes[recipes.columns[2]]


# 6.Which recipes require exactly 1 egg? Use a logical statement to get True or False for each value of eggs.

# In[9]:


eggs == 1


# 7.Alize is going to make 2 batches of cupcakes (1st row) and 1 batch of cookies (3rd row).
# 
# You already have a variable for cupcakes. Create a variable for cookies with the data from the 3rd row.
# 

# In[17]:


#type your code here
## here we have variable cookies !
cookies = recipes[2:3]
cookies


# 8.
# Get the number of ingredients for a double batch of cupcakes by using multiplication on cupcakes. Save your new variable to double_batch.

# In[20]:


#type your code here
## for doubling cupcakes we use function 'multiply' :
double_batch = np.multiply(cupcakes, cupcakes)
double_batch


# 9.
# Create a new variable called grocery_list by adding cookies and double_batch.

# In[22]:


#type your code here
## for adding we simply perform addition !
grocery_list = cookies + double_batch
grocery_list


# In[ ]:




