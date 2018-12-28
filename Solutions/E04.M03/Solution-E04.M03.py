
# coding: utf-8

# # Solution: Exercise 4.M03

# In[2]:

# Import the math library
import math


# ### a) Calculate the area of a circle

# The area of a circle with a given radius is calculate via:
# \begin{equation} A = \pi \cdot r^2 \end{equation}

# In[3]:

# Initialize the radius of the circle
radius = 2.0


# In[14]:

# Calculate the area of the circle
area = math.pi * radius**2


# In[16]:

# Display the result
print("The area of a circle with radius " + str(radius) + " is " + str(area))


# ### b) Calculate the volume of a sphere

# The volume of a sphere with a given radius is calculate via:
# \begin{equation} V = \frac{4}{3} \cdot \pi \cdot r^3 \end{equation}

# In[13]:

# Initialize the radius of the sphere
radius = 2.0


# In[18]:

# Calculate the volume of the sphere
volume = 4.0 / 3.0 * math.pi * radius**3


# In[19]:

# Display the result
print("The volume of a sphere with radius " + str(radius) + " is " + str(volume))


# In[ ]:



