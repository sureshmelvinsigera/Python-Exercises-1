
# coding: utf-8

# # Solution: Exercise 4.H02

# In[3]:

# Import the math library
import math


# In[4]:

# Initialize the coordinates of point 1
x1 = -2
y1 = 1


# In[5]:

# Initialize the coordinates of point 1
x2 = 1
y2 = 5


# In[6]:

# Calculate the distance
d = math.sqrt(pow((math.fabs(x1-x2)),2) + pow((math.fabs(y1-y2)),2))


# <i>Hint: You can break above calculation down into several small ones to make it less confusing.</i>

# In[8]:

# Display the result
print("The distance between the two points is: " + str(d))


# ### Bonus

# Instead of explicitly stating the corrdinates of the points at the beginning we will now write a code that accepts the coordinates as user input in the format (x,y).

# ##### Request user input

# In[22]:

# Request user input: First coordinate
pos1 = input("Please specify the first coordinate in the following format: (x,y). ")


# In[23]:

# Request user input: First coordinate
pos2 = input("Please specify the second coordinate in the following format: (x,y). ")


# #### Extract the relevant information from the first coordinate input

# First we need to look at the input format: (x,y)
# 
# Note how each input starts with a (. This character corresponds to index 0 in the string. We can ngelect it. Each input also ends with another ). This is the last index in the string and can also be neglected. Everything between ( and ) is relevant with a , seperating the x- and the y-coordinates.
# 
# We will need to extract the characters between ( and the , and the number between the , and the ). Then we can convert the new strings into numbers and will have obtained the coordinates.

# In[24]:

# Find the corresponding index to the , in the first input string
commaIndex = pos1.find(",")

# Extract a substring from the input from index 1 up to but excluding
# the position of the comma. This is the x-coordinate.
# Remember to convert the string into a number
x1 = float(pos1[1:commaIndex])

# Extract a substring from the input from the position after the comma
# up to but excluding the last index.
# This is the y-coordinate.
# Remember to convert the string into a number
y1 = float(pos1[commaIndex+1:-1])

# Display the coordinates:
print("The first x-coordinate is: " + str(x1))
print("The first y-coordinate is: " + str(y1))


# #### Extract the relevant information from the second coordinate input

# In[25]:

# Find the corresponding index to the , in the second input string
commaIndex = pos2.find(",")

# Extract a substring from the input from index 1 up to but excluding
# the position of the comma. This is the x-coordinate.
# Remember to convert the string into a number
x2 = float(pos2[1:commaIndex])

# Extract a substring from the input from the position after the comma
# up to but excluding the last index.
# This is the y-coordinate.
# Remember to convert the string into a number
y2 = float(pos2[commaIndex+1:-1])

# Display the coordinates:
print("The second x-coordinate is: " + str(x2))
print("The second y-coordinate is: " + str(y2))


# #### Calculate the distance

# Now that we have extracted the information from the user input we can simply use the code we have written above to calculate the distance:

# In[26]:

# Calculate the distance
d = math.sqrt(pow((math.fabs(x1-x2)),2) + pow((math.fabs(y1-y2)),2))


# In[28]:

# And finally we can display the result
print("The distance between " + pos1 + " and " +  pos2 + " is " + str(d))


# In[ ]:



