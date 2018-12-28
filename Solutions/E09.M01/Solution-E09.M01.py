
# coding: utf-8

# # Solution: Exercise 9.M01

# In[4]:


# Set the filenamne
fileName = "E09.M01_Cities.txt"

# Open the file to write
f = open(fileName, "w")

# Initialize infinite loop
while True:
    # Ask the user for a city
    city = input("Please enter a city or STOP to quit: ")
    
    # Case 1: User has entered STOP
    if(city == "STOP"):
        break
    # Case 2: The user has entered a city
    else:
        # Write to the file
        f.write(city + "\n")
    

# Close the file
f.close()

