
# coding: utf-8

# # Solution: Exercise 8.E03

# In[2]:


# Initialize an empty list
numberList = []

# Display content of the list
print(numberList)


# ##### Option 1: WHILE loop with counter

# In[3]:


# Initilize a counter
counter = 0

# Initialize WHILE loop
while (counter <= 1000):
    # Append the current counter to the list
    numberList.append(counter)
    
    # Update the counter
    counter += 1


# In[4]:


# Display the list
print(numberList)


# ##### Option 2: WHILE loop without the counter

# In[5]:


# Initialize the while loop
while (len(numberList) <= 1000):
    # Append next number
    numberList.append(len(numberList))


# In[6]:


# Display content of list
print(numberList)

