
# coding: utf-8

# # Solution: Exercise 8.M01

# In[15]:


# Initialize an empty list
numberList = []

# Initialize a counter
counter = 1

# Fill the list with numbers
while (counter <= 10000):
    # Add the current counter to the list
    numberList.append(counter)
    
    # Update the counter
    counter += 1


# ###### Option 1: WHILE loop

# In[16]:


# Initialize a result variable for the sum of all numbers
sum = 0

# Initialize a new counter
counter = 0

# Initialize the WHILE loop
while (counter < len(numberList)):
    # Add the current list element to the sum
    sum = sum + numberList[counter]
    
    # Update the counter
    counter += 1


# In[17]:


# Display the result
print("The sum of all numbers between 1 and 10,000 is:")
print(sum)


# ##### Option 2: FOR loop

# In[18]:


# Initialize a result variable for the sum of all numbers
sum = 0

# Initialize the FOR loop
for number in numberList:
    # Add the current list element to the sum
    sum = sum + number


# In[19]:


# Display the result
print("The sum of all numbers between 1 and 10,000 is:")
print(sum)


# ##### Bonus: Calculating the average

# The average of a list of numbers is the sum of all numbers divided by the total number of numbers.

# In[20]:


# Determine the number os objects in the list
objectNumber = len(numberList)

# Determine the average number
average = sum / objectNumber

# Display the result
print(average)

