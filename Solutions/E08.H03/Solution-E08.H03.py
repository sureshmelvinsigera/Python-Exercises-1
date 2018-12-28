
# coding: utf-8

# # Solution: Exercise 8.H03

# In[ ]:


from matrixOperations import matrixPrint


# ### a) Matrix-Number Multiplication

# In[2]:


# Initialize a test matrix
M1 = [[5, 6, 1], [7, 8, 1],[9, 10, 4], [11, 12, 1]]

# Display the original matrix
print("Original matrix:")
matrixPrint(M1)

# Define number you want to multiply the matrix with
num = 4

# Loop over the row
for i in range(0,len(M1)):
    # Loop over all columns
    for j in range(0,len(M1[0])):
        # Multiply each element by the number
        M1[i][j] = M1[i][j] * num
    
    
    
# Display the result 
print("\nUpdated matrix:")
matrixPrint(M1)


# ### b) Matrix-Matrix Multiplication

# In[3]:


# Initialize two test matrices
M1 = [[3, 2], [0, 1]]
M2 = [[1, 3], [2, 0]]

# Initialize matrix to store results
mRes = []

# Loop over the first matrix
for i in range(0,len(M1)):
    # Store the indvidual rows
    row = []
    for j in range(0,len(M1)):
        row.append(M1[i][j] + M2[i][j])
        
    # Append row
    mRes.append(row)

# Display the result   
print("Result:")
matrixPrint(mRes)


# ### c) Matrix-Matrix Multiplication

# In[5]:


# Initialize two test matrices
M1 = [[1, 2], [3, 4]]
M2 = [[5, 6], [7, 8]]


# Initialize matrix to store results
mRes = []

# Loop over all rows of the first matrix
for n in range(0,len(M1)):
    # Store the indvidual rows
    row = []
    
    # Loop over all columns of the second matrix
    for k in range(0,len(M2[0])):  
        # Initialize the variable that will store the temporary sums
        multSum = 0
        # Loop over all rows of the second matrix
        for m in range(0,len(M2)):
            # Add the latest multiplication to the sum
            multSum += M1[n][m] * M2[m][k]
        # Add the sum to the row 
        row.append(multSum)
    
    # Append the rows to the matrix
    mRes.append(row)


    
# Display the result  
print("Result:")
matrixPrint(mRes)

