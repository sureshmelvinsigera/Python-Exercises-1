
# coding: utf-8

# # Solution: Exercise 6.E05

# In[4]:

# Request the user age
age = input("Please enter your age: ")


# In[5]:

# Convert the input string into an integer
age = int(age)


# In[7]:

# Case 1: The user is 18 or older
if(age >= 18):
    # Display message
    print("You are allowed to enter.")
    
# Default: The user is younger than 18
else:
    # Display message
    print("You are a minor and not allowed to come in")


# In[ ]:



