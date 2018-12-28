
# coding: utf-8

# # Solution: Exercise 9.M06

# In[28]:


# Request user input
reference = input("Please enter your 6 digit reference number: ")

# Convert the reference from a string to an integer
reference = int(reference)
    


# In[29]:


# Set the file name
fileName = "E09.M06_DeliveryReferenceNumbers.txt"

try:
    f = open(fileName,"r")
except:
    print("Error! File '" + fileName + "' not found!")
else:
    # List for all reference numbers
    refNumber = []

    # Read in the delivery references
    for line in f:
        # Case 1: Data line
        if (line[0] != "#"):
            refNumber.append(int(line))
        # Case 2: Comment line starting with a #
        else:
            # Skip to next line
            continue


    # Check whether reference number is valid
    if(reference not in refNumber):
        # The reference number not in list
        print("Sorry, the reference number you " 
              + "provided is not valid.")
    else:
        # Calculate the delivery number which is the index of the
        # delivery reference plus 1
        deliveryNumber = refNumber.index(reference) + 1
        
        # Calculate the minimum amount of time it will take 
        # for the parcel to be delivered (assuming every delivery
        # before will take 5 minutes)
        minDelivery = deliveryNumber * 5
        
        # And convert it into hours and minutes
        minDeliveryHM = [minDelivery//60,minDelivery%60]
        
        # Calculate the minimum amount of time it will take 
        # for the parcel to be delivered (assuming every delivery
        # before will take 15 minutes)
        maxDelivery = deliveryNumber * 15
        
        # And convert it into hours and minutes
        maxDeliveryHM = [maxDelivery//60,maxDelivery%60]
        
        # Set time of delivery driver leaving the depot
        startTime = 9    

        # Display an estimated delivery timeslot:
        print("Your parcel will be delivered between "
              + str(startTime+minDeliveryHM[0]) + ":"
              + str(minDeliveryHM[1]) + " and " 
              + str(startTime+maxDeliveryHM[0]) + ":"
              + str(maxDeliveryHM[1]))
   


