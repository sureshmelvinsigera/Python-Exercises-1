
# coding: utf-8

# # Solution: Exercise 9.E05

# In[3]:


# Set the file name
fileName = "E09.E04_OneThousand.txt"

# Open the file to write
f = open(fileName, "r")

# Initialize a result variable
sumResult = 0

# Loop over all lines in the file
for line in f:
    # Convert the line to an number
    num = int(line)
    
    # Add the number to our result
    sumResult += num

# Close the file
f.close()

# Display the result
print("The sum of all numbers in the file "
      + fileName + " is " + str(sumResult))

