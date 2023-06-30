#What is the difference between type casting and conversion?
#Convert one data type to another is the definition for both typecasting and conversion 
#Implicit type conversion - supported by C. (Not in Python)
#Explicit type conversion - Forced type conversion in Python 

#To convert into int we use int() method 
a="12"
b="13"
print(a+b)              #this gives concatenated string as they are not integers

a=int(a)
b=int(b)
print(a+b)              #this gives sum as they are converted into int values 

 
#To convert data of GET method into int 

print(str(12.5))

#Strings cannot be converted into Bool
print(bool("hello"))    #String returns true if not empty 
print(bool(-1))         #Only for 0 it gives false 
 
print(float(1))         #Gives float value of 1 which is 1.0
print(float(True))      #Gives 1.0 as output 

