
# coding: utf-8

# # Solution: Exercise 9.E03

# In[2]:


# Specify the file name
fileName = "E09.E03_LotROpeningLine.txt"

# Open the file to read
f = open(fileName, "r")

# Read in each line
for line in f:
    print(line)

# Close the file
f.close()

