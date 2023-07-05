#A collection in which corresponding to every data there is a key 
#Data stored with key value 
# Represented using {}
# It is immutable 
# Used in projects when key value is required. 
# Duplicate keys are are not allowed but duplicate values are allowed
# Keys are unique but data can be same (such as names)
# Insertion order is preserved after Python 3  .7 

mydict={1:20,2:20,3:40}
print(mydict.get(1))    #Returns value stored in key 1
print(mydict.keys())    #Returns all the keys 
print(mydict.items())   #Returns all items (key-value pairs)
print(mydict.values())   #Returns all values

#No add or delete
#Cannot access elements using index number (Use keys to access)
#if keys are duplicated, it does not show error, instead replaces the key with new value
mydict[1]=21            #This changes the key 1 value from 20 to 21
print(mydict)