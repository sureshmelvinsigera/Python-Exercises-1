
# coding: utf-8

# # Solution: Exercise 9.E02

# In[13]:


# Request input from the user
item = input("Please enter an item for the shopping list: ")

# Set the file name
fileName = "E09.E02_ShoppingList.txt"

# Open the file to append
f = open(fileName, "a")

# Write the item to the shopping list
f.write("- " + item + "\n")

# Close the file
f.close()

