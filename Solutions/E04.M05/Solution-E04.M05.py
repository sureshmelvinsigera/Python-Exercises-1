
# coding: utf-8

# # Solution: Exercise 4.M05

# In[41]:

# Ask the user for a time duration in seconds and
# convert it to an integer straight away
tSeconds = int(input("Please enter a time duration in seconds: "))


# In[42]:

# Backup the initial number of seconds
tSecondsInitial = tSeconds


# #### Calculate how many full days are contained in tSeconds

# In[43]:

# Calculate the number of seconds in a day
secondsInDay = 24 * 60 * 60

# Calculate how many full days are in tSeconds
tDays = tSeconds // secondsInDay

# Calculate the remaining seconds after subtracting the full days
tSeconds = tSeconds % secondsInDay


# #### Calculate how many full hours are contained in the remaing tSeconds

# In[44]:

# Calculate the number of seconds in an hours
secondsInHour = 60 * 60

# Calculate how many full days are in tSeconds
tHours = tSeconds // secondsInHour

# Calculate the remaining seconds after subtracting the full hours
tSeconds = tSeconds % secondsInHour


# #### Calculate how many full minutes are contained in the remaing tSeconds

# In[45]:

# Calculate the number of seconds in an hours
secondsInMinute = 60

# Calculate how many full days are in tSeconds
tMinutes = tSeconds // secondsInMinute

# Calculate the remaining seconds after subtracting the full minutes
tSeconds = tSeconds % secondsInMinute


# #### Display the result

# In[46]:

print(str(tSecondsInitial) + " seconds correspond to " + str(tDays) + " days, " + str(tHours) + " hours, " + str(tMinutes) + " minutes, and " + str(tSeconds) + " seconds.")


# ### Bonus:

# Above print command looks very messy which tends to happen once you try and print multiple values and especially if some of them need to be converted as well. Below the same output is prioduced using the format function (see exercise 3.H02):

# In[47]:

print("{0} seconds correspond to {1} days, {2} hours, {3} minutes, and {4} seconds."
      .format(tSecondsInitial, tDays, tHours, tMinutes, tSeconds))


# In[ ]:



