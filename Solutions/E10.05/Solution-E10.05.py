
# coding: utf-8

# # Solution: Exercise 10.05

# ### Find the Maximum

# In[3]:


# Initialize function
def FindMaximumInList(myList):
    # Initialize temp. variable for maximum
    maximum = myList[0]
    
    # Initialize counter
    counter = 0
    
    # Iterate over list
    while (counter < len(myList)):
        # If the current element is larger than the
        # current maximum, set the maximum to the current
        # element
        if(myList[counter] > maximum):
            maximum = myList[counter]
        
        # Update counter
        counter = counter + 1
            
    # Return result
    return maximum       


# In[4]:


# Initialize some test list
testList = [0, -100, 100, 3, 67, 402, 1000, -1000, 0, 345, 9, 19]


# In[5]:


# Test function
print(FindMaximumInList(testList))


# ### Find the Minimum

# In[6]:


# Initialize function
def FindMinimumInList(myList):
    # Initialize temp. variable for maximum
    minimum = myList[0]
    
    # Initialize counter
    counter = 0
    
    # Iterate over list
    while (counter < len(myList)):
        # If the current element is larger than the
        # current maximum, set the maximum to the current
        # element
        if(myList[counter] < minimum):
            minimum = myList[counter]
        
        # Update counter
        counter = counter + 1
            
    # Return result
    return minimum       


# In[7]:


# Initialize some test list
testList = [0, -100, 100, 3, 67, 402, 1000, -1000, 0, 345, 9, 19]


# In[8]:


# Test function
print(FindMinimumInList(testList))

