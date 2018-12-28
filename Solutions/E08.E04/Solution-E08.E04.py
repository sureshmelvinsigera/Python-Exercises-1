
# coding: utf-8

# # Solution: Exercise 8.E04

# In[4]:


# Initialize an empty list
favMovies = []


# In[5]:


# Initialize a counter
counter = 0

# Initialize the loop
while (counter < 5):
    # Request user input
    movie = input("Please enter a favourite movie: ")
    
    # Append the new movie to your list
    favMovies.append(movie)
    
    # Update the counter
    counter += 1


# In[6]:


# Print the list of movies
print(favMovies)

