
# coding: utf-8

# # Solution: Exercise 7.M01

# In[4]:


# Generate the sub-lists
list1 = [1]
list2 = 2 * [2]
list3 = 3 * [3]
list4 = 4 * [4]
list5 = 5 * [5]
list6 = 6 * [6]
list7 = 7 * [7]
list8 = 8 * [8]
list9 = 9 * [9]
list10 = 10 * [10]


# In[5]:


# Add all the list together
bigList = list1 + list2 + list3 + list4 + list5
bigList = bigList + list5 + list6 + list7 
bigList = bigList + list8 + list9 + list10


# In[6]:


# Display list content
print(bigList)

