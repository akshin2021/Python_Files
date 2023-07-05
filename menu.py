#Creating a menu with 3 choices 
#Choose the greater of 2 numbers if choice is 1
#Choose the lesser of 2 number if choice is 2
#Swap the numbers if choice is 3
 
print("\n 1. Max \n 2. Min \n 3. Swap")

n1,n2=map(int,input("Enter two numbers").split(','))
choice =int(input("Enter your choice "))

if choice==1:
    print(max(n1,n2))  #Inbuilt method in python to get maximum
    #if n1>n2: 
    #    print(n1)
    #else:
    #    print(n2)

elif choice==2:
    if n1<n2:         #using logic to get minimum instead of inbuilt method 
        print(n1)
    else:
        print(n2)
    
elif choice==3:
    n1,n2=n2,n1
    print("After swapping the first number is %d" %n1 ,"and the second number is %d" %n2)


