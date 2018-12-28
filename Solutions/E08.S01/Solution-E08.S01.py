
# coding: utf-8

# # Solution: Exercise 8.S01

# In[7]:


# Define the list of words
words = ["greet", "doctor", "balance", "writing",
         "belligerent", "compete", "thoughtless",
         "furtive", "dad", "month", "excite", "nest", 
         "bright", "seat", "political", "extend", 
         "fold", "smoke", "servant", "elegant"]


# In[12]:


# We then define a variable that will store the index 
# of the longest word so we can extract it later
longIndex = 0

# Generate a variable storing the length of the 
# longest word we've found so far
longLength = 0

# Generate a variable that stores the number of iterations
counter = 0


# In[10]:


# Loop over all elements in the list
for word in words:
    # Determine the length of the current word stored in i
    length = len(word)
    
    # Let's test if this new word is longer then 
    # our currently longest word
    if (length > longLength):
        # If so, let's update the length of the
        # longest word 
        longLength = length
        
        # Set the index equal to our current counter
        longIndex = counter
        
        # Update our iteration counter
        counter += 1
        
    # If the current word is shorter then our current 
    # longest word we want to update our counter 
    # and simply move on to the next word
    else:
        # Update our iteration counter
        counter += 1
 


# In[9]:


# Display the longest word
print("The longest word in our list is: "+ words[longIndex])

