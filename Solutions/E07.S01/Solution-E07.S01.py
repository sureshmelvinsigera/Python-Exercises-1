
# coding: utf-8

# # Solution: Exercise 7.S01

# In[1]:


# Initialize an empty list
listOfCities = []

# Display list
print(listOfCities)


# In[2]:


# As the user for three cities
city1 = input("Please enter the first city: ")
city2 = input("Please enter the second city: ")
city3 = input("Please enter the thirs city: ")


# In[3]:


# Append the input to the list of cities
listOfCities.append(city1)
listOfCities.append(city2)
listOfCities.append(city3)

# Display the list content
print(listOfCities)


# ##### Option 1:
# Check ever list object manually

# In[4]:


# Check first element
print(listOfCities[0] == "London")


# In[5]:


# Check second element
print(listOfCities[1] == "London")


# In[6]:


# Check third element
print(listOfCities[2] == "London")


# ##### Option 2:
# Use the in function

# In[7]:


# Check whether "London" is contained in the list
print("London" in listOfCities)

