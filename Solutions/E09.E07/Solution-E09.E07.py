
# coding: utf-8

# # Solution: Exercise 9.E07

# In[17]:


# Specify the file name
fileName = "E09.E07_PrideAndPrejudice.txt"

# Open the file to read
f = open(fileName, "r")

# Initialize string variable in which to store all lines
book = ""

# Read in each line
for line in f:
    # Append active line to book variable
    book += line

# Close the file
f.close()


# In[18]:


# Calculate the number of words in the book variable
numWords = len(book)


# In[19]:


# Display the result
print("Jane Austen's 'Pride and Prejudice' contains "
      + str(numWords) + " words.")

