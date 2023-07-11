# Functions without name are called anonymous functions 

# lambda creates a function by taking arguments and statements 
# Syntax is as follows 
# lambda arguments : statements ... 

add = lambda a,b:a+b
c=add(1,2)
print(c)

greater= lambda a,b: a if a>b else b 
print(greater(1,2))