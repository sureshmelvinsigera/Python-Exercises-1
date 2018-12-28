
# coding: utf-8

# # Solution: Exercise 8.M09

# ### a)

# In[2]:


# Initialize list that will store all the prime numbers
primeList = []

# Specify lower and upper boundary:
numMin = 2
numMax = 1000

# Loop over all numbers between num_min and num_max
for i in range(numMin,numMax):
    # Generate a flag indicating whether the number is
    # a prime or not (default: TRUE)
    prime = True
    
    # Loop over all numbers between 2 and i/2
    j = 2
    while (j <= i/2):
        # Case 1: The number is divisible by j 
        # and therefore not a prime
        if(i%j == 0):
            # Set flag to False and exit nested loop
            prime = False
            break
        else:
            # Update the counter and continue   
            j += 1
        
    # Check the prime flas
    if(prime):
        # The number is a prime, let's append it to
        # out list of prime numbers
        primeList.append(i)
    else:
        # The number is not a prime, let's continue to
        # the next itertion
        continue


# In[4]:


# Display the lis tof primes
print(primeList)


# ### b)

# In[6]:


# Initialize a counter for the primes
primeCounter = 0

# Loop over the list of prime numbers
for number in primeList:
    # Add another number to our counter
    primeCounter += 1
    
# Display the primeCounter
print("There are " + str(primeCounter) 
      + " prime numbers between " + str(numMin) 
      + " and " + str(numMax))

