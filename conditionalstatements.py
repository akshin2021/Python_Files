# if 
# if/else
# if elif 
# conditions dont need bracket in Python 
# Loops require identation

n=int(input("Enter a number "))
if(n==1):                                   #Here all conditions are checked regardless of one being true 
    print("Number is 1")
if(n==2):
    print("Number is 2")
if(n==3):
    print("Number is 3")
if(n==4):
    print("Number is 4")
if(n==5):
    print("Number is 5")
if(n==6):
    print("Number is 6")

#if n<1 or n>6:
    print("Invalid")


#Nested if 
#Suppose 2 conditions are to be executed such that 2nd condition is to be checked after checking 1st condition
#This is where we use nested if 
name=input("Enter a name")
age=int(input("Enter age "))
status=input("Enter status ")
if name=="Akshin":                                  #This loop works on the basis of checking first condition and skips others if first conditon is false 
    if age>=20:
        if status=="Student":
            print("Applicant is eligible ")
        else:
            print("Only students are eligible ")
    else:
        print("Age not satisfied")
else:
    print("Name is not in list")


#Elif can be used in python instead of switch case
#Here all conditions are not checked if one is true 

n=int(input("Enter a number "))
if(n==1):                    #Here all conditions are not checked if one is true 
    print("Number is 1")
elif(n==2):
    print("Number is 2")
elif(n==3):
    print("Number is 3")
elif(n==4):
    print("Number is 4")
elif(n==5):
   print("Number is 5")
elif(n==6):
    print("Number is 6")
