
# coding: utf-8

# # Solution: Exercise 3.M05

# In[1]:

# Request suer input
fullName = input("Please enter your full name: ")


# In[6]:

# Find the index corresponding to the blank separator:
blankIndex = fullName.find(" ")

# Extract the first name
firstName = fullName[:blankIndex]

# Extract the last name
lastName = fullName[blankIndex+1:]

# Extract the initials
firstInitial = firstName[0]
lastInitial = lastName[0]

# Display the result
print(fullName + " [" + firstInitial + lastInitial + "]")


# Note how you need to add a 1 to lastName = fullName[blankIndex+1:]. If you forget to add the 1 you will extract the blank as well leading to " Monster" (try it out and see what changes!). The first character will then be a blank. Alternatively, you could leave out the 1 and instead remove all blanks from the substring using the strip() function.

# In[ ]:



