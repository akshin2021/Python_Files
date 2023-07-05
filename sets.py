#Sets 
#Mutable 
#Heterogenous data 
#Insertion order is not preserved (Therefore slicing is also not allowed)
#Duplicates are not allowed 
#Aadhar, mobile no. wherever duplicate entries are not required, set is to be used
#Set,  frozen set and dictionary are represented by {}
#Cannot be accessed using indexed number

# A blank set (empty) - By default is considered as dict 
myset=set({}) #To convert dict into set 
print(type(myset))
mynewset={} #This is a dict 
print(type(mynewset))
mynewset=frozenset({}) #Converts dict into frozenset
print(type(mynewset)) 

myset={1,4,32,3}
print(myset) #prints in random order

myset.add(10)
print(myset) #prints in random order

n=int(input("Enter the limit"))
x=int(input("Enter the element to be added"))
for i in range(n):
    myset.add(x)

print(myset)

myset.discard(40) #does not show error even if element not present in set 
#myset.remove(40) #shows an error if myset doesnt contain the element
print(myset)

#Frozen set and sets have same properties 
#Frozen set is immutable whereas set is 

myset=frozenset({1,2,3,45})  #Converts into frozenset 
print(type(myset))