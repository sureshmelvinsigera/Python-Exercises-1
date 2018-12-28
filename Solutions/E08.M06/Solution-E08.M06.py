
# coding: utf-8

# # Solution: Exercise 8.M06

# In[4]:


# Initialize a list
cities = []


# In[5]:


# Initialize an infinite loop
while True:
    # Ask the user for a city
    city = input("Please enter a city or type STOP to quit: ")
    
    # Case 1: The user has entered STOP
    if(city == "STOP"):
        # Trigger the break command to terminate the loop 
        break
    # Case 2: The user has not entered STOP
    else:
        # Append the new city to the list of cities
        cities.append(city)


# In[6]:


# Display the content of the list
print(cities)

