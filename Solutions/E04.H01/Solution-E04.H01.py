
# coding: utf-8

# # Solution: Exercise 4.H01

# Copying the original code block into our Jupyter Notebook gives us:

# In[1]:

# Define variables
num1 = 0.3
num2 = 0.2 + 0.1

# Check if both variables contain the same value
print(num1 == num2)


# which is not what we would expect. After all, we know that 
# \begin{equation} 0.2 + 0.1 = 0.3 \end{equation}
# to the comparison between num1 and num2 should return <b>TRUE</b>

# But let's take a closer look at print the numbers themselves:

# In[3]:

print("num1 = " + str(num1))
print("num2 = " + str(num2))


# Even though the numbers should be the same, Python has added a 0000000000000004 to the end of num2.
# 
# Errors such as this occur in all programming languages due to the nature of floating-point numbers and the fact that computers are not precise but will always round numbers to a certain degree.

# If you want to compare two numbers, it's usually better to make sure their difference is smaller than a very small number, for example 0.0000000000001. If this is true, we can treat them as being equal:

# In[5]:

# Define variables
num1 = 0.3
num2 = 0.2 + 0.1

# Define largest difference we will allow between num1 and num2 for
# them to be still considered equalt
maxDifference = 0.0000000000001

# Check the difference between num1 and num2
difference = num1 - num2

# Check whether difference < max Difference 
# (if so, the numbers are considered to be equal)
print(difference < maxDifference)


# In[ ]:



