# Arithmetical operators + - * / // % ** 
# // - floor division 
# % - Mod
# + does addition as well as concatenation 
# ** - exponential 

print("Data" * 3)
print(5**3)

print(14/2) # division always returns a float value 
print(15//2) # this does floor division and provides decimal value (floor of 7.5 is 7)

print(15%2) # this gives remainder 
print(True + False ) # True means 1 and False means 0, so output of 1 is displayed 

# Relational operators - Gives relation between two values 
# < , > , >= , <= , == , =!
# These operators always return value in True or False 

a= 15>10
print(a) # Prints True since 15 is greater than 10 
print(15==15) #Here values are checked and True is displayed 
#print(15=15) - This shows error as it directly assigns value 
a=15
b=15
c=15
print(a==b)
print(a==b==c) #This 
a,b,c=15,10,0
print(a>b>c)

 
#Logical Operators 
# and, or aka short circuit operators because if first condition is false(for AND) or true( for OR), further conditions will not be checked 
# not
d=(5>10) and (7>5)
e=not d
print(d)
print(e)

# Conditional operators 
# if else 

#Program to check if no is positive or negative 
n=int(input("Enter a no"))
if n>=0:
    print("Number is positive")
else:
    print("NUmber is negative ")

# To check if no is odd or even 
if n%2==1:
    print("Number is odd")
else:
    print("Number is even")

#Program to enter 2 numbers and print greater no
n1=int(input("Enter 1st no. "))
n2=int(input("Enter 2nd no. "))

if n1>n2:
    print(n1)
else:
    print(n2)

#Arithmetic Assignment operators 
# +=,-=,*=,/= , //=,%=
a+=10  # a=a+10 can be written like this 

#Identity operator is not applicable for float, decimal , and only on 0-256
# This is because the address is same for such variables. 
a=100
b=100 # Here address of a and b are same until value of 256 
print(a is b)

#Membership operator (applicable for collections as well)
# in , not in (Useful for checking valid, invalid emails etc)
Name="Akshin is here "
print('V'in Name) #Prints True if present 
print('Akshin' in Name)

#Check if Email is valid
Email=input("Enter an email id")
if ('@' not in Email and '.com' not in Email):
    print("Invalid email")
else:
    print("Valid email")


#Bitwise operators
# &, | , ^ , ~ , << , >> 
# Left shift operator - Does zero filling 
# Right shift operator - Does filling based on value of MSB ( if MSB is 0, fills with 0 else with 1)
# Shortcut for Left shift operator - a=5<<3 ( Multiply 5 with 2 raised to power of 3)
# Shortcut for Right shift operator - Divide by no of times (Suppose 13>>2, since odd, do n-1/2 that gives 6 then divide n/2 gives 3 which is the answer )

# Replacement operator
# format() method
rno = 500
name="Akshin"
age=20
str="Roll no is {0} and name is {1} and age is {2}"
print(str.format(rno,name,age))

strin="Roll no is {rn} and name is {nm}"
print(strin.format(rn=rno,nm=name))