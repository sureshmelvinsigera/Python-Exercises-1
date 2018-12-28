
# coding: utf-8

# # Solution: Exercise 8.E05

# In[1]:


# Initialize empty list
squareList = []

# Display content of list
print(squareList)


# In[2]:


# Initialize the counter
counter = 0

# Initialize the WHILE loop
while (counter <= 1000):
    # Calculate the suqare of the current number
    square = counter**2
    
    # Append the square to the list
    squareList.append(square)
    
    # Update the counter
    counter += 1


# In[3]:


# Display the content of the list
print(squareList)

