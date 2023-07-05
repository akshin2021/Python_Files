#Break, continue , pass are the transfer statements in python 
#Normal termination is when loop completes its termination after executing the conditions 
#Break can be used to terminate before normal termination 
#for i in range(1,101):
#    if i==11:
#        break
#    print(i)
#x=[10,9,8,7]

#n=int(input("Enter a number "))
#for i in x:
#    if i==n:
#        print("Element is found")
#        break #As soon as condition is met, no other conditions are checked. 

#Continue statement 
#for i  in range(1,11):
#    if (i==5): 
#        print("This is 5")
#        continue #for i=5, loop goes back to inital condition
#    print(i)

#To print odd numbers from 1-100
#for i in range(1,101):
#    if i%2==0:
#        continue 
#    print(i)

# Pass is used as placeholders 
a=int(input("Enter a number "))
if a>50:
    pass    
else:
    print(a)

for i in range(1,10):
    pass                              #To run for without giving condition, we use pass.
else:
    print("Number gretter than 10")
