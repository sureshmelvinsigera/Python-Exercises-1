
# coding: utf-8

# # Solution: Exercise 6.H02

# In[8]:

# Request a square identifier from the user
squareID = input("Please enter a square identifier: ")


# The trick here is to figure out a way to correlate the square ID to the number. So you will need to find a pattern.

# From considering the board we can make the following observations:
# 
# - A cell is white if
#     - squareID[0] is odd and squareID[1] is a, c, e, or g
#     - squareID[0] is even and squareID[1] is b, d, f, h
#     
#     
# - A cell is black if
#     - squareID[0] is even and squareID[1] is a, c, e, or g
#     - squareID[0] is odd and squareID[1] is b, d, f, h

# In[9]:

# Case 1: squareID[0] is odd
if(int(squareID[0]) % 2 != 0):
    
    # Case 1.1: squareID[1] is a, c, e, or g
    if(squareID[1] in "aceg"):
        # Display result
        print("Cell " + squareID + " is white.")
        
    # Case 1.2: squareID[1] is b, d, f, h
    else:
        # Display result
        print("Cell " + squareID + " is black.")
        
# Case 2: squareID[0] is even
else:
    
    # Case 2.1: squareID[1] is a, c, e, or g
    if(squareID[1] in "aceg"):
        # Display result
        print("Cell " + squareID + " is black.")
        
    # Case 2.2: squareID[1] is b, d, f, h
    else:
        # Display result
        print("Cell " + squareID + " is white.")


# ## Bonus

# It's always a good idea to make sure your code can catch invalid input before it crashes. Let's rewrite above code but this time we will make sure no invalid square identifiers are passed to the main <b>IF</b> and <b>ELSE</b> Statment.

# In[23]:

# Request a square identifier from the user
squareID = input("Please enter a square identifier: ")


# In[24]:

# Let's make sure the input contains exactly two characters
if(len(squareID) != 2):
    # Display error
    print("Error: This is not a valid square ID!")

# Let's make sure the first character in the input is a number and the 
# second is a letter
elif(not squareID[0].isnumeric() or squareID[1].isnumeric()):
    # Display error
    print("Error: This is not a valid square ID!")
    
# Let's make sure the ID does not exceed the board vertically
elif(int(squareID[0]) > 8 or int(squareID[0]) < 0):
    # Display error
    print("Error: This is not a valid square ID!")
    
# Let's make sure the ID does not exceed the board horizontally
elif(squareID[1] not in "abcdefgh"):
    # Display error
    print("Error: This is not a valid square ID!")

# If no case above is triggered we can be sure the input was valid
# and we can proceed with the actual task of determining the square
# colour
else:
    if(int(squareID[0]) % 2 != 0):
    
        # Case 1.1: squareID[1] is a, c, e, or g
        if(squareID[1] in "aceg"):
            # Display result
            print("Cell " + squareID + " is white.")
        
        # Case 1.2: squareID[1] is b, d, f, h
        else:
            # Display result
            print("Cell " + squareID + " is black.")
        
    # Case 2: squareID[0] is even
    else:
    
        # Case 2.1: squareID[1] is a, c, e, or g
        if(squareID[1] in "aceg"):
            # Display result
            print("Cell " + squareID + " is black.")
        
        # Case 2.2: squareID[1] is b, d, f, h
        else:
            # Display result
            print("Cell " + squareID + " is white.")


# In[ ]:



