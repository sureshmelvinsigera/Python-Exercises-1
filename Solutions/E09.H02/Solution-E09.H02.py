
# coding: utf-8

# # Solution: Exercise 9.H02

# ### a)

# In[5]:


# Import the numpy library
import numpy as np


# Set initial parameters:
# -----------------------

# Throw velocity in m/s
v0 = 10

# Gravitational constant in m/s**2
gravity =  9.81

# File name
fileName = "E09.H02_ThrowIn.txt"

# Open file
f = open(fileName,"w")
f.write("# angle (rad)\tangle (deg)\trange (m)\n")


# Loop over all angles between 0 degrees (0 rad) and 
# 90 degrees (pi/2 rad)
for angle in np.arange(0, np.pi/2.0,0.01):
    
    # Calculate angel in degrees
    angleDeg = angle * 360 / (2 * np.pi)
    
    # Calculate the velocities in x- and y-direction in m/s
    vx = v0 * np.cos(angle)
    vy = v0 * np.sin(angle)

    # Starting time
    t = 0
    
    # Calculate how many seconds it will take for the ball 
    # to hit the ground
    t = 2 * v0 * np.sin(angle)/gravity
        
    # Calculate how far the ball will fly in time t in m
    rangeBall = vx * t

    # Write results into file
    f.write("{0:.4f}\t{1:.4f}\t{2:.4f}\n".format(angle,angleDeg,rangeBall))
    
# Close file again
f.close()


# ### b)

# In[6]:


# Open file
try:
    f = open(fileName,"r")
except:
    print("Error! File '" + fileName + "' not found!")
else:
    # Initialize maximum variables
    rangeMax = 0.0
    angleMax = 0.0
    
    for line in f:
        if(line[0] != "#"):
            angleRad, angleDeg, rangeBall = line.split("\t")
            
            # Check whether new maximum value found
            if(float(rangeBall) > rangeMax):
                rangeMax = float(rangeBall)
                angleMax = float(angleDeg)
            
    print("The maximum range of {0:.2f} meters is achieved by throwing the ball at an angle of {1:.2f} degrees.".format(rangeMax,angleMax))
    
    # Close file
    f.close()


# ### c)

# In[7]:


# Importing the graphics library
import  matplotlib.pyplot as plt

try:
    f = open(fileName,"r")
except:
    print("Error! File '" + fileName + "' not found!")
else:
    # Initialize maximum variables
    angleRad = []
    angleDeg = []
    rangeBall = []
    
    for line in f:
        if(line[0] != "#"):
            angleRadFile, angleDegFile, rangeBallFile = line.split("\t")
            
            angleRad.append(float(angleRadFile))
            angleDeg.append(float(angleDegFile))
            rangeBall.append(float(rangeBallFile))

    
    # Title of plot
    plt.title("Throw-in")
    
    # Axis labels
    plt.xlabel('alpha [deg]')
    plt.ylabel('range [m]')
    
    # Plot range versus angle [deg]
    plt.plot(angleDeg,rangeBall)
    plt.show()
            
            
    # Close file
    f.close()

