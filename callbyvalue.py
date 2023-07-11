
def myfactorial(n):
    i=1
    while n!=0:
        i=n*i
        n=n-1
    return i

def myreversenum(n):
    s=0
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    return s

def area(r):
    areaa=3.14*r*r
    return areaa 

