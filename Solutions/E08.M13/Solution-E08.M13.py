
# coding: utf-8

# # Solution: Exercise 8.M13

# In[2]:


# Initialize the lists
L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
L2 = [8, 9, 10, 11, 12, 13]


# ### a)

# In[3]:


# Generate a new list to store object present 
# in both lists
intersection = []

# Loop over L2 to check each object and whether it's 
# in L1 too
for i in range(0,len(L2)):
    if(L2[i] in L1):
        # The object is in L1 and L2 -> append to list
        intersection.append(L2[i])


# In[4]:


# Display content of list
print(intersection)


# ### b)

# In[5]:


# Generate a new list to store objects present in 
# one or the other list, not both
difference = []

# Loop over L1 to check each object and whether 
# it's also in L2
for i in range(0,len(L1)):
    if(L1[i] not in L2):
        # Append only if in L1 but not L2
        difference.append(L1[i])
        
# Loop over L2 to check each object and whether 
# it's also in L1
for i in range(0,len(L2)):
    if(L2[i] not in L1):
        # Append only if in L2 but not L1
        difference.append(L2[i])


# In[6]:


# Display content of list
print(difference)

