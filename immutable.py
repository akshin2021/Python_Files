#Immutability - Not changeable (Memory addresses)
#Identity operator in Python - is and isnot 
#Every datatype in python is a class 
#Every data in python is an object 
#Compiler accesses this data by address 
#We access it by identifiers 

a=100 #Here the datatype is int, which is a class and 100 is an object of that class
b=100 #Data 100 is placed in memory and the identifiers a and b are given to the same address to reduce space complexity 
print(type(a))
print(id(a))   #Gives address of 
print(id(b))   #Same address as a 

print(a is b)  #Returns true because same address for both 
print(a is not b)
a=a+10
b=110
print(id(b))
print(id(a))
print(a is b)

#Unwanted memory is those memroy which has no refernence. This is removed by garbage collector. 

