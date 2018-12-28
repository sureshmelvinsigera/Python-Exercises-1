
# coding: utf-8

# # Solution: Exercise 3.S02

# In[1]:

# Set a couple of email adresses
email1 = "12345678@hogwarts.ac.uk"
email2 = "87654321@hogwarts.ac.uk"
email3 = "00100100@hogwarts.ac.uk"


# ### Email1

# In[3]:

# Determine the index of the @ symbol
indexAt = email1.find("@")

# Generate a substring containing all characters from the beginning
# of the original string up to but excluding the @
studentNumber = email1[0:indexAt]

# Display the result
print(studentNumber)


# ### Email2

# In[5]:

# Determine the index of the @ symbol
indexAt = email2.find("@")

# Generate a substring containing all characters from the beginning
# of the original string up to but excluding the @
studentNumber = email2[0:indexAt]

# Display the result
print(studentNumber)


# ### Email3

# In[6]:

# Determine the index of the @ symbol
indexAt = email3.find("@")

# Generate a substring containing all characters from the beginning
# of the original string up to but excluding the @
studentNumber = email3[0:indexAt]

# Display the result
print(studentNumber)


# ### Bonus: Writing your own function

# This course will not cover functions. Have a look at this after the course ends if you want to continue Python and would like to see how functions can be used to simplify some of the exercises you have worked on during the past few weeks.

# In[7]:

# Define a function that extracts the student number from an email
# address of the following format: studentNumber@hogwarts.ac.uk

def FindStudentNumber(email):
    # Determine the index of the @ symbol
    indexAt = email.find("@")

    # Generate a substring containing all characters from the 
    # beginning of the original string up to but excluding the @
    studentNumber = email[0:indexAt]

    # Display the result
    print(studentNumber)


# In[9]:

# Test the function with email address 1
FindStudentNumber(email1)


# In[10]:

# Test the function with email address 2
FindStudentNumber(email2)


# In[11]:

# Test the function with email address 3
FindStudentNumber(email3)


# In[ ]:



