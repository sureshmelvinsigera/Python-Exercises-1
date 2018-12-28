
# coding: utf-8

# # Solution: Exercise 6.M03

# In[15]:

# Request user input
year = input("Please enter a year: ")


# In[16]:

# Convert the input from string to integer
year = int(year)


# In[17]:

# Case 1: The year is a leap year meaning it is:
# - exactly divisible by 4
# - not exactly divisible by 100
if (year%4 == 0 and year%100 != 0):
    # Display message
    print(str(year) + " is a leap year.")
    
# Case 2: The year is a leap year meaning it is:
# - exactly divisible by 4
# - exactly divisible by 100
# - exactly divisible by 400
elif (year%4 == 0 and year%100 == 0 and year%400 == 0):
    # Display message
    print(str(year) + " is a leap year.")

# Default: The year is not a leap year
else:
    print(str(year) + " is not a leap year.")


# In[ ]:



