
# coding: utf-8

# # Solution: Exercise 9.M07

# ### a) to c)

# In[6]:


# Open the new files:
employeesComplete = open("E09.M07_EmployeesComplete.txt","w")
employeesMissingBDay = open("E09.M07_EmployeesMissingBDay.txt", "w")
employeesRetire = open("E09.M07_EmployeesRetire.txt", "w")


# Add comment lines to files
employeesComplete.write("# List of all employees with "
                        + "complete data"
                        + "\n# Name\tID Number\tBirthday\n")
employeesMissingBDay.write("# List of all employees with "
                           + "incomplete data"
                           + "\n# Name\tID Number\n")
employeesRetire.write("# List of all employees set to "
                      + "retire" 
                      + "\n# Name\tID Number\tBirthday\n")


# Generate a list that will store all employees
employees = []

# Open the file containing all employee data
fileName = "E09.M07_Employees.txt"

try:
    f = open(fileName,"r")
except:
    print("Error! File '" + fileName + "' not found!")
else:
    for line in f:
        # Ignore comment line
        if (line[0] == "#"):
            continue
        else:
            # Count how many tabs are in the line 
            # (if the birthdate is missing, there will 
            # only be one)
            tabs = line.count("\t")
            
            
            # Case 1: Data is complete
            if (tabs == 2):
                # Split line
                Name, ID, Bday = line.split("\t")
                
                # Remove formatting from Bday
                Bday = Bday[:-1]
                
                # Split Bday in day, month and year
                day, month, year = Bday.split(".")

                # Add data to list
                employees.append([Name, ID, day, month, year])
                
                # a) 
                # print name, ID and birthday of every employee 
                # with a complete data set into a new 
                # file E09.M07_EmployeesComplete.txt
                employeesComplete.write(Name + "\t" + ID 
                                        + "\t" + Bday + "\n")
                
                # c) 
                # Check which employees are set to retire soon
                # and add relevant employees to 
                # E09.M07_EmployeesRetire.txt
                current_year = 2018
                if(current_year-int(year)>65):
                    employeesRetire.write(Name + "\t" + ID 
                                          + "\t" + Bday + "\n")
              
            # Case 2: Data is incomplete
            else:
                # Data is incomplete
                Name, ID = line.split("\t")
                
                # Remove formatting from ID
                ID = ID[:-1]
                
                # b) 
                # print name and ID of every employee with an 
                # incomplete data set into a new file 
                # E09.M07_EmployeesMissingBDay.txt
                employeesMissingBDay.write(Name + "\t" + ID 
                                          + "\n")

     
         
# Close the new files
employeesComplete.close()
employeesMissingBDay.close()
employeesRetire.close()


# ### d)

# In[26]:


# Request user input
string = input("Please name a date in the following format dd.mm: ")

# Split string
day, month = string.split(".")


# In[27]:


# List storing all employees whose birthday is on the specified day
bdayEmployees = []

currentYear = "2018"

# Go through the list of employees and check birthday
for i in range(len(employees)):
    # Check if birthday and date are the same
    # (the strip method takes care of leading 0 in the input)
    if(employees[i][2] == day.lstrip("0") 
       and employees[i][3] == month.lstrip("0")):
        
        # Calculate the age of the employee
        age = int(currentYear) - int(employees[i][4])
        
        # Add the employee to the birthday list
        bdayEmployees.append([employees[i][0],age])
    else:
        continue


# In[28]:


# Display output
print("Birthdays on the " + string + ":")

# Case 1: No birthdays
if(len(bdayEmployees) == 0):
    print("\tNo birthdays on thise date.")
else:
    # Loop over all BDay employees
    for i in range(len(bdayEmployees)):
        print("\t- " + bdayEmployees[i][0] + "("
              + str(bdayEmployees[i][1]) + ")")
        


# ### d)

# In[22]:


# Importing the library
import datetime


# In[23]:


# Determine todays date
year, month, day = str(datetime.date.today()).split("-")


# You can now simply copy the code from b)

# In[24]:


# List storing all employees whose birthday is on the specified day
bdayEmployees = []

currentYear = "2018"

# Go through the list of employees and check birthday
for i in range(len(employees)):
    # Check if birthday and date are the same
    # (the strip method takes care of leading 0 in the input)
    if(employees[i][2] == day.lstrip("0") 
       and employees[i][3] == month.lstrip("0")):
        
        # Calculate the age of the employee
        age = int(currentYear) - int(employees[i][4])
        
        # Add the employee to the birthday list
        bdayEmployees.append([employees[i][0],age])
    else:
        continue


# In[25]:


# Display output
print("Birthdays on the " + string + ":")

# Case 1: No birthdays
if(len(bdayEmployees) == 0):
    print("\tNo birthdays on thise date.")
else:
    # Loop over all BDay employees
    for i in range(len(bdayEmployees)):
        print("\t- " + bdayEmployees[i][0] + "("
              + str(bdayEmployees[i][1]) + ")")
        


# ### f)

# In[32]:


# Loop over all employees in bday_employees
for i in range(len(bdayEmployees)):
    # Save employee information
    firstName, lastName = bdayEmployees[i][0].split(" ")
    
    # Open a file
    f = open("E09.M07_BDWishes-" + firstName + lastName + ".txt ","w")
    
    # Print birthday message
    f.write("\nDear " + firstName + "\n\nHappy Birthday!"
            + "\n\nBest wishes,\nYour colleagues.")
    
    # Close the file again
    f.close()

