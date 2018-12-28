
# coding: utf-8

# # Solution: Exercise 9.S01

# In[2]:


# Import the math library
import math


# In[3]:


# Initialize the first list
numList = range(0, 1001)


# In[4]:


# Initialize the second list
squareNumList = []

for number in numList:
    # Calculate the square root of the current number
    squareRoot = math.sqrt(number)
    
    # Append the sqaure root to the list
    squareNumList.append(squareRoot)


# In[9]:


# Set the file name
fileName = "E09.S01_SquareRoots.txt"

# Open the file 
f = open(fileName, "w")

# Write a header to the file
f.write("# Square Roots of Numbers Between 0 and 1,000")
f.write("\n# num\tsqrt(num)")

# Initialize a counter
counter = 0

# Loop over the numbers in the lists
while (counter < len(numList)):
    # Write the number and the square root to the file
    f.write("\n" + str(numList[counter]))
    f.write("\t" + str(squareNumList[counter]))
    
    # Update the counter
    counter += 1

# Close the file
f.close()

