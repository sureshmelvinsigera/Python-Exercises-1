
# coding: utf-8

# # Solution: Exercise 8.M04

# In[15]:


# Request input from the user
number = input("Please enter an integer: ")

# Convert the input into an integer
number = int(number)


# In[16]:


# Set the counter equal to the number
counter = number

# Initialize the result
factorial = 1

# Initialize the WHILE loop
while (counter > 0):
    # Multiply the result with the current number
    factorial = factorial * counter
    
    # Update the counter
    counter -= 1


# In[17]:


# Display the result
print("The factorial of " + str(number) 
        + " is: " + str(factorial))

