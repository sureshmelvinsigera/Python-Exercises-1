
# coding: utf-8

# # Solution: Exercise 7.M04

# In[18]:


# Generate the initial shopping list
shoppingList = ["milk", "eggs", "red peppers", "chicken",
                "apples", "onions", "bread", "coffee",
                "cucumber"]


# ### a)

# In[19]:


# Determine length of the shopping list
lengthShoppingList = len(shoppingList)

print("The shopping list contains " + str(lengthShoppingList) + " items")


# ### b)

# In[20]:


# Print the shopping list
print("Shopping list:")
print("\t - " + shoppingList[0])
print("\t - " + shoppingList[1])
print("\t - " + shoppingList[2])
print("\t - " + shoppingList[3])
print("\t - " + shoppingList[4])
print("\t - " + shoppingList[5])
print("\t - " + shoppingList[6])
print("\t - " + shoppingList[7])


# ### c)

# In[21]:


# Add two more objects to the list
shoppingList.append("butter")
shoppingList.append("spring onions")

# Display new list to check whether everything worked out
print(shoppingList)


# ### d)

# In[22]:


# Find the index of the onions
onionIndex = shoppingList.index("onions")

# Insert the lemons before the onions
shoppingList.insert(onionIndex, "lemons")

# Display the content of the list
print(shoppingList)


# ### e)

# In[23]:


# Remove the coffee from the list
shoppingList.remove("coffee")

# Display the content of the list
print(shoppingList)


# ### f)

# In[24]:


# Check whether apples are on the shopping list
print("apples" in shoppingList)


# ### g)

# In[25]:


# Print the shopping list
print("Shopping list:")
print("\t - " + shoppingList[0])
print("\t - " + shoppingList[1])
print("\t - " + shoppingList[2])
print("\t - " + shoppingList[3])
print("\t - " + shoppingList[4])
print("\t - " + shoppingList[5])
print("\t - " + shoppingList[6])
print("\t - " + shoppingList[7])
print("\t - " + shoppingList[8])
print("\t - " + shoppingList[9])
print("\t - " + shoppingList[10])

