
# coding: utf-8

# # Solution: Exercise 9.E01

# In[2]:


# Set the filenamne
fileName = "E09.E01_HelloWorld.txt"

# Open the file to write
f = open(fileName, "w")

# Write strings to file
f.write("Hello World")
f.write("\nGoodbye World")

# Close the file
f.close()

