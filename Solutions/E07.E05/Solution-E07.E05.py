
# coding: utf-8

# # Solution: Exercise 7.E05

# In[18]:


# Initialize lists
numberList = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
stringList = ["February", "2018", "Europe", "Earth"]


# ### a)
# 
# 

# In[19]:


# Removing the string February from stringList
stringList.remove("February")

# Display updated list
print(stringList)


# ### b)

# In[20]:


# Removing the string "Earth" from stringList
del stringList[2]

# Display the updated list
print(stringList)


# ### c)

# In[21]:


# Removing all number 3s from numberList
del numberList[3]
del numberList[3]
del numberList[3]

# Display updated list
print(numberList)


# ### d)

# In[22]:


# Removing all number 4s from numberList
numberList.remove(4)
numberList.remove(4)
numberList.remove(4)
numberList.remove(4)

# Display updated list
print(numberList)

