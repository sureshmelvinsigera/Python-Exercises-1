
# coding: utf-8

# # Solution: Exercise 3.M06

# In[3]:

# Initialize the data sets
data1 = "Harry Potter 1980"
data2 = "Hermione Granger 1979"
data3 = "Ron Weasley 1980"


# ### Data set 1

# In[21]:

# Find the position of first space
indexSpace1 = data1.find(" ")

# Generate a substring containing the first name 
nameFirst = data1[0:indexSpace1]

# Store the remainder of the string in a temporary variable
stringTMP = data1[indexSpace1:]

# Remove any leading spaces
stringTMP = stringTMP.strip()

# Find the position of first space in this new string (which is actually 
# the second space in the original string)
indexSpace2 = stringTMP.find(" ")

# Generate a substring containing the last name 
nameLast = stringTMP[:indexSpace2]

# Store the remainder (which is the year of birth) in a final variable
year = stringTMP[indexSpace2:]

# Convert the year string into an integer
year = int(year)

# Calculate the age of the person
age = 2018 - year

# Display the result:
print(nameFirst + " " + nameLast + " is " + str(age) + " years old.")


# We can now repeat this action for every dataset by copying the entire code and only changing the name of the data set.
# 
# ### Data set 2

# In[23]:

# Find the position of first space
indexSpace1 = data2.find(" ")

# Generate a substring containing the first name 
nameFirst = data2[0:indexSpace1]

# Store the remainder of the string in a temporary variable
stringTMP = data2[indexSpace1:]

# Remove any leading spaces
stringTMP = stringTMP.strip()

# Find the position of first space in this new string (which is actually the 
# second space in the original string)
indexSpace2 = stringTMP.find(" ")

# Generate a substring containing the last name 
nameLast = stringTMP[:indexSpace2]

# Store the remainder (which is the year of birth) in a final variable
year = stringTMP[indexSpace2:]

# Convert the year string into an integer
year = int(year)

# Calculate the age of the person
age = 2018 - year

# Display the result:
print(nameFirst + " " + nameLast + " is " + str(age) + " years old.")


# Instead of searching for the first space, generating substrings and searching for the next space you can search for the second space straight away with a more complex command:
# 
# str.find("x",i)
# 
# will search for index of x in string str starting at index i.
# 
# Many (string) operators have additional optional arguments that can make your life much easier. It's always a good idea to read the short description of the operator in the Python Standard Library to make sure you're not making life unnecessarily difficult for yourself.

# ### Data set 3

# In[43]:

# Find the position of second blank
indexSpace2 = data3.find(" ",data3.find(" ")+1)

# Extract the complete name
name = data3[0:indexSpace2]

# Extract the year
year = int(data3[indexSpace2:])

# Calculate the age
age = 2018 - year

# Display result
print(name + " is " + str(age) + " years old.")


# ### Remarks on writing your own functions

# We have now written a program that can be applied to all possible data sets as long as they follow the same format. This is the first step of abstraction. No matter which name and birthday configuration you are given you can simply recycle the code you've already written to determine the person's age. The next step would be turning this code into your own function. Then you only need to write it once and after that you can simply call it over and over again.
# 
# Functions are not covered in this course but below you can find an example of how functions could be used in this exercise. Have a look at it towards the end/ after the course if you are interested in continuing with Python.

# In[44]:

# Generate a function that determines the age of a person from a date set of 
# the following format: FirstName LastName YearOfBirth

def CalculateAge(dataset):
   # Find the position of second blank
    indexSpace2 = dataset.find(" ",dataset.find(" ")+1)

    # Extract the complete name
    name = dataset[0:indexSpace2]

    # Extract the year
    year = int(dataset[indexSpace2:])

    # Calculate the age
    age = 2018 - year

    # Display result
    print(name + " is " + str(age) + " years old.")
 


# Now that we have defined a function called CalculateAge() we can apply it to our data sets:

# In[45]:

# Use function on data set 1:
CalculateAge(data1)


# In[47]:

# Use function on data set 2:
CalculateAge(data2)


# In[48]:

# Use function on data set 3:
CalculateAge(data3)


# In[ ]:



