
# coding: utf-8

# # Solution: Exercise 5.M01

# Let's execute the code example from the exercise first:

# In[ ]:

x = 5
y = "This is a string"

# Case 1:
print("x > 0 or y > 0: " + str(x > 0 or y > 0))


# In[2]:

# Case 2:
print("x > 0 and y > 0: " + str(x > 0 and y > 0))


# The reason why Case 1 is executed without a problem while Case 2 results in an error is so-called short-circuit evaluation.

# In Case 1 the logical operator is <b>OR</b>. The <b>OR</b> operator acts on two statements as follows:
#     
#                             statement1 or statement2
# 
# The <b>OR</b> operator only needs one of the above statements to be <b>TRUE</b> to return <b>TRUE</b>. So if statement1 is <b>TRUE</b> Python does not to care at all about statement2 as result of the <b>OR</b> operation has already been decided. To save time, statement2 won't even be evaluated and Python will therefore never run into the error.

# In Case 2 the logical operator is <b>AND</b>. The <b>AND</b> operator acts on two statements as follows:
#     
#                             statement1 and statement2
# 
# The <b>AND</b> operator needs both statements to be <b>TRUE</b> to return <b>TRUE</b>. If statement1 is <b>TRUE</b> Python still needs to know the value of statement2 to make a decision. So this time, statement2 is evaluated and Python will encounter the error.

# In[ ]:



