
# coding: utf-8

# # Solution: Exercise 8.H01

# In[6]:


# List of costumers
costumer = [["Lorn Winthrop", "324190810"],
            ["Jordain Honor", "328423458"],
            ["Alvie Gone", "323535232"],
            ["Dobrinsky Kimble", "345289475"],
            ["Garfinkel Kulseth", "987917597"],
            ["Pollerd Bocock", "923845783"],
            ["Conners Corri", "198734563"],
            ["Fleisher Athenian", "234523532"],
            ["Donaldson Bolan", "345245901"],
            ["Ketty Statis", "903471598"]]


# In[9]:


# Let's ask the user for a name
name = input("Please specify a costumer name: ")


# In[10]:


# We will now loop over our 2D list and check if the name 
# stored in the first element of the child list is
# equal to the name the user gave us

# First define the counter variable for a while loop
i = 0

while (i < len(costumer)):
    
    # Check whether the names are identical
    # (the name is element 1 of the child list which 
    # corresponds to index 0)
    if (name == costumer[i][0]):
        # If this condition is true we have found the 
        # correct costumer and we can return their
        # mobile phone number and exit the loop 
        # (the mobile number is element 2 of the child 
        # list which corresponds to index 1)
        print(name + "'s mobile phone number is: " 
              + costumer[i][1])
        break
        
    # Now if the names are not identical we want to 
    # move on to the next name in the list
    # IF there are still names left in it
    elif((name != costumer[i][0]) and ((i+1) < len(costumer))):
        # In this case we can update the counter and 
        # move on to the next iteration
        i += 1
    # However, if the names are not identical and we 
    # have reached the end of our list, we will need 
    # to let the user know that the name they entered
    # is not a valid costumer name and exit the loop
    else:
        print(name + " is not a valid costumer name.")
        break
        

