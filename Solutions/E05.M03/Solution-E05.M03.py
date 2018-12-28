
# coding: utf-8

# # Solution: Exercise 5.M03

# In[1]:

# Initialize the variables
a = 0
b = 10
c = -5
d = 3
e = 3


# ### a)

# In[2]:

# Evaluate the expression
bol1 = a > b or a > c

# Display the result
print(bol1)


# ### b)

# In[3]:

# Evaluate the expression
bol2 = a == 0.0 or d == 4.9

# Display the result
print(bol2)


# ### c)

# In[4]:

# Evaluate the expression
bol3 = c < -6 or (d > 0 and e == d)

# Display the result
print(bol3)


# ### d)

# In[6]:

# Evaluate the expression
bol4 = a + b <= 11 or d == 5

# Display the result
print(bol4)


# ### e)

# In[7]:

# Evaluate the expression
bol5 = not(a > 30 or d <0)

# Display the result
print(bol5)


# ### f)

# In[8]:

# Evaluate the expression
bol6 = not(not(not((a + e > 2) or (c + b > 0)) or (e - a> 2)))

# Display the result
print(bol6)


# ### g)

# In[9]:

# Evaluate the expression
bol7 = not(b%2 == 0)

# Display the result
print(bol7)


# ### h)

# In[14]:

# Evaluate the expression
bol8 = (c%2 > 0 or e%2 > 0 or b%2 > 0) and a%4 == 0

# Display the result
print(bol8)


# ### i)

# In[12]:

# Evaluate the expression
bol9 = (b//2 > 0 and not(a//2 > 0)) or (not(b//2 > 9) and a//2 > 0)

# Display the result
print(bol9)


# ### j)

# In[13]:

# Evaluate the expression
bol10 = not(bol3 and (a + b**2 > 50)) or d == e

# Display the result
print(bol10)


# In[ ]:



