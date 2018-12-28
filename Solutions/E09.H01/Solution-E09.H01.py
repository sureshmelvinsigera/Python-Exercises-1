
# coding: utf-8

# # Solution: Exercise 9.H01

# In[1]:


# Importing the random library
import random


# In[2]:


# Store the hangman visualisations
hangman = []
hangman.append("\n\n\n\n\n\n\n\n\n\n\t---------------\n")
hangman.append("\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t---------------\n")
hangman.append("\t|/\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t---------------\n")
hangman.append("\t---------\n\t|/\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t---------------\n")
hangman.append("\t---------\n\t|/      |\n\t|       |\n\t|       \n\t|     \n\t|       \n\t|      \n\t|      \n\t|    \n\t|\n\t---------------\n")
hangman.append("\t---------\n\t|/      |\n\t|       |\n\t|       O\n\t|     \n\t|       \n\t|      \n\t|      \n\t|  \n\t|\n\t---------------\n")
hangman.append("\t---------\n\t|/      |\n\t|       |\n\t|       O\n\t|       |\n\t|       |\n\t|       \n\t|     \n\t|    \n\t|\n\t---------------\n")
hangman.append("\t---------\n\t|/      |\n\t|       |\n\t|       O\n\t|     _/|\n\t|       |\n\t|       \n\t|      \n\t|    \n\t|\n\t---------------\n")
hangman.append("\t---------\n\t|/      |\n\t|       |\n\t|       O\n\t|     _/|\_\n\t|       |\n\t|       \n\t|      \n\t|    \n\t|\n\t---------------\n")
hangman.append("\t---------\n\t|/      |\n\t|       |\n\t|       O\n\t|     _/|\_\n\t|       |\n\t|      /  \n\t|     /    \n\t|    -     \n\t|\n\t---------------\n")
hangman.append("\t---------\n\t|/      |\n\t|       |\n\t|       O\n\t|     _/|\_\n\t|       |\n\t|      / \ \n\t|     /   \ \n\t|    -     -\n\t|\n\t---------------\n")


# In[3]:


# Wrapper for the game

while True:
    
    # Specify the file name containing the word list
    # The file containing a list of word is available for 
    # download on github: 
    # https://github.com/jesstess/Scrabble/blob/master/scrabble/sowpods.txt
    fileName = "E09.H01_sowpods.txt "

    # Open the file
    try:
        f = open(fileName,"r")
    except:
        print("Error! File '" + fileName + "' not found!")
    else:
        wordList = []
        # Loop over all lines and store them in a word list1
        for line in f:
            # Append the word after removing the formatting
            wordList.append(line[:-1])
    
        #Close the file again
        f.close()
    
        # Chose a word at random
        randNum = int(random.random() * len(wordList))
        word = wordList[randNum]
    
        # Generate list containing the correctly guessed letters
        wordGuess = ["_" for i in range(0,len(word))]
    
        # Count the number of incorrect guesses:
        incorrGuessN = 0
    
        # Set the number of incorrect guesses allowed
        incorrGuessMax = 11
    
        # Variable containing all incorrectly guessed letters
        incorrGuess = []
    
    
        # Start the guessing loop
        while True:
        
            
            # Display the word
            print("\nI'm thinking of the following word: ")
            # Print the word again this time with the letter 
            # added 
            for l in wordGuess:
                print(l,end=" ")
        
            # Ask the user for a guess
            letter = input("\nPlease guess a letter: ").upper()
        
        
            # Letter has been guessed correctly and for the 
            # first time
            if((letter in word) and (letter not in wordGuess)):
                print("Correct! '{0}' is part of the word I'm thinking off.".format(letter))
            
                # Add the new word to the list of correctly guessed 
                # letters
                for i in range(0,len(word)):
                    if (word[i] == letter):
                        wordGuess[i] = letter
                    else:
                        continue
            
                # Check whether the entire word has been guessed
                if("_" not in wordGuess):
                    print("\nCongratulations you have guessed the word and won the game!")
                    for l in wordGuess:
                        print(l,end=" ")
                    break
            
            
            # Letter has been guessed correctly or incorrectly but 
            # not for the first time
            elif((letter in word) and (letter in wordGuess) 
                 or (letter not in word) and (letter in incorrGuess)):
                if (letter in word):
                    print("\nCorrect, but you have guessed this letter already!")          
                else:
                    print("\nIncorrect, but you have guessed this letter already!")
            
            # Letter has not been guessed correctly
            else:
                # Print message and tell user how many guesses 
                # they have left 
                #print("'{0}' is not part of the word I'm thinking off.\nYou have {1} guesses left.".format(letter, incorr_guess_max - incorr_guess_n))
            
                # Print message and display hangman figure
                print("'{0}' is not part of the word I'm thinking off.\n".format(letter))
                print(hangman[incorrGuessN])
            
                # Add letter to list of incorrectly guessed 
                # letters
                incorrGuess.append(letter)
            
                # Update the number of incorrect guesses:
                incorrGuessN += 1 
        
                # Too many incorrect guesses
                if(incorrGuessN >= incorrGuessMax):
                    print("You lost :( The word I was looking for was: '{0}'.".format(word))
                    break
                    
    # Ask user if they want to play another game:
    anotherRound = input("\n\nWould you like to play again (y/n)? ")
    if(anotherRound == "y"):
        continue
    else:
        break
        
    
    

