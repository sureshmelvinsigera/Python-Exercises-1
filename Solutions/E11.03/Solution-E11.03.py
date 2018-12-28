
# coding: utf-8

# # Solution: Exercise 10.08

# In[20]:


class Complex:
    
    # Attributes
    mReal = 0
    mImaginary = 0
    
    # The __init__() Method:
    def __init__(self, real, imag):
        self.mReal = real  
        self.mImaginary = imag
        
    # Setters: 
    def SetReal(self, real):
        self.mReal = real
        
    def SetImaginary(self, imag):
        self.mImaginary = imag
            
    # Getters:
    def GetReal(self):
        return self.mReal
        
    def GetImaginary(self):
        return self.mImaginary
    
    
    # Misc. Function
    
    # Display the imaginary numbers
    def DisplayImaginaryNumber(self):
        print(str(self.mReal) + " + i * " + str(self.mImaginary))
    
    # Add two number together
    def AddImaginaryNumbers(self, imagNumber):
        # Calculate the real part of the number
        real = self.mReal + imagNumber.GetReal()
        
        # Calculate the imaginary part of the number
        imag = self.mImaginary + imagNumber.GetImaginary()
        
        # Generate the new object
        imagSum = Complex(real,imag)
        
        # Return result
        return imagSum
    
    # Subtract two numbers
    def SubtractImaginaryNumbers(self, imagNumber):
        # Calculate the real part of the number
        real = self.mReal - imagNumber.GetReal()
        
        # Calculate the imaginary part of the number
        imag = self.mImaginary - imagNumber.GetImaginary()
        
        # Generate the new object
        imagSub = Complex(real,imag)
        
        # Return result
        return imagSub
        


# In[21]:


# Intialize two imagine numbers
num1 = Complex(1,2)
num2 = Complex(3,4)


# In[22]:


# Add the numbers together
num3 = num1.AddImaginaryNumbers(num2)

# Display number
num3.DisplayImaginaryNumber()


# In[23]:


# Subtract the numbers 
num4 = num1.SubtractImaginaryNumbers(num2)

# Display number
num4.DisplayImaginaryNumber()

