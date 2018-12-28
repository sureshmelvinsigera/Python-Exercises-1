
# coding: utf-8

# # Solution: Exercise 9.E06

# In[1]:


# Set the file name
fileName = "E09.E06_PiToOneMillionDigits.txt"

# Open the file to write
f = open(fileName, "r")

# Initialize a variable which will store the number pi
pi = ""

# Read information from the file
for line in f:
    pi = line

# Close the file
f.close()


# In[6]:


# Set your birthday in ddmmyyyy format
birthday = "01012000"

# Check whether your birthday is in the first one million
# digits of pi
print(birthday in pi)

