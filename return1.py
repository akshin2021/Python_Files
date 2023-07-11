def asmd(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    return c,d,e,f

n,p,q,r=asmd(10,12)
print(n)


def myswap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b

a,b=myswap(10,12 )
print("After",a,b)