#there are many methods to check validity of number
#the differnce is not felt when we take numbers in english 
#but these come into play when considering numbers from other languages 

n=(input("Enter a number"))

if n.isdigit(): # checks if number is digit or not , isnumerical or isdecimal can also be used 
    n=int(n)
    if n%2==0:
        print("Number is even")

    else:
        print("Number is odd")

else:
    print("Not a number, please enter a valid number")