
# coding: utf-8

# # Solution: Exercise 6.02

# In[1]:

# Request a letter from the user
letter = input("Please enter a letter: ")


# ### Option 1: IF-ELIF-ELSE Chain Statement

# In[4]:

# Case 1: letter == a
if(letter == "a"):
    # Display result
    print(letter + " is a vowel")
    
# Case 2: letter == e
elif(letter == "e"):
    # Display result
    print(letter + " is a vowel")
    
# Case 3: letter == i
elif(letter == "i"):
    # Display result
    print(letter + " is a vowel")
    
# Case 4: letter == o
elif(letter == "o"):
    # Display result
    print(letter + " is a vowel")
    
# Case 5: letter == u
elif(letter == "u"):
    # Display result
    print(letter + " is a vowel")
    
# Default
else:
    # Display result
    print(letter + " is not a vowel")


# ### Option 2: IF-ELSE Statement with OR Operator

# In[11]:

# Case 1: letter is either a, e, i, o, or u
if(letter == "a" or letter == "e" 
       or letter == "i" or letter == "o" 
       or letter == "u" ):
    
    print(letter + " is a vowel")
    
# Default
else:
    # Display result
    print(letter + " is not a vowel")


# In[ ]:



