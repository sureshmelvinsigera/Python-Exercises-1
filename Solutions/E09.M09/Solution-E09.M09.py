
# coding: utf-8

# # Solution: Exercise 9.M08

# In[8]:


# Set the filenamne
fileName = "E09.M09_WorldPopulation.txt"

try:
    # Open the file to write
    f = open(fileName, "r")
except:
    print("Error! File '" + fileName + "' not found!")
else:
    # Declare data lists
    year = []
    population = []
    
    # Loop over every line in the file
    for line in f:
        # Ignore comment line
        if(line[0] == "#"):
            continue
        else:
            data = line.split()
            
            # Append data to lists
            year.append(int(data[0]))
            population.append(float(data[1]))
    

# Close the file
f.close()


# Find index of first population above one billion (1,000,000,000)

# In[9]:


# Initialize counter 
index = 0

while (index < len(population)):
    if(population[index] > 1000000000):
        break
    else:
        # Update counter
        index += 1

# Determine the corresponding year
year1Billion = year[index]

# Display result
print("The human population of Earth surpassed 1 billion in "
      + "the year " + str(year1Billion))

