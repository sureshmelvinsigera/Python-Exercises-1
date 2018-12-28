
# coding: utf-8

# # Solution: Exercise 7.M03

# In[1]:


# Initialize the list
myList = 14 * [0] + [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[2]:


# Display the list
print(myList)


# In[4]:


# Find the index corresponding to the object 1
indexOne = myList.index(1)


# In[5]:


# Generate a sub-list containing all the elements of the original
# list from indexOne to the end
mySubList = myList[indexOne:len(myList)]


# In[6]:


# Display the new sub-list:
print(mySubList)

