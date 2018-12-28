
# coding: utf-8

# # Solution: Exercise 6.E04

# In[5]:

# Request user input: Name
name = input("Please enter your name: ")


# In[19]:

# Request user input: Nationality
nationality = input("Please enter your nationality (eng/fr/de/esp/it): ")


# In[20]:

# Case 1: User is English
if(nationality == "eng"):
    # Display greeting
    print("Good morning, " + name + "!")
    
# Case 2: User is French
elif(nationality == "fr"):
    # Display greeting
    print("Bonjour, " + name + "!")
    
# Case 3: User is German
elif(nationality == "de"):
    # Display greeting
    print("Guten Morgen, " + name + "!")
    
# Case 4: User is Spanish
elif(nationality == "esp"):
    # Display greeting
    print("Buenos dias, " + name + "!")
    
# Case 5: User is Italien
elif(nationality == "it"):
    # Display greeting
    print("Buongiorno, " + name + "!")
    
# Default
else:
    print("Sorry, that language is currently not supported.")


# In[ ]:



