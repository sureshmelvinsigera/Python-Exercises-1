
# coding: utf-8

# # Solution: Exercise 6.M02

# In[10]:

# Request day of the week from user
day = input("Please enter the day of the week: ")


# In[11]:

# Request time of the day in 24h format
hour = input("Please enter the time in 24h format: ")


# In[12]:

# Convert the hour into an integer
hour = int(hour)


# In[13]:

# Case 1: It's Sunday
if(day == "Sunday"):
    # Case 1.1: It's between 10am and 5pm and the shop is open
    if(hour >= 10 and hour <= 17):
        # Display message
        print("The shop is currently open.")
    # Default: Shop is closed
    else:
        # Display message
        print("The shop is currently closed.")

# Default: It's not Sunday
else:
    # Case 1.1: It's between 7am and 10pm and the shop is open
    if(hour >= 7 and hour <= 22):
        # Display message
        print("The shop is currently open.")
    # Default: Shop is closed
    else:
        # Display message
        print("The shop is currently closed.")   


# In[ ]:



