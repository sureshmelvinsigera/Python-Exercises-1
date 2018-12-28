
# coding: utf-8

# # Solution: Exercise 8.M11

# In[3]:


# This is a list containing all the students in the class
studentList = ["Oliver", "Harry", "George", "Jack", 
               "Jacob", "Olivia", "Amelia", "Emily", 
               "Isla", "Ava"]


# This list will contain all possible pairs
studentPairs = []

# The first for loop will loop over every single
# member of our class
for i in studentList:
    
    # Let's set the name of the first member of 
    # the student pair equal to the value currently 
    # stored in our looping variable
    student1 = i
    
    # Now the second loop will also loop over all 
    # students in our class EXCEPT the student that 
    # has already been determined to be part of this 
    # particular pair, in other words: student1.
    # (Note how our looping variable is now j not i!
    # You can never use the same looping variable for 
    # two looping conditions within the same loop block.)
    for j in studentList:
        # First let's make sure that we're not trying 
        # to pair up a student with themselves
        if (i != j):
            # If i and j are not equal we can be sure 
            # that i and j are two different students 
            # and we can form a pair. So we will set
            # student2 equal to j...
            student2 = j
            
            # Let's make sure we haven't already added 
            # this pair to the list that will eventually
            # contain all possible combinations of students
            pairReverse = student2 + " and " + student1
            if pairReverse in studentPairs:
                # In this case we have already added this 
                # specific pair of students to the list 
                # so we can go straight to the next 
                # iteration
                continue
            
            # If we haven't added the pair yet we can append 
            # the group to our list 
            pair = student1 + " and " + student2
            studentPairs.append(pair)
        else:
            # If i and j are equal we know we can skip 
            # this step because a student cannot be 
            # paired with themselves. So, we use the
            # continue command to advance to the next 
            # iteration of j
            continue
            
            
    # The next iteration of i begins AFTER the 
    # j loop has finished!
    
    
    
            
# We can now print all possible pair constellations:
print("Possible pair constellations:")
for i in studentPairs:
    print("\t- " + i)

# And finally we can count how many combinations 
# there are in total
print("\nThere are " + str(len(studentPairs)) + 
      " possible combinations in total.")

