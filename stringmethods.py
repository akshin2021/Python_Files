#Methods of Strings 
# Strings are immutable so that they are not changed even by mistake 
# To access methods, we use a dot (.)

s="   this {} is my rollno and {} is my name. I am not giving anymore data  "
rno=1
name="Akshin"
age=20
                            
print(s.upper())              #Converts to upper case      
print(s.lower())

print(s.count('s'))           #Takes count of any character
print(len(s))                 #Gives length of string
print(s.count('this',5))      #Takes count of this from 5th index
print(s.find("data"))         #Gives location of data 
print(s.capitalize())         #To make first letter capital 
print(s.format(rno,name)) 
print(s.title())              #Capitilise 1st letter of every word
print(s.strip())              #Removes unwanted space - Helps to avoid counting space for valid emails etc. 
print(s.lstrip())             #Removes left space
print(s.rstrip())             #Removes right space