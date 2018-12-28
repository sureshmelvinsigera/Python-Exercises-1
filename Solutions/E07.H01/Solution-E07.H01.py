
# coding: utf-8

# # Solution: Exercise 7.H01

# In[1]:


# Initialize 2D list
myNestedList = [[0], [1, 2, 3], [4, 5, 6, 7], [8, 9, 10]]


# ### a)

# In[2]:


# Print the first child list
print(myNestedList[0])


# In[3]:


# Print the second child list
print(myNestedList[1])


# In[4]:


# Print the third child list
print(myNestedList[2])


# In[5]:


# Print the fourth child list
print(myNestedList[3])


# ### b)

# In[6]:


# Print out 0
print(myNestedList[0][0])


# In[7]:


# Print out 3
print(myNestedList[1][2])


# In[8]:


# Print out 4
print(myNestedList[2][0])


# In[9]:


# Print out 9
print(myNestedList[3][1])


# ### c)

# In[10]:


# Replace 8 with 88
myNestedList[3][0] = 88

# Display list
print(myNestedList)


# ### d)

# In[14]:


# Generate the sub-list
mySubList = myNestedList[2][0:3] + myNestedList[3][1:]

# Display the sub-list
print(mySubList)


# ### e)

# In[15]:


# Append new child list
myNestedList.append([11, 12, 13, 14, 15, 16])

# Display updated nested list
print(myNestedList)


# ### f)

# In[16]:


# Insert a new child list
myNestedList.insert(0, [-2, -1])

# Display updated nested list
print(myNestedList)


# ### g)

# In[17]:


# Remove the second child list
del myNestedList[1]

# Display updated nested list
print(myNestedList)


# ### h)

# In[19]:


# Remove element 4 from the nested list
myNestedList[2].remove(4)

# Display updated nested list
print(myNestedList)


# In[20]:


# Remove element 4 from the nested list
myNestedList[3].remove(9)

# Display updated nested list
print(myNestedList)


# ### i)

# In[21]:


# Check whether 10 is in child list 1
print(10 in myNestedList[0])


# In[22]:


# Check whether 10 is in child list 2
print(10 in myNestedList[1])


# In[23]:


# Check whether 10 is in child list 3
print(10 in myNestedList[2])


# In[24]:


# Check whether 10 is in child list 4
print(10 in myNestedList[3])


# In[25]:


# Check whether 10 is in child list 5
print(10 in myNestedList[4])


# ### j)

# In[26]:


# Determine number of child lists
lenParent = len(myNestedList)

# Display result
print(lenParent)


# ### h)

# In[27]:


# Determine length of child list 1
lenChild1 = len(myNestedList[0])

# Display result
print(lenChild1)


# In[28]:


# Determine length of child list 2
lenChild2 = len(myNestedList[1])

# Display result
print(lenChild2)


# In[29]:


# Determine length of child list 3
lenChild3 = len(myNestedList[2])

# Display result
print(lenChild3)


# In[30]:


# Determine length of child list 4
lenChild4 = len(myNestedList[3])

# Display result
print(lenChild4)


# In[31]:


# Determine length of child list 5
lenChild5 = len(myNestedList[4])

# Display result
print(lenChild5)

