
# coding: utf-8

# # Solution: Exercise 9.M08

# In[3]:


# Set the file name of the murderer DNS
murdererFile = "E09.M08_DNA-Murderer.dat"


try:
    murderer = open(murdererFile,"r")
except:
    print("Error! File '" + murdererFile + "' not found!")
else:
    for line in murderer:
        # Store the DNA in a string
        dnaMurderer = line
        

# Now loop over all other DNA samples
for i in range(1,50):
    suspectFile = "E09.M08_DNA-Suspect{num:04d}.dat".format(num=i)
    
    try:
        suspect = open(suspectFile,"r")
    except:
        print("Error! File '" + suspectFile + "' not found!")
    else:
        for line in suspect:
            # Store the dna in a string
            dnaSuspect = line
            
    if (dnaSuspect == dnaMurderer):
        break
        

# Produce the output
print("Suspect number " + str(i) + " is the murderer!")   
    

