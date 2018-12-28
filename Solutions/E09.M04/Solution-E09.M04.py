
# coding: utf-8

# # Solution: Exercise 9.M04

# In[38]:


# Set the file name
fileName = "E09.M04_WorldCountryCapitals.txt"

try:
    # Open the file to append
    f = open(fileName, "r")
except:
    print("Error! File '" + fileName + "' not found!")
else:
    # Initialize data lists
    countries = []
    capitals = []

    # Loop over every line in the file
    for line in f:
        # Split the line
        data = line.split("\t")

        # Store the first column element in countries
        countries.append(data[0])

        # Store the second column element in capital
        capitals.append(data[1][:-1])

    # Close the file
    f.close()


# #### Bonus:

# In[41]:


# Request user input
country = input("Please enter a country: ")


# In[42]:


# Determine the index corresponding to the given country
countryIndex = countries.index(country)

# Determine the corresponding capital
capital = capitals[countryIndex]

# Display capital
print("The capital of " + country + " is " + capital)

