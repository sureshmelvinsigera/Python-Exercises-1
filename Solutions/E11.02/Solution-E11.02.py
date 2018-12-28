
# coding: utf-8

# # Solution: Exercise 10.07

# In[3]:


class Vehicle:
    
    # Class Attributes:
    mValue = 0
    
    
    # The __init__() Method:
    def __init__(self, value):
        self.mValue = value       
        
        
    # Setters:       
    def SetValue(self, value):
        self.mValue = value

        
    # Getters:
    def GetValue(self):
        return self.mValue


# In[8]:


class Car(Vehicle):
    
    # Attributes 
    mBrand = ""
    
    # __init__():
    def __init__(self, value, brand):
        
        # Call the __init__() function of the parent class
        super().__init__(value)
        
        # Set the ID attribute
        self.mBrand = brand
        
    # Setters:   
    def SetBrand(self, brand):
        # Change the course list
        self.mBrand = brand
              
    # Getters:
    def GetBrand(self):
        # Return the course list
        return self.mBrand


# In[10]:


class Bicycle(Vehicle):
    
    # Attributes 
    mColour = ""
    
    # __init__():
    def __init__(self, value, colour):
        
        # Call the __init__() function of the parent class
        super().__init__(value)
        
        # Set the ID attribute
        self.mColour = colour
        
    # Setters:   
    def SetColour(self, colour):
        # Change the course list
        self.mColour = colour
              
    # Getters:
    def GetColour(self):
        # Return the course list
        return self.mColour


# In[13]:


# Initialize a car
car1 = Car(6000, "Ford")

# Extract Value
print(car1.GetValue())

# Extract Brand
print(car1.GetBrand())


# In[14]:


# Initialize a bicycle
bike1 = Bicycle(600, "green")

# Extract Value
print(bike1.GetValue())

# Extract Brand
print(bike1.GetColour())

