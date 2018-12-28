
# coding: utf-8

# # Solution: Exercise 4.H01

# ### a) Building AND using only OR and NOT

# Instead of writing
# 
#         statement1 and statement2
#         
# you can also write:
# 
#         not(not statement1 or not statement2)
#         
# both logical operators will return the same results for any values of statement1 and statement2.

# In[3]:

# Change the values here to check the behavious
statement1 = True
statement2 = True

andCombination = not(not statement1 or not statement2)

print("Original: " + str(statement1 and statement2))
print("Combination: " + str(andCombination))


# ### b) Building OR using only NOT and AND

# Instead of writing
# 
#         statement1 or statement2
#         
# you can also write:
# 
#         not(not statement1 and not statement2)
#         
# both logical operators will return the same results for any values of statement1 and statement2.

# In[4]:

# Change the values here to check the behavious
statement1 = True
statement2 = False

orCombination = not(not statement1 and not statement2)

print("Original: " + str(statement1 or statement2))
print("Conversion: " + str(orCombination))


# In[ ]:



