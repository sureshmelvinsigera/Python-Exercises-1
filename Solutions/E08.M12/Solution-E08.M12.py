
# coding: utf-8

# # Solution: Exercise 8.M12

# In[1]:


# Importing the math library to access pi
import math


# ### a) 
# 
# Approximate $\pi$ using $\pi = 4 \cdot \sum_{k=0}^{n} \frac{(-1)^k}{2\cdot k +1}$ and $n=10$

# In[2]:


# Set the upper limit of our sum
n = 10

# Generate the pi variable
piApprox = 0

# Generate a loop over all k between 0 and n
# (remember: the range function range(i,j) 
# includes all numbers betweeb i up to but EXCLUDING j
for k in range(0,n+1):
    # Add the new loop element to our approximation of pi
    piApprox += (-1.0)**k / (2.0 * k + 1.0)
    
# Once the summation if complete, multiply with 4
piApprox *= 4.0

# Calculate the deviation in percent
devi = abs(math.pi - piApprox)

# Display the result
print("Approximation of pi: " + str(piApprox))
print("Deviation from math.pi: " + str(devi))



# ### b)
# 
# Approximate $\pi$ using $\pi = 4 \cdot \sum_{k=0}^{n} \frac{(-1)^k}{2\cdot k +1}$ and $n=100$

# In[3]:


# Set the upper limit of our sum
n = 100

# Generate the pi variable
piApprox = 0

# Generate a loop over all k between 0 and n
# (remember: the range function range(i,j) 
# includes all numbers betweeb i up to but EXCLUDING j
for k in range(0,n+1):
    # Add the new loop element to our approximation of pi
    piApprox += (-1.0)**k / (2.0 * k + 1.0)
    
# Once the summation if complete, multiply with 4
piApprox *= 4.0

# Calculate the deviation in percent
devi = abs(math.pi - piApprox)

# Display the result
print("Approximation of pi: " + str(piApprox))
print("Deviation from math.pi: " + str(devi))



# ### c) 
# 
# Approximate $\pi$ using $\pi = 4 \cdot \sum_{k=0}^{n} \frac{(-1)^k}{2\cdot k +1}$ and $n=1000$

# In[4]:


# Set the upper limit of our sum
n = 1000

# Generate the pi variable
piApprox = 0

# Generate a loop over all k between 0 and n
# (remember: the range function range(i,j) 
# includes all numbers betweeb i up to but EXCLUDING j
for k in range(0,n+1):
    # Add the new loop element to our approximation of pi
    piApprox += (-1.0)**k / (2.0 * k + 1.0)
    
# Once the summation if complete, multiply with 4
piApprox *= 4.0

# Calculate the deviation in percent
devi = abs(math.pi - piApprox)

# Display the result
print("Approximation of pi: " + str(piApprox))
print("Deviation from math.pi: " + str(devi))


