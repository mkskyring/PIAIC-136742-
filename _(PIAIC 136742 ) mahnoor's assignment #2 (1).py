#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[15]:


import numpy as np
#here we arranged the value and reshaped it into two rows and 5 columns
np.arange(0,10).reshape(2,5)


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[4]:


## first importing numpy .
import numpy as np


# In[8]:


## here we have two arrays : arry1 ,arry2 
arry1 = np.arange(0,10).reshape(2,5)
arry2 = np.ones(10).reshape(2,5).astype('int32')
## to get desired output we use vstack function : 
np.vstack((arry1,arry2))


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[41]:


arrystack=np.hstack((arry1,arry2))
##here stacking horixontally by using 'hstack'
arrystack


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[49]:


import numpy as np
arry3=[0,1,2,3,4]
arry4=[5,6,7,8,9]
arr=np.vstack((arry3,arry4))
#now flattening the array into 1d array :
arr.flatten()


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[67]:


arry5= np.arange(0,15).reshape(3,5)
print(arry5)
arry5.flatten()


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[68]:


arry6 = np.arange(0,15).reshape(5,3)
arry6


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[71]:


arry7 = np.arange(50,75).reshape(5,5)
np.square(arry7)


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[72]:


arry8 = np.arange(30,60).reshape(5,6)
np.mean(arry8)


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[73]:


np.std(arry8)


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[74]:


np.median(arry8)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[75]:


arry8.T


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[4]:


import numpy as np
arry9 = np.arange(2,18).reshape(4,4)
print(arry9)
np.trace(arry9)


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[5]:


np.linalg.det(arry9)


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[6]:


print(np.percentile(arry9,5))
np.percentile(arry9,95)


# ## Question:15

# ### How to find if a given array has any null values?

# In[8]:


import numpy as np
np.isnan(np.min(arry9))

