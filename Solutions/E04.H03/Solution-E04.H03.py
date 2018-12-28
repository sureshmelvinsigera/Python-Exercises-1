
# coding: utf-8

# # Solution: Exercise 4.H03

# Initialize the variables
# (distances are in meters, velocities in meters per s)

# In[1]:

# Set the initial position of the swimmer
xStart = 0
yStart = 5

# Set the velocity of the swimmer in x-direction
vxSwimmer = 0.5

# Set the velocity of the water in y-direction
vyWater = 1.0

# Set the width of the river
widthRiver = 10


# #### Step 1:
# 
# Calculate how long it will take the swimmer to cross the river. Given a distance s and a velocity v, the time can be calculated via:
# 
# \begin{equation} t = s / v \end{equation}

# In[2]:

crossingTime = widthRiver / vxSwimmer


# #### Step 2:
# 
# We now know how long the swimmer is in the water. Therefore we are able to calculate how far the river will carry the swimmer downstream over that periode of time.
# 
# Given a time t and a velocity v the distance traveled can be calculated via:
# \begin{equation} s = v \cdot  t\end{equation}

# In[3]:

deltaY = vyWater * crossingTime


# #### Step 3:
# 
# Now we can calculate the position at which the swimmer will emerge from the river. 
# 
# The new x-position will be the initial position plus the width of the river:
# 
#    \begin{equation} x_{End} = x_{Start} + w\end{equation}
#    
# The new y-position will be the initial position minus the distance the swimmer has been carried downstream:
# 
#    \begin{equation} y_{End} = y_{Start} - delta_y \end{equation}

# In[4]:

# Calculate the new x-position
xEnd = xStart + widthRiver

# Calculate the new y-position
yEnd = yStart - deltaY


# #### Step 4:
# 
# Let's display the result.

# In[6]:

print("The swimmer will emerge at position (" + str(xEnd)  + ", " + str(yEnd) + ")")


# Or using the format function:

# In[8]:

print("The swimmer will emerge at position ({0}, {1})".format(xEnd,yEnd))


# In[ ]:



