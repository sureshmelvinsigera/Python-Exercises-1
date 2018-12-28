
# coding: utf-8

# # Solution: Exercise 4.E03

# In[5]:

import math


# In[6]:

# Initialization of variables

num1 = 100
num2 = 0.0
num3 = -100
num4 = 33
num5 = 16
num6 = 1000


# ### a)

# Calculate the square root of num1

# In[8]:

# Carry out the calculation
result = math.sqrt(num1)

# Display the result
print(result)


# ### b)

# Calculate the square root of num4

# In[10]:

# Carry out the calculation
result = math.sqrt(num4)

# Display the result
print(result)


# ### c)

# Calculate the absolute value of num5

# In[13]:

# Carry out the calculation
result = math.fabs(num5)

# Display the result
print(result)


# ### d)

# Calculate the absolute value of num3

# In[16]:

# Carry out the calculation
result = math.fabs(num3)

# Display the result
print(result)


# ### e)

# Determine whether the absolute value of num1 and num3 are the same

# In[17]:

# Carry out the calculation
result = math.fabs(num1) == math.fabs(num3)

# Display the result
print(result)


# ### f)

# Determine whether the square root of num6 is larger than num1

# In[18]:

# Carry out the calculation
result = math.sqrt(num6) > math.sqrt(num1)

# Display the result
print(result)


# ### g)

# Determine whether the absolute value of num5 is smaller than num2

# In[19]:

# Carry out the calculation
result = math.fabs(num5) < num2

# Display the result
print(result)


# ### h)

# Determine whether the square root of the sum of num1 and num2 is larger than 200

# In[20]:

# Carry out the calculation
result = math.sqrt(num1 + num2) > 200

# Display the result
print(result)


# ### i)

# Determine the multiplication product of the square root of num5 and the absolute value of num3

# In[21]:

# Carry out the calculation
result = math.sqrt(num5) * math.fabs(3)

# Display the result
print(result)


# ### j)

# In[23]:

# Carry out the calculation
result = math.sqrt(math.sqrt(num5))

# Display the result
print(result)


# In[ ]:



