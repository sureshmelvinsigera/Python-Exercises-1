
# coding: utf-8

# # Solution: Exercise 6.S01

# In[16]:

# Request user input
percentage = input("Please enter the percentage of points achieved: ")


# In[17]:

# Convert the input into a number
percentage = int(percentage)


# In[18]:

# Case 1: Student will receive grade A
if((percentage >= 90)):
    print("The student receives grade A")
    
# Case 2: Student will receive grade B
elif((percentage >= 70) and (percentage < 90)):
    print("The student receives grade B")
    
# Case 3: Student will receive grade C
elif((percentage >= 60) and (percentage < 70)):
    print("The student receives grade C")
    
# Case 4: Student will receive grade D
elif((percentage >= 50) and (percentage < 60)):
    print("The student receives grade D")
    
# Case 5: Student has failed
else:
    print("The student has failed the exam")


# In[ ]:




# In[ ]:



