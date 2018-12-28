
# coding: utf-8

# # Solution: Exercise 7.M02

# In[15]:


# Initialize the lists (using list comprehension)
list1 = [i for i in range(10000) if i%3 == 0]
list2 = [i for i in range(10000) if i%4 == 0]
list3 = [i for i in range(10000) if i%5 == 0]


# In[16]:


# Determine the length of list1
lengthList1 = len(list1)

# Display the result
print("list1 contains " + str(lengthList1) + " objects.")


# In[17]:


# Determine the length of list2
lengthList2 = len(list2)

# Display the result
print("list2 contains " + str(lengthList2) + " objects.")


# In[19]:


# Determine the length of list3
lengthList3 = len(list3)

# Display the result
print("list3 contains " + str(lengthList3) + " objects.")

