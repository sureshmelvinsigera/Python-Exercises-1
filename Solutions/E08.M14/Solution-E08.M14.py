
# coding: utf-8

# # Solution: Exercise 8.M14

# In[4]:


# Request user input
string1 = input("Please enter the first word: ")
string2 = input("Please enter the second word: ")


# In[5]:


# Initialize an anagram flag
anagram = True

# Check that the lengths of the strings are equal
if(len(string1) != len(string2)):
    # Set flag to false
    anagram = False
else:
    # Now we know that string1 and string2 are of the 
    # same length let's count how many instances of 
    # each letter are in each string
    for i in range(0,len(string1)):
        # Count how many times string1[i] appears 
        # in string1
        count_str1 = string1.count(string1[i])
        
        # Count how many times string1[i] appears 
        # in string2
        count_str2 = string2.count(string1[i])
        
        # If the numbers differ for any letter the two 
        # strings cannot be anagrams
        if(count_str1 != count_str2):
            anagram = False
        else:
            continue


# In[6]:


# Display result
if(anagram):
    print(string1 + " and " + string2 + " are anagrams!")
else:
    print(string1 + " and " + string2 + " are not anagrams.")

