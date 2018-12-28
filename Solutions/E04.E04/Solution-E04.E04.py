
# coding: utf-8

# # Solution: Exercise 4.E04

# ### a)

# Solve \begin{equation} y = 6x^2 + 3x + 2 \end{equation} for \begin{equation} x = 5 \end{equation}

# In[3]:

# Initialize x variable
x = 5

# Calculate corresponding value of y
y = 6 * x**2 + 3 * x + 2

# Display result
print(y)


# ### b)

# For \begin{equation} x = 0.5  \end{equation} determine the result of
# \begin{equation} y = \sqrt{\sqrt{\sqrt{x / 3.6} } }   \end{equation}
# 
# 

# In[13]:

# Declare the variable
x = 10

# Calculate the y value
y = math.sqrt(math.sqrt(math.sqrt(x/3.6)))

# Display result
print(y)


# ### c)

# Determine the two possible solutions to a quadratic equation \begin{equation} ax^2 + bx + c = 0 \end{equation}
# 
# via
# 
# \begin{equation} y_{1/2} =\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}   \end{equation}
# 
# for \begin{equation} a = 3  \end{equation} \begin{equation} b = 10  \end{equation}  \begin{equation} c = -2  \end{equation}

# In[5]:

# Import the math library
import math

# Declare the variables
a = 3
b = 10
c = -2

# Calculate the y values
y1 = (-b + math.sqrt(b**2 - 4 * a * c))/(2*a)
y2 = (-b - math.sqrt(b**2 - 4 * a * c))/(2*a)

# Display result with manual type conversion
print("y1 = " + str(y1))
print("y2 = " + str(y2))


# Note how I converted the primitive data types of the results from float to string using the str() function in order to perform a string concatenation within the print function. If you haven't already done so, have a look at exercise 2.M06 for instructions and motivations behind type conversions.

# ##### Bonus:

# You can also use the format function which will take care of the type conversion for you (see exercise 3.H02):

# In[6]:

# Display result using the format function
print("y1 = {0}".format(y1))
print("y2 = {0}".format(y2))


# In[ ]:



