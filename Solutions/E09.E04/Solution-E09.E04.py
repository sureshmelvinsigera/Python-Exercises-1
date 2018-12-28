
# coding: utf-8

# # Solution: Exercise 9.E04

# In[3]:


# Set the file name
fileName = "E09.E04_OneThousand.txt"

# Open the file to write
f = open(fileName, "w")

# Initialize a counter
counter = 0

# Loop over all numbers between 0 and 1,000
while (counter <= 1000):
    # Write the number into the file
    f.write(str(counter) + "\n")
    
    # Update the counter
    counter += 1

# Close the file
f.close()

