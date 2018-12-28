
# coding: utf-8

# # Solution: Exercise 6.M06

# In[2]:

# Initialize the variables
num1 = 0
num2 = 33
num3 = -40


# ### a) Determine the Maximum

# In[3]:

# Case 1: num1 is larger than num2
if(num1 > num2):
    # Case 1.1: num1 is also larger than num3
    if(num1 > num3):
        # Set maximum value
        maximum = num1
    # Case 1.2: num3 is larger than num1
    else:
        # Set maximum value
        maximum = num3

# Case 2: num2 is larger than num1
else:
    # Case 2.1: num2 is also larger than num3
    if(num2 > num3):
        # Set maximum value
        maximum = num2
    # Case 2.2: num3 is larger than num2
    else:
        # Set maximum value
        maximum = num3

        
# Display final result
print("The maximum of the numbers {0}, {1}, and {2} is {3}."
          .format(num1,num2,num3,maximum))


# ### b) Determine the Minimum

# In[4]:

# Case 1: num1 is smaller than num2
if(num1 < num2):
    # Case 1.1: num1 is also smaller than num3
    if(num1 < num3):
        # Set minimum value
        minimum = num1
    # Case 1.2: num3 is smaller than num1
    else:
        # Set minimum value
        minimum = num3

# Case 2: num2 is smaller than num1
else:
    # Case 2.1: num2 is also smaller than num3
    if(num2 > num3):
        # Set minimum value
        minimum = num2
    # Case 2.2: num3 is smaller than num2
    else:
        # Set minimum value
        minimum = num3

        
# Display final result
print("The minimum of the numbers {0}, {1}, and {2} is {3}."
          .format(num1,num2,num3,minimum))


# In[ ]:



