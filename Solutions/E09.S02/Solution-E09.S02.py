
# coding: utf-8

# # Solution: Exercise 9.E02

# In[19]:


# Set the file name
fileName = "E09.S02_SN2005ek.txt "

# Open the file 
f = open(fileName, "r")

# Initialize data variables
wavelength = []
fluxDensity = []

# Loop over ever line in the file
for line in f:
    # Split the line 
    data = line.split()
    
    # Store the data in the respective lists
    wavelength.append(float(data[0]))
    fluxDensity.append(float(data[1]))
    

# Close the file
f.close()


# Plotting is not covered in this course but below code fragement will generate a plot so you can see what the data actually looks like:m

# In[20]:


import matplotlib.pyplot as plt

plt.plot(wavelength, fluxDensity)
plt.xlabel("Wavelength [in Angstrom]")
plt.ylabel("Flux Density")

plt.show()


# In[23]:


# Determine the maximum in a list
maximumFluxDensity = max(fluxDensity)

# Find the corresponding index to the maximum flux density
maximumIndex = fluxDensity.index(maximumFluxDensity)

# Determine the corresponding wavelength
maximumWavelength = wavelength[maximumIndex]


# In[25]:


# Display results
print("The flux density maximum is at wavelength " 
      + str(maximumWavelength))

