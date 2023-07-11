a=50
def one():
    #global a #without this line it causes an error as local variable is not initialized. (used to make changes to global variable)
    #a+=50
    new=globals()['a']
    x=10+new 
    print("Sum" , x)
    
print("global", globals()['a'])

print(one())
print(a) #prints 100 as the global variable has been changed 