
# coding: utf-8

# # Solution: Exercise 7.M06

# In[16]:


# Initialize a list
numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Backup the original list
numberListBackup = numberList[:]


# In[17]:


# Initialize empty reverse list
numberListReverse = []


# In[18]:


# Fill numberListReverse with the objects in numberList
# starting at the end
numberListReverse.append(numberList.pop())
numberListReverse.append(numberList.pop())
numberListReverse.append(numberList.pop())
numberListReverse.append(numberList.pop())
numberListReverse.append(numberList.pop())
numberListReverse.append(numberList.pop())
numberListReverse.append(numberList.pop())
numberListReverse.append(numberList.pop())
numberListReverse.append(numberList.pop())
numberListReverse.append(numberList.pop())


# In[19]:


# Display the results:
print("Original list:")
print(numberListBackup)

print("\nReversed list:")
print(numberListReverse)

