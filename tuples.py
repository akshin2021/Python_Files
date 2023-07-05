#A read only version of lists 
#Immutable 
#Duplicates are allowed
#Indexing can be done but further changes cannot be done
#Elements cannot be added in runtime 
#Slicing can also be done 

myt=(10)
print(type(myt)) #For a single element tuple a , has to be added. Otherwise type is taken as int

myt=(10,20,30)
print(type(myt))

for x in myt:
    print(x)

#m=len(myt) 
for i in range(len(myt)):
    print(myt[i])

#To add or make changes to a tuple, change it into a list, make changes and convert it back to a tuple.

mylist=[]

n=int(input("Enter the number of elements"))
for i in range(n):
    x=int(input())   #Takes input of each element of list in a loop 
    mylist.append(x)
myt=(mylist)
print(type(myt))

check=myt.count(1)
print(check)