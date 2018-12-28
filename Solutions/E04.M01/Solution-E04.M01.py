
# coding: utf-8

# # Solution: Exercise E04.M01

# ### a) Kilometres to miles

# To convert a distance in kilometres to the equivalent distance in miles use:
# \begin{equation}
#     x_{miles} = 0.621371 \cdot x_{km}
# \end{equation}

# In[3]:

# Initialize test distance [in km]
distanceKm = 100


# In[4]:

# Convert the distance from km to miles
distanceMiles = 0.621371 * distanceKm


# In[5]:

# Display the result
print(str(distanceKm) + " km" + " = " + str(distanceMiles) + " miles")


# ### b) Miles to kilometres

# To convert a distance in miles to the equivalent distance in kilometers use:
# \begin{equation}
#     x_{km} = 1.60934\cdot x_{miles}
# \end{equation}

# In[7]:

# Initialize test distance [in miles]
distanceMiles = 100


# In[8]:

# Convert the distance from km to miles
distanceKm = 1.60934 * distanceMiles


# In[9]:

# Display the result
print(str(distanceMiles) + " Miles" + " = " + str(distanceKm) + " km")


# In[ ]:



