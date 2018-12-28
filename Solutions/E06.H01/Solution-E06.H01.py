
# coding: utf-8

# # Solution: Exercise 6.H01

# In[32]:

# Request user input
number = input("Please provide a three digit integer: ")


# In[33]:

# Set the number of digits
digits = 3


# In[34]:

# Extract the individual digits from the number entered
# by the user and convert them into integers

digit1 = int(number[0])
digit2 = int(number[1])
digit3 = int(number[2])


# In[35]:

# Calculate the sum of the individual digits raised to the
# power of the total number of digits (3)
digitSum = digit1 ** digits + digit2 ** digits + digit3 ** digits


# In[36]:

# Case 1:
# digitSum is equal to the original number, meaning the number
# is an Armstrong number
if(digitSum == int(number)):
    print(str(number) + " is an Armstrong number.")
    
# Default:
# digitSum is not equal to the original, meanin the number
# is not an Armstrong number
else:
    print(str(number) + " is not an Armstrong number.")


# In[ ]:



