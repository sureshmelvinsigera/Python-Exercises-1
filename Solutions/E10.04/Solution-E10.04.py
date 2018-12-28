
# coding: utf-8

# # Solution: Exercise 10.04

# In[1]:


# Initialize function
def CalculateAge(birthYear):
    # Set current year
    currentYear = 2018
    
    # Calculate age of person
    age = currentYear - birthYear
    
    # Return result
    return age


# Let's test the function:

# In[5]:


CalculateAge(1900)


# In[6]:


CalculateAge(2000)


# In[7]:


CalculateAge(1999)

