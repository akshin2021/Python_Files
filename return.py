def myfactorial(m):
    f=1
    while m!=0:
        f=f*m
        m=m-1
        return f #return by value. when a function  
    
m=int(input("Enter a no "))
x=myfactorial(m)
print( "factorial %d" %x)