#Two loops in python 
#While and for 
#To execute a block of statements repeatdely in python
#Every loop has 3 requirements, initilization condition and incremental or decremental

#n=int(input("Enter a number"))

#for i in range(0,n):           #This repeats the statement n no. of times 
#   print("Repeat")

#while(n<=9):
#    n+=1
#    print(n)                    #Prints numbers from entered number upto 10 
    

#To print square of numbers from 1 to 10 
#i=1
#while(i<=9):
#    print(i*i)
#    i+=1

# for loop with else (Only supported in Python)
#for i in range(6): #This means range starts from 0 and ends at 5, does not go to 6. 
#    print(i)
#else:
#    print("Loop has ended")  #This is executed when the loop execution has been completed. 

#NESTED FOR LOOP 
#Nesting while loop becomes complex 
#Using range in for is suitable for nesting 

#Displaying a pyramid structure using nested for loops 
lm=int(input("Enter the limit "))
#for i in range(1,lm+1,1): #for every value for 1 print all 5 values 
#    for j in range(1,i+1,1):
#        print("*",end=" ")

#    print()

#To print star pyramid in reverse 
for i in range(1,lm+1,1):
    for j in range(lm,i-1,-1):
        print("*", end=" ")
    print()
