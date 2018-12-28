
# coding: utf-8

# # Solution: Exercise 4.M02

# ### a) Fahrenheit to Celsius

# To convert a temperature in Fahrenheit to the equivalent temperature in celsius use:
# \begin{equation}
#     T_{Celsius} = (T_{Fahrenheit} - 32) \cdot 5/9
# \end{equation}

# In[9]:

# Initialize test temperature [in Fahrenheit]
temperatureF = 100


# In[10]:

# Convert the temperature from Fahrenheit
# to Celsius
temperatureC = (temperatureF - 32) * 5/9


# In[8]:

# Display the result
print(str(temperatureF) + "°F" + " = " + str(temperatureC) + "°C")


# ### b) Celsius to Fahrenheit

# To convert a temperature in Celsius to the equivalent temperature in Fahrenheit use:
# \begin{equation}
#     T_{Fahrenheit} = T_{Celsius} \cdot 9/5 + 32
# \end{equation}

# In[17]:

# Initialize test temperature [in Celsius]
temperatureC = 100


# In[18]:

# Convert the temperature from Celsius
# to Fahrenheit
temperatureF = temperatureC * 9/5 + 32


# In[19]:

# Display the result
print(str(temperatureC) + "°C" + " = " + str(temperatureF) + "°F")


# In[ ]:



