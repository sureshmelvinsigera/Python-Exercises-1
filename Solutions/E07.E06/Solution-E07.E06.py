
# coding: utf-8

# # Solution: Exercise 7.E06

# In[4]:


# Initialize lists
babyNames2017 = ["Sophia", "Olivia", "Emma", "Ava", 
                  "Isabella", "Mia", "Aria", "Riley", 
                  "Zoe", "Amelia", "Jackson", "Liam", 
                  "Noah", "Aiden", "Lucas", "Caden", 
                  "Grayson", "Mason", "Elijah", "Logan"]


# In[8]:


# Request user input
babyName = input("Please enter a name: ")


# ### Option 1:

# In[9]:


# Simple check whether the babyName is in the list
print(babyName in babyNames2017)


# ### Option 2:

# In[10]:


# Initialize an IF and ELSE Statement
if (babyName in babyNames2017):
    print(babyName + " was among the top 20 baby names of 2017")
else:
    print(babyName + " was not among the top 20 baby names of 2017")

