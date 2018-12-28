
# coding: utf-8

# # Solution: Exercise 8.M05

# In[8]:


# Initialize a test list
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
          11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Backup the list
myListBackup = myList[:]


# In[9]:


# Initialize the empty reverse list
myListReverse = []

# Generate a while loop
while (len(myList) > 0):
    # Remove and return the last object of myList
    lastObject = myList.pop()
    
    # Append the object to the reverse list
    myListReverse.append(lastObject)


# In[10]:


# Display the result
print("Original list:")
print(myListBackup)

print("\nReverse list:")
print(myListReverse)

