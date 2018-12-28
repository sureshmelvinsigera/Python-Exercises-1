
# coding: utf-8

# # Solution: Exercise 8.S02

# In[20]:


# Request a number
numberStr = input("Please enter an integer: ")

# Convert the number into an integer
numberInt = int(numberStr)


# In[21]:


# Determine how many digits the number has
digits = len(numberStr)

# Initialize a result variable
result = 0

# Initialize a counter
counter = 0

# Loop over every digit of the input number
while (counter < digits):
    # Calculate the number corrsponding to the digit
    # counter to the power of digit
    # (Remember to convert the string into an int)
    tmpResult = int(numberStr[counter])**digits
    
    # Add the temporary result to the result variable
    result = result + tmpResult
    
    # Update the counter
    counter = counter + 1


# In[22]:


# Compare the original number to the result

# Case 1: The numbers are identical
if(result == int(numberInt)):
    print(numberStr + " is an Armstrong number!")
# Case 2: The numbers are different
else:
    print(numberStr + " is not an Armstrong number.")

