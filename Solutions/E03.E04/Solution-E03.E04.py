
# coding: utf-8

# # Solution: Exercise 3.E04

# In[1]:

# Request user input
userInput = input("Please hit some random keys: ")


# In[9]:

# Count the occurrences of a in the string
occurrencesA = userInput.count("a")

# Count the occurrences of e in the string
occurrencesE = userInput.count("e")

# Count the occurrences of i in the string
occurrencesI = userInput.count("i")

# Count the occurrences of o in the string
occurrencesO = userInput.count("o")

# Count the occurrences of u in the string
occurrencesU = userInput.count("u")


# In[10]:

# Display result
print("The string '" + userInput + "' contains:")
print("\t- 'a':\t" + str(occurrencesA))
print("\t- 'e':\t" + str(occurrencesE))
print("\t- 'i':\t" + str(occurrencesI))
print("\t- 'o':\t" + str(occurrencesO))
print("\t- 'u':\t" + str(occurrencesU))


# In[ ]:



