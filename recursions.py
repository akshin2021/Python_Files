#Function calling itself is called recursion 
#two types of recursion 
# direct and indirect recursion
#Space complexity is increased by recursion 
#recursion and recursive functions are different 
#recursions are used mostly in DSA 

#def abc():  #example of direct recursion 
#    print("Hello")

#    abc()

#abc()

#def ab():

#    xy()

#def xy():

#    ab()

#def factorial(n): #Using recursion to get a factorial
#    if n==0:
#        return 1
#    else:
#        f=n*factorial(n-1)
#        return f 
     

#n=int(input("Enter a number "))
#x=factorial(n)
#print("Factorial is ", x)

#def factorial(n):
#    f=1
#    while(n!=0):
#        f=f*n
#        n=n-1
#        return f
s=0
def reverse(n): #Reverse of number using recursion
    global s 
    if n>0:
        r=n%10
        s=s*10+r
        n=n//10
        reverse(n)
    return(s)

n=int(input("Enter a number "))
x=reverse(n)
print("Reverse is " , x)
if n==x:  #To check if palindrome 
    print("Number is palindrome")

else:
    print("Not palindrome ")

#print(11//10)