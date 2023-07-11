# By default there is a main thread in Python 
# The main thread goes to running state directly without going to newborn 
#There are three methods to create threads
# Without using thread class
# Inherit your class with thread class
# Without inherit class with thread class
import time 
from threading import * 

def display():
    for i in range(1,11):
        print(i)
        time.sleep(1) #Sleep puts program on halt for one second 

def show():
    for i in range(100,111):
        print(i)
        time.sleep(1)

#Without using class 

#start=time.time()
#display()
#show()
#end=time.time()
#print(end-start)
t1=Thread(target=display) #Brings threads into Newborn stage
t2=Thread(target=show)
start=time.time()
t2.start()
t1.start()
end=time.time()

print(end-start)
print(t1.getName())
t1.setName("One")
print(t1.getName())

#Methods of Thread Class in python 
#start()
#is_alive() - checks if thread is alive or not
#join(timeout) - if there are 3 threads, if time of 10 seconds is given. It holds for 10 seconds. 
#join() - all threads wait until it completes execution 
#getName() - gives name of thread 
#setName(string)- sets name of thread 
#name - it is a property (not a method)
#is Deamon() 
#set Deamon()


