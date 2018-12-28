
# coding: utf-8

# # Solution: Exercise 3.H01

# In[1]:

# Request input from the user
string = input("Please enter a word: ")


# In[2]:

# Reverse the string
reverseString = string[::-1]


# Above command will print every character in the original string starting with index i = -1 (which is the last index), then index i = -1-1 = -2 (which is one index before the last index), then index i = -1-1-1 = -3 (which is two indices before the last index) and so on. In other words: You are iterating throught the string with step -1.

# In[3]:

# Display result
print(reverseString)


# In[ ]:



