
# coding: utf-8

# # Solution: Exercise 8.M07

# In[14]:


# Initialize an emoty list
numberList = []


# In[15]:


# Initialize a counter
counter = 0

# Initialize WHILE loop
while (counter <= 1000):
    # Calculate the modulus 5 of the current counter
    mod5 = counter % 5
    
    # If the number is divisible by 5 (meaning mod5 == 0)
    # skip ahead to the next iteration
    if(mod5 == 0):
        # Update the counter
        counter += 1
        
        # Skip rest of the current iteration
        continue
    
    # Add the number to the list
    numberList.append(counter)
    
    # Update the counter
    counter += 1


# In[17]:


# Count the number of elements in the list
lenList = len(numberList)

# Display the result
print("The list contains " + str(lenList) + " numbers.")

