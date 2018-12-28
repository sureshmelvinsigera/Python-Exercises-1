
# coding: utf-8

# # Solution: Exercise 8.M03

# In[6]:


# Initialize an empty list
numberList = []


# In[7]:


# Initialize counter
counter = 0

# Initialize WHILE loop
while (counter < 1000000):
    # Determine the modulus 17 of the current number
    modNumber = counter % 17
    
    # Case 1: The number is divisible by 17
    if(modNumber == 0):
        # Append the number to the list
        numberList.append(counter)
        
        # Update counter
        counter += 1
    # Case 2: The number is not divisible by 17
    else:
        # Do nothing except update the counter
        counter += 1


# In[9]:


# Determine length of list
lenList = len(numberList)


# In[14]:


# Display result
print("There are " + str(lenList) 
      + " numbers between 0 and 1,000,000 that are divisible by 17.")

