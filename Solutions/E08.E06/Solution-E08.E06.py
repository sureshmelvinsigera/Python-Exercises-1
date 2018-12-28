
# coding: utf-8

# # Solution: Exercise 8.E06
# 

# In[3]:


# Initialize a list
numberList = [0.001, 45, 234, 0.45, 2, 94, 63, -0.5]


# In[4]:


# Initialize new empty list
numberList10 = []

# Display content of new list
print(numberList10)


# In[5]:


# Initialize FOR loop
for item in numberList:
    # Calculate the product of 10 * object
    result = 10 * item
    
    # Append it to the new list
    numberList10.append(result)


# In[7]:


# Display the content of the new list
print(numberList10)

