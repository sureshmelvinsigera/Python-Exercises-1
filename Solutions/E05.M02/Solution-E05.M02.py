
# coding: utf-8

# # Solution: Exercise 5.M02

# In[2]:

# Initialize the variables
bol1 = False
bol2 = True
bol3 = False


# ### a)

# In[4]:

# Determine logical expression
bol4 = bol1 or bol2 and not bol3

# Display result
print(bol4)


# ### b)

# In[5]:

# Determine logical expression
bol5 = not bol1 and bol3 or bol2

# Display result
print(bol5)


# ### c)

# In[6]:

# Determine logical expression
bol6 = not(bol2 or bol3)

# Display result
print(bol6)


# ### d)

# In[7]:

# Determine logical expression
bol7 = not(bol2 and not bol3)

# Display result
print(bol7)


# ### e)

# In[8]:

# Determine logical expression
bol8 = not(bol1 or bol2) or (bol2 and bol3)

# Display result
print(bol8)


# ### f)

# In[9]:

# Determine logical expression
bol9 = bol1 or (bol1 or (bol1 or bol2)) or bol3

# Display result
print(bol9)


# ### g)

# In[10]:

# Determine logical expression
bol10 = bol9 and bol2 and not bol3

# Display result
print(bol10)


# In[ ]:



