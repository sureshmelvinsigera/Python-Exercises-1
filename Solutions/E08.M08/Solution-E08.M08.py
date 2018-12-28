
# coding: utf-8

# # Solution: Exercise 8.M08

# ### a)

# In[1]:


# Set a number to be guessed
number = 4


# In[2]:


# Set the number of allowed tries to 3
tries = 3

# Initialize a counter
counter = 0

# Initialize a winner variable (default: computer
winner = "computer"

# Initialize a WHILE loop
while (counter < tries):
    # Ask the user for a number
    userGuess = input("Guess a number: ")
    
    # Convert the input into an integer
    userGuess = int(userGuess)
    
    # Case 1: The user has guessed correctly
    if(userGuess == number):
        # Update the winner
        winner = "user"
        
        # Terminate the loop
        break
    # Case 2: The user has not guessed correctly
    else:
        # Update the counter
        counter += 1   
        
        # Tell the user how many guesses they have left
        if(counter < tries):
            print("That's not the number I'm looking for." 
                  + " Try again.")
        else:
            print("That's not the number I'm looking for." 
                  + " No more attempts left.")
            
# Display the winner
print("The winner is: " + winner)


# ### b)

# In[6]:


# Set a number to be guessed
number = 677


# In[8]:


# Set a counter for the number of guesses the user has made
guesses = 1

# Initialize an infinite WHILE loop
while True:
# Ask the user for a number
    userGuess = input("Guess a number: ")
    
    # Convert the input into an integer
    userGuess = int(userGuess)
    
    # Case 1: The user has guessed correctly
    if(userGuess == number):       
        # Terminate the loop
        break
    # Case 2: The user has not guessed correctly
    else:
        # Update the counter
        guesses += 1   
        
        # Case 1: The guessed number was smaller than the
        # actual number
        if(userGuess < number):
            print("Incorrect." 
                  + " I'm looking for a larger number." 
                  + " Try again.")
        # Case 2: The guessed number was larger then the
        # actual number
        else:
            print("Incorrect." 
                  + " I'm looking for a smaller number." 
                  + " Try again.")
            
# Display the number of guesses it took the user
print("It took you " + str(guesses) 
      + " tries to guess the correct number!")

