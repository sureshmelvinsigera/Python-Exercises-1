
# coding: utf-8

# # Solution: Exercise 4.S01

# ### Visualisation of the sin() and cos() functions

# In this example we will be looking at the sin() function. For illustrative purposes I have added a plot script so you have an idea of what the function looks like. Don't worry about the code written to produce it as it is beyond the scope of this course just look at the plot below.

# In[25]:

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0, 2 * math.pi, 0.01)
ySin = [math.sin(i) for i in x]
yCos = [math.cos(i) for i in x]

plt.plot(x, ySin, label = "sin(x)")
plt.plot(x, yCos, label = "cos(x)")

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()


# The figure above is the sinus(x) and the cos(x) functions between 0 and 2$\pi$.

# ### Solution

# In[27]:

# Importing the math library
import math


# #### a) 
# 
# Calculate: \begin{equation} sin(0) \end{equation}

# In[33]:

# Calculate the result
result = math.sin(0)

# Disply the result
print(result)


# #### b) 
# 
# Calculate: \begin{equation} sin\left(\frac{1}{2} \cdot \pi\right) \end{equation}

# In[34]:

# Calculate the result
result = math.sin(0.5 * math.pi)

# Disply the result
print(result)


# #### c) 
# 
# Calculate: \begin{equation} cos\left(0\right) \end{equation}

# In[36]:

# Calculate the result
result = math.cos(0)

# Disply the result
print(result)


# #### d) 
# 
# Calculate: \begin{equation} cos\left(\frac{1}{2} \cdot \pi\right) \end{equation}

# In[37]:

# Calculate the result
result = math.sin(0.5 * math.pi)

# Disply the result
print(result)


# In[ ]:



