
# coding: utf-8

# # Solution: Exercise 6.M01

# In[1]:

# Set the account balance
accountBalance = 100


# In[13]:

# Ask the user how much money they want to withdraw
withdrawl = input("How much money would you like to withdraw? ")


# In[14]:

# Convert the input into a float
withdrawl = float(withdrawl)


# In[15]:

# Calculate the potential new account balance after the withdrawl
newAccountBalance = accountBalance - withdrawl


# In[16]:

# Case 1: New balance would be positive -> Transaction allowed
if(newAccountBalance >= 0):
    # Update account balance
    accountBalance = newAccountBalance
    
    # Display message
    print("Transaction successfull. Your new balance is: {0}".
              format(newAccountBalance))

# Default: New balance would be negative -> Transaction forbidden  
else:
    # The account balance is negative after the withdrawl
    print("Transaction not possible. Not enough funds.")


# In[ ]:



