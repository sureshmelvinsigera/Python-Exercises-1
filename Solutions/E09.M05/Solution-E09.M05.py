
# coding: utf-8

# # Solution: Exercise 9.M05

# ### a)

# In[19]:


# Ask the user for input
name = input("Please enter your name: ")
date = input("Please enter the date of purchase (dd.mm.yyyy): ")
item = input("Please describe your purchased item: ")
comment = input("How was your shopping experience? ")

print("\nThank you so much for your feedback! Have a good day!")


# In[20]:


# Set the file name
fileName = "E09.M05_Reviews.txt"

# Open the file
f = open(fileName,"a")

# Display final message

# Store the information in the file seperated by tabs
f.write(name)
f.write("\t" + date)
f.write("\t" + item)
f.write("\t" + comment + "\n")
    
# Close file
f.close()


# ### b)

# In[21]:


# Ask for user input
costumerName = input("Please specify a costumer name: ")


# In[22]:


# Set the file name
fileName = "E09.M05_Reviews.txt"

try:
    # Open the file
    f = open(fileName,"r")
except:
    print("Error! File '" + fileName + "' not found!")
else:
    for line in f:
        lineContent = line.split("\t")

        if(lineContent[0] == costumerName):
            # Extract information
            date = lineContent[1]
            item = lineContent[2]
            comment = lineContent[3]

            # Remove new line command \n from comment string
            comment = comment[0:-1]

        else:
            continue

    # Close the file
    f.close()


# In[23]:


# Display message
print(name + " bought '" + item + "' on the " + date 
      + " and left the following comment:\n" + comment)

