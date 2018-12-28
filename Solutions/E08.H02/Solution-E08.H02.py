
# coding: utf-8

# # Solution: Exercise 8.H02

# ### a) Converting a decimal number to a binary number

# In[3]:


# Request decimal number to be converted
decimal = input("Please enter a decimal integer: ")

# Store a copy of the decimal number
decimalBackup = decimal

# Convert the string into an integer
decimal = int(decimal)


# In[11]:


# Initialize binary number (in string format!)
binary = ""

# Calculate the binary expression
while (decimal >= 0):
    # Add the modulus to your binary string
    binary += str((decimal % 2))
    # Determine the new decimal value (loop step)
    decimal = decimal // 2
    
    # Exit loop at the end
    if (decimal == 0):
        break
        
# Reverse the string
binary = binary[::-1]
    
# Display result    
print("The decimal number " + str(decimalBackup)
      + " is equal to the following binary number: " 
      + str(binary))


# ### b) Converting a binary number into a decimal number
# 
# 

# In[12]:


# Request binary number to be converted
binary = input("Please enter a binary number: ")

# Store a copy of the binary number
binaryBackup = binary


# In[13]:


# Initialize a variable that will store your result
decimal = 0

# Fill your list with the 2 to the power of i
for i in range(0, len(binary)):
    # Check whether valid bit
    if (binary[i] == "1"):
        # Add newest value to result variable
        decimal += 2**((len(binary)-1)-i)
    else:
        continue

# Display result    
print("The binary number " + str(binaryBackup)
      + " is equal to the following decimal number: " 
      + str(decimal))

