#Actual and formal arguemnts
#Positional arguments - No of arguments passed must be same as no defined in function definition 
#Keyword arguments 
#Default arguements 
#Functions in python are objects which is why we can also pass functions as arguments 

def abc(a,b): # a,b are formal arguments 
    pass

def abc(a="10",b="20"): #here values are given acc to keyword so order does not matter 
    pass

def abc(a,b,c,d=10): #d has a default value of 10 so even if no value is passed in function call it does not return error 
    pass             #default value has to be given from last to first so that positional parameters are not affected

def abc( * args): # * is used to define variable length arguments , args is a variable name
    for m in args:# now for every argument that is passed a for loop is created to take in the arguments which is stored as a tuple. 
        print(m)  # variable argument has to be passed at the end, so that size issue is not created 
     
def display(f):
    return "Course is being done " +f

def msg():
    return "This is the message you wanted "

#calling 

#x=display("Akshin")
print(display("Akshin")) #This way we pass a value directly 
print(display(msg()))    #This way we pass a function as argument 