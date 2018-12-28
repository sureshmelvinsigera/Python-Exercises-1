
# coding: utf-8

# # Solution: Exercise 7.E02

# In[18]:


# Initializing the lists
citiesUK1 = ["London", "Birmingham", "Leeds", "Glasgow"]
citiesUK2 = ["Sheffield", "Bradford", "Manchester", "Edinburgh"]


# In[19]:


# Combining both lists
citiesUK = citiesUK1 + citiesUK2


# ### a)

# In[20]:


# Display the entire list
print(citiesUK)


# ### b)

# In[21]:


# Display the third object in the list
print(citiesUK[2])


# ### c)

# In[22]:


# Display the last object
print(citiesUK[7])


# In[23]:


# Side Note:
# The last element in a list (and a string) also corresponds to 
# index -1, so the following syntax is also valid
print(citiesUK[-1])


# ### d)

# In[24]:


# Change the first object from London to Cardiff
citiesUK[0] = "Cardiff"

# Display the list
print(citiesUK)


# ### e)

# In[26]:


# Generate a sub-list
citiesUK3 = citiesUK[1:7] 

# Display the list content
print(citiesUK3)

