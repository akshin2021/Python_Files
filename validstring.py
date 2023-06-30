s=input("Enter a string")
print(s.isascii())     #this returns true as english letters have an ascii code 


hindi="हिंदी" 
print(hindi)           #Python supports unicode,so this will be printed
print(hindi.isascii()) # This returns false as hindi letters do not have ascii, they only have unicode 

count=0
if s.isspace(): # checks only if the entire string is Space, does not check if there is space in between 
    print("Space is not allowed")

else:
    print("This is valid ")

#Get the count of space in a string (By replacing string with digit, alpha, numeric ,we can get count of those)
for i in range(0,len(s)):
    if(s[i].isspace()):
        count+=1

print("the count of space is %d" %count)

