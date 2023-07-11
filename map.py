# This program is for map and filter with lambda function
# filter(function,sequence) 

mylist=[1,3,4,2,5]
#maplambda = lambda 

#mylist1=list(map(lambda x:(x*x),mylist))       #Perform operation on lambda function
#print(mylist1)


def odd_even(n):

    if n%2==0:
        return True 
    else:
        return False 

#mylist2=list(filter(odd_even,mylist))   
mylist2=list(filter(lambda n:(n%2==0) ,mylist))   # Filter specific data from sequence 
print(mylist2)

def prime(n):
    i=2
    r=0
    while i<n:
        if n%i==0:
            r=1
        i=i+1
    if r==0:
        return True 
    else:
        return False

mylist3=list(filter(prime,mylist))
print(mylist3)



mystring="Data Anaylsis Course"

mystring1=list(filter(lambda v:v == "a" or v=="e" or v=="i" or v=="o" or v=="u",mystring))
print(mystring1)

