
# coding: utf-8

# # Solution: Exercise 3.E01

# In[1]:

# Initialize the string
string = "Triceratops"


# ### a)

# In[2]:

# Transform the string in all upper letters
stringUpper = string.upper()

# Display the result
print(stringUpper)


# ### b)

# In[3]:

# Transform the string in all upper lower
stringLower = string.lower()

# Display the result
print(stringLower)


# ### c)

# In[6]:

# Count the occurrences of t in the string
occurrencesT = string.count("t")

# Display the result
print(occurrencesT)


# Note that Python is case sensitive. This means, Python will treat "t" and "T" as different letters.

# ### d)

# In[7]:

# Count the occurrences of t in the string
occurrencesP = string.count("p")

# Display the result
print(occurrencesP)


# ### e)

# In[8]:

# Find the index of letter a
indexA = string.find("a")

# Display the result
print(indexA)

