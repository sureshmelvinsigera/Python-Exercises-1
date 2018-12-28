
# coding: utf-8

# # Solution: Exercise 6.M05

# In[1]:

# Request input from the user
stringOriginal = input("Please enter a word: ")


# In[2]:

# Reverse the string using string slicing operations
stringReversed = stringOriginal[::-1]


# In[5]:

# Case 1: The original and the reversed string are identical
if(stringOriginal.lower() == stringReversed.lower()):
    # Display message
    print(stringOriginal + " is a palindrome.")
    
# Default: The original and the reversed string are not
# identical
else:
    # Display message
    print(stringOriginal + " is not a palindrome.")


# Note how we used the lower() function to transform both strings into all lower case letters before comparing them. This step is necessary because Python is case-sensitive.

# In[ ]:



