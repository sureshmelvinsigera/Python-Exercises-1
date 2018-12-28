
# coding: utf-8

# # Solution: Exercise 6.M04

# In[1]:

# Request user input: month
month = input("Please provide a month: ")


# In[3]:

# Request user input: month
day = input("Please provide a day: ")


# In[ ]:

# Convert the day from string to integer
day = int(day)


# In[4]:

# Case 1: It's winter
if((month == "December" and day >= 21) 
       or (month == "January") 
       or (month == "February") 
       or (month == "March" and day <= 20)):
    # Display message
    print("It's winter!")
    
# Case 2: It's spring
elif((month == "March" and day >= 21) 
         or (month == "April") 
         or (month == "May") 
         or (month == "June" and day <= 20)):
    # Display message
    print("It's spring!")
    
# Case 3: It's summer   
elif((month == "June" and day >= 21) 
         or (month == "July") 
         or (month == "August") 
         or (month == "September" and day <= 20)):
    # Display message
    print("It's summer!")

# Default: It's autumn
else:
    print("It's autumn!")


# In[ ]:



