# List is a collection of heterogenous datatype 
# [] this is used to represent a list 
# Indexing can be done in normal order starting from 0 
# Reverse indexing starts from -1
# Indexing order of list is preserved (Order in which data is given, data is printed in same order)
# Duplicate elements are allowed in Lists 
# Mutable. It can be changed. 
# Methods in list. add(), remove() , reverse() , sort () etc
# Slicing is allowed. (Whenver indexing is preserved, slicing is allowed)

#list=[1,2,3,"Akshin",1.1]
#print(list[1:3])
#print(len(list))

#for i in range(0,len(list),1): #Accessing lists can be done this way 
#    print(list[i])

#for i in list:  #This can also be used to access the lists 
#    print(i)

mylist=[] #Keep an empty list
#print(len(mylist))

n=int(input("Enter the limit "))
print("Enter elements in list ")
for i in range(n):
    m=int(input())
    mylist.append(m) #Using append we add data to the end of list 
print(sum(mylist)) #directly by using the method of sum 

mylist.sort() #This is a method to sort the list. It cannot be directly printed. has to be given as statement before. 
mylist.reverse() #This reverses the elements which were sorted earlier  
mylist.insert(5,10) #first the position, then the data 
mylist.pop() #this removes the last element 
mylist.remove(1)
remove=int(input("Enter the number to be removed"))
mylist.remove(remove)
print(mylist)
# or to print sum using for loop
sum=0
for i in mylist:
    sum=sum+i
print(sum)