#Printing fibonacci series using recursion 


a=0
b=1

def fibo(n):
    global a,b
    if n==0:
        return 
    
    else:
        c=a+b
        
        print(c,end="")
        a=b
        b=c
        fibo(n-1)

#Calling 
n=int(input("Enter the limit "))
print(a)
print(b)
fibo(n-2)