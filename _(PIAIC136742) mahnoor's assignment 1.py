#!/usr/bin/env python
# coding: utf-8

# # **Assignment For Numpy**

# Difficulty Level **Beginner**

# 1. Import the numpy package under the name np

# In[1]:


import numpy as np


# 2. Create a null vector of size 10 

# In[2]:


np.zeros(10)


# 3. Create a vector with values ranging from 10 to 49

# In[2]:


import numpy as np
vec2r = np.arange(10,49)


# 4. Find the shape of previous array in question 3

# In[3]:


vec2r.shape


# 5. Print the type of the previous array in question 3

# In[4]:


print(vec2r.dtype)


# 6. Print the numpy version and the configuration
# 

# In[7]:


print(np.__version__)
print(np.show_config())


# 7. Print the dimension of the array in question 3
# 

# In[5]:


vec2r.ndim


# 8. Create a boolean array with all the True values

# In[7]:


np.ones((15), dtype=bool)


# 9. Create a two dimensional array
# 
# 
# 

# In[9]:


np.ones((4, 4))


# 10. Create a three dimensional array
# 
# 

# In[10]:


np.ones((2,5,2))


# Difficulty Level **Easy**

# 11. Reverse a vector (first element becomes last)

# In[11]:


vec2r[::-1]


# 12. Create a null vector of size 10 but the fifth value which is 1 

# In[19]:


v=np.zeros(10)
v[4]=1
v


# In[22]:


v_id= np.identity(4)
v_id


# 13. Create a 3x3 identity matrix

# In[23]:


v_id= np.identity(3)
v_id


# 14. arr = np.array([1, 2, 3, 4, 5]) 
# 
# ---
# 
#  Convert the data type of the given array from int to float 

# In[26]:


arr = np.array([1, 2, 3, 4, 5])
arr.astype('float32')


# 15. arr1 =          np.array([[1., 2., 3.],
# 
#                     [4., 5., 6.]])  
#                       
#     arr2 = np.array([[0., 4., 1.],
#      
#                    [7., 2., 12.]])
# 
# ---
# 
# 
# Multiply arr1 with arr2
# 

# In[27]:


arr1 = np.array([[1., 2., 3.],

            [4., 5., 6.]])  
arr2 = np.array([[0., 4., 1.],

           [7., 2., 12.]])
np.multiply(arr1,arr2)


# 16. arr1 = np.array([[1., 2., 3.],
#                     [4., 5., 6.]]) 
#                     
#     arr2 = np.array([[0., 4., 1.], 
#                     [7., 2., 12.]])
# 
# 
# ---
# 
# Make an array by comparing both the arrays provided above

# In[60]:


result_compr= arr1==arr2
result_compr


# 17. Extract all odd numbers from arr with values(0-9)

# In[32]:


arr = np.arange(2,13)
print(arr)
arr_odd = arr[arr%2 != 0]
arr_odd


# 18. Replace all odd numbers to -1 from previous array

# In[72]:


arr[arr%2 != 0] = -1
arr


# 19. arr = np.arange(10)
# 
# 
# ---
# 
# Replace the values of indexes 5,6,7 and 8 to **12**

# In[73]:


arr[5:9]=12
arr


# 20. Create a 2d array with 1 on the border and 0 inside

# In[104]:


arr_2d = np.zeros(9).reshape(3,3)
arr_2d[0:1,]=1
arr_2d[:,0]=1
arr_2d[:,-1]=1
arr_2d[-1,]=1
print(arr_2d)


# Difficulty Level **Medium**

# 21. arr2d = np.array([[1, 2, 3],
# 
#                     [4, 5, 6], 
# 
#                     [7, 8, 9]])
# 
# ---
# 
# Replace the value 5 to 12

# In[109]:


arr2d = np.array([[1, 2, 3],

            [4, 5, 6], 

            [7, 8, 9]])
arr2d[1,1]=12
arr2d


# 22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# 
# ---
# Convert all the values of 1st array to 64
# 

# In[125]:


arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[0,][0,] = 64
arr3d


# 23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it

# In[129]:


arr_2d1 = np.arange(0,9).reshape(3,3)
print(arr_2d1)
arr_2d1[0,]


# 24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it

# In[130]:


arr_2d2 = np.arange(0,9).reshape(3,3)
print(arr_2d2)
arr_2d2[1,1]


# 25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows

# In[131]:


print(arr_2d2)
arr_2d2[0:2,2]


# 26. Create a 10x10 array with random values and find the minimum and maximum values

# In[134]:


arr_10 = np.arange(0,100).reshape(10,10)
print(arr_10.max())
print(arr_10.min())


# 27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
# ---
# Find the common items between a and b
# 

# In[137]:


a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
c= a[a == b]
c


# 28. a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# 
# ---
# Find the positions where elements of a and b match
# 
# 

# In[12]:


a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
c = np.where(a == b)
c


# 29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will**
# 

# In[149]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
data[np.where(names != 'Will')]


# 30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**
# 
# 

# In[153]:


data[np.where((names != 'Will') & (names != 'Joe'))]


# Difficulty Level **Hard**

# 31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.

# In[161]:


np.linspace(1,15, num=15).reshape(5,3)


# 32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.

# In[172]:


arr32= np.linspace(1,16, num=16).reshape(2,2,4)
print(arr32)


# 33. Swap axes of the array you created in Question 32

# In[175]:


np.swapaxes(arr32,0,2)


# 34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0

# In[234]:


arr34 = np.linspace(0.01,2,10)
print(arr34)
arr34 = np.sqrt(arr34)
arr34[np.where(arr34 < 0.5)] = 0
arr34


# 35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays

# In[259]:


ar351 = np.max(np.random.random(12))
ar352 = np.max(np.random.random(12))
print(ar351)
print(ar352)
arr35 = np.array([ar351,ar352])
arr35


# 36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 
# ---
# Find the unique names and sort them out!
# 

# In[260]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
set(names)


# 37. a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# 
# ---
# From array a remove all items present in array b
# 
# 

# In[281]:


a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
a = np.setdiff1d(a,b)
a


# 38.  Following is the input NumPy array delete column two and insert following new column in its place.
# 
# ---
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# 
# 
# ---
# 
# newColumn = numpy.array([[10,10,10]])
# 

# In[285]:


sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)
sampleArray[:,1] = np.array([[10,10,10]])
sampleArray


# 39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
# 
# 
# ---
# Find the dot product of the above two matrix
# 

# In[287]:


x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
np.dot(x,y)


# 40. Generate a matrix of 20 random values and find its cumulative sum

# In[2]:


import numpy as np
arry12 = np.random.random(20)
print(arry12)
np.cumsum(arry12)

