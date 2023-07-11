import time 
from threading import *
class myThread1(Thread):
    def run(self):
        for i in range(1,11):
            print("This is my thread1",i)#getName())
            time.sleep(1)

class myThread2(Thread):
    def run(self):
        for i in range(12,22):
            print("This is my thread2",i)#getName())
            time.sleep(1)

t1=myThread1()
t2=myThread2()

print("Main thread starts")
#print("Name of main thread",threading.main_thread())
t1.start() #this makes the program consider it as thread
t2.start()
print("Main thread ends")
