
# coding: utf-8

# # Solution: Exercise 6.S02

# In[5]:

# Request user input
em = input("Please specify an EM wavelength in nm: ")


# In[6]:

# Convert the input into a float
em = float(em)


# In[10]:

# Check whether the wavelength is visible to humans
if(em < 380 or em > 749):
    # Light is not visible
    print("Wavelentgh {0} nm is not visible to humans.".format(em))
else:
    # Light is visible
    if(em >= 380 and em < 450):
        print("Wavelentgh {0} nm appears violet.".format(em))
    elif(em >= 450 and em < 495):
        print("Wavelentgh {0} nm appears blue.".format(em))
    elif(em >= 495 and em < 570):
        print("Wavelentgh {0} nm appears green.".format(em))
    elif(em >= 570 and em < 590):
        print("Wavelentgh {0} nm appears yellow.".format(em))
    elif(em >= 590 and em < 620):
        print("Wavelentgh {0} nm appears orange.".format(em))
    else:
        print("Wavelentgh {0} nm appears red.".format(em))


# In[ ]:



