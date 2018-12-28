
# coding: utf-8

# # Solution: Exercise 10.06

# In[14]:


class Dog:
    
    # Class Attributes:
    mName = ""
    mAge = 0
    mBreed = ""
    
    
    # The __init__() Method:
    def __init__(self, name, age, breed):
        self.mName = name
        self.mAge = age
        self.mBreed = breed
        
        
        
    # Setters: 
    def SetName(self, name):
        self.mName = name
        
    def SetAge(self, age):
        self.mAge = age
        
    def SetBreed(self, breed):
        self.mBreed = breed
        
        
    # Getters:
    def GetName(self):
        return self.mName
        
    def GetAge(self):
        return self.mAge
        
    def GetBreed(self):
        return self.mBreed
    
    
    # Misc. Functions:
    def DisplayInformation(self):
        print(self.mName + " is " + str(self.mAge) 
              + " years old and a " + self.mBreed + ".")


# In[15]:


# Intialize a test object
dog1 = Dog("Pluto", 3, "Corgi")


# In[16]:


# Display information
dog1.DisplayInformation()

