#Types of strings 
# Strings in python are immutable
# alpha string - containing only alphabets
# numerical string - containing only numbers 
# alpha numerical string - containing both alphabets and numbers 
# Password is an example of a alpha numerical string 

# Strings are stored as an array with indexing starting from 0 
# Reverse indexing can also be done in Python with last index being -1

# This concept is used in slicing 

name="This course"
print(name[5])

for i in range(len(name)): # This prints the string character by character
    print(name[i])

# Escape sequences in Python 

s= input("Enter a string")
print(s.isupper())
print(s.islower()) # Method to check if lower case
print(s.isalpha()) # To check if alphabet 

#Program to check if name is valid. 
if(s.isalpha()):
    print("Valid First Name")
else:
    print("Invalid First Name ")

#Program to check if password contains both alpha and numericals 
p=input("Enter a password")
if(p.isalnum()):
    print("Password is valid ")

#isalpha 
#isascii
#isnumeric 
#isdigit
#.index
#istitle - If first letters are capital returns true 
#.replace

print(s.replace('a','b'))


#Strings

