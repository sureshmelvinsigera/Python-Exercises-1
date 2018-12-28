
# coding: utf-8

# # Solution: Exercise 7.M05

# In[6]:


# Initialize the list
numberList = [1 if i%11==0 else 0 for i in range(10000)]


# In[8]:


# Count how many times the number 1 is contained in the list:
amountOne = numberList.count(1)


# In[11]:


# Display the result
print("There are " + str(amountOne) + " numbers between 0 and 10,000 that are divisible by 11.")

