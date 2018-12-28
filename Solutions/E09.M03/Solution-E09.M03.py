
# coding: utf-8

# # Solution: Exercise 9.M03

# In[19]:


# Set the file name
fileName = "E09.M03_USStates.txt"

try:
    # Open the file to append
    f = open(fileName, "r")
except:
    print("Error! File '" + fileName + "' not found!")
else:
    # Initialize a list to store the states in
    statesUS = []

    # Loop over every line in the file
    for line in f:
        # Case 1: Line is empty or contains nothing but spaces
        if(line == "" or line.strip() == ""):
            # Move on to the next line
            continue
        # Case 2: Line contains actual data
        else:
            # Append current line to list removing the last
            # character which is \n
            statesUS.append(line[:-1])

    # Close the file
    f.close()


# In[20]:


# Display the content of the list
print(statesUS)


# In[21]:


# Count the number of objects in the list
numberStates = len(statesUS)

# Display result
print("There are " + str(numberStates) 
      + " states in the US.")

