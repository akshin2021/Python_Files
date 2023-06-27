#This shows how to format a string 

a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=a+b

print("The addition of %d and %d is : %d" %(a,b,c) )

print("The value of %d is correct" %a)  # %f, %i can also be used 
print("Value is ",a,b,c,sep=":",end=".....") # this adds a seperator between the values and an end msg of sorts)

placeholder="Value of a {} , of b {} and of c {}" # {} acts as a placeholder and .format states the values it holds 
print(placeholder.format(a,b,c))