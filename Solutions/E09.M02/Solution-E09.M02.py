
# coding: utf-8

# # Solution: Exercise 9.M02

# In[15]:


# Set the file name
fileName = "E09.M02_IrishProvinces.txt"

try:
    # Open the file to append
    f = open(fileName, "r")
except:
    print("Error! File '" + fileName + "' not found!")    
else:
    # Loop over every line in the file
    for line in f:
        # Case 1: Comment line
        if(line[0] == "#"):
            # Move on to the next line
            continue
        # Case 2: Line is actual data line
        else:
            print(line)

    # Close the file
    f.close()

