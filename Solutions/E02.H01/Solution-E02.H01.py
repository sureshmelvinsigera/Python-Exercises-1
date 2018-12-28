
# coding: utf-8

# # Solution: Exercise 2.H01

# In[3]:

# Request user input and assign variables
var1 = float(input("Please enter a first number: "))
var2 = float(input("Please enter a second number: "))

print("Variable content: var1 = " + str(var1) + ", var2 = " + str(var2))


# ### a) Swapping variables with an additional variable

# In[4]:

# Generate a temporary variable
var3 = var1
 
# Swap variable content 
var1 = var2
var2 = var3

print("Variable content: var1 = " + str(var1) + ", var2 = " + str(var2))


# ### b) Swapping variables without an additional variable
# 

# In[5]:

# Let's reverse the change again by swapping the variable content without any 
# new variables
var1 = var1 + var2
var2 = var1 - var2
var1 = var1 - var2

print("Variable content: var1 = " + str(var1) + ", var2 = " + str(var2))


# Version a) of swapping variable is preferable to version b) as every mathematical operation will introduce a (tiny) error due to to intrinsic numerical inaccuracies.

# In[ ]:



