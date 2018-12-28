
# coding: utf-8

# # Solution: Exercise 8.E01

# In[1]:


# Initialize the message
message = "Hello World"


# In[2]:


# Initialize the counter and set it to 0
counter = 0

# Initialize the WHILE loop
while (counter < 50):
    # Display the message 
    print(message)
    
    # Update the counter
    counter = counter + 1


# Side Note:
# In the context of WHILE loops you will often encounter a notation like this
# 
#         counter += 1
#         
# instead of
# 
#         counter = counter + 1
#         
# Both statements are identical. The first statement is a so-called compound operator and used as shorthand.
