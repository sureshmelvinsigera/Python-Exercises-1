
# coding: utf-8

# # Solution: Exercise 8.M10

# In[25]:


# Ask the user to give you a three digit pin code:
password = input("Please enter a three digit pin code: ")


# In[26]:


# Generate the list containing possible pin code numbers:
listNumbers = ["1", "2", "3", "4", "5", 
               "6", "7", "8", "9", "0"]


# Define counters:
counterD1 = 0
counterD2 = 0
counterD3 = 0

# Loop over all possibilities for digit1
while (counterD1 < len(listNumbers)):
    
    # Set the first digit equal to listNumbers[counterD1]
    digit1 = listNumbers[counterD1]
    
    # Loop over all posibilities for digit2
    while(counterD2 < len(listNumbers)):
        # Set the second digit equal to 
        # listNumbers[counterD2]
        digit2 = listNumbers[counterD2]
        
        
        # Loop over all possibilities for digit3
        while(counterD3 < len(listNumbers)):
            # Set the third digit equal to 
            # listNumbers[counterD3]
            digit3 = listNumbers[counterD3]
            
            # Generate the pin
            pin = str(digit1) + str(digit2) + str(digit3)
            
            # Case 1: Pin is correct
            if (pin == password):
                # Exit loop
                break
            # Case 2: Pin incorrect:
            else:
                # Update counter for digit 3
                counterD3 += 1               
                continue
        
        # Check if pin has been found
        if (pin == password):
            # Exit loop
            break
        # Case 2: Pin incorrect:
        else:
            # Reset counter for digit 2
            counterD3 = 0                
        
            # Update counter for digit 2
            counterD2 += 1
            
    # Check if pin has been found
    if (pin == password):
        # Exit loop
        break
    # Case 2: Pin incorrect:
    else:
        # Reset counter for digit 2
        counterD2 = 0
    
        # Update counter for digit 1
        counterD1 += 1


# In[27]:


# Display pin
print("Your pin is: " + pin)

