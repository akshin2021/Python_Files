# Input and output functions in Python 

# This is one way to write 
print("Enter first no ")
a= input()


# In python, we can combine these two lines into one as follows 
a=input("Enter first no ")

#Input always reads data as string, this can lead to concatenation instead of addition 

a=int(input("Enter a first no ")) #typecasting has been done to convert string into int 
 
#Reading data in a single line 
#Entering value of 2 variables in single line using split method. 
a,b=map(int,input("Enter two no").split(','))
print(b)