
# coding: utf-8

# # Solution: Exercise 4.S02

# In[1]:

# Import the Library
import math


# ### a) Convert Radians to Degrees

# In[2]:

# Initialize an angle in radians
angleRad = 234


# In[4]:

# Convert the angle from radians into degrees
angleDeg = 360 / ( 2 * math.pi) * angleRad


# In[7]:

# Display the result
print(str(angleRad) + " rad = " + str(angleDeg) + " deg")


# ### b) Convert from Degrees to Radians

# In[8]:

# Initialize an angle in degrees
angleDeg = 234


# In[10]:

# Convert the angle from radians into degrees
angleRad = 2 * math.pi / 360  * angleDeg


# In[11]:

# Display the result
print(str(angleDeg) + " deg = " + str(angleRad) + " rad")


# In[ ]:



