''' Multithreading '''
'''
multithreading is a way acheiving multitasking. In multithreading the concept of threads is used.
we need to import 'threadidng' API to implement multithreading in python
'''






''' Index :_
What is Multitasking in Python?
Types of MUlittasking?
What is thread?
How to achieve Multithreading in Pyhton?
How to create Threads in Python?
       >>> Without creating a class
       >>> By extending Thread class
       >>> Wtihout extending Thread class
Advantages of Multithreading
       '''

'''
>>> What is Multitasking in Python?
    A) processor executes multiple tasks at the same time is known multitasking
'''

'''
>>> Types of Multitasking?
    A) There are two types of multitasking. They are:
                   1) Process Based
                   2) Thread Based
'''

''' 
>>> What is thread?
    A) A thread is basically independently flow of execution. 
       A single process can consists multiple threads. 
       Each thread in a program performs a particular task 
       '''
'''
>>> How to achieve multithreading in python?
   A) '''

from time import sleep, time
from threading import *


# ''' Method -1 creaing threads without creating class '''
# def new(n):
#     for x in range(n):
#         print(x,'- child executing..',current_thread().getName())
# t1 = Thread(target=new,args=(6,)) # assign the function name to target whetever function you want to execute in this thread, args is specifying funcitono argument values
# print(current_thread().getName()) # getting current thread name executing
# t1.start() # child thread is created when this start is called only
# t1.join() # the next thread or(main) is in waiting state until this thread task is completed
# print('Bye',current_thread().getName())




# ''' Method -2 creating threads by extending thread class.'''
# class A(Thread):
#     def run(self): # to run thread, the method name must be called 'run' keyword in this way. so when we clall the start method the run method automatically executed
#         for i in range(5):
#             print('Hello',current_thread().getName())
            

# class B(Thread):
#     def run(self):
#        for i in range(5):
#            print("hi",current_thread().getName())
 

# a = A()
# b = B()

# a.start() # starting thread. it call automatically run method in that class
# b.start()
# a.join() # wait until thread 1 is completely executed
# b.join() # wait until thread 2 is completely executed
# print('Bye',current_thread().getName())


# ''' Method - 3 creating threads without extending thread class '''
# class C:
#     def c(self,n): # to run thread, the method name must be called 'run' keyword in this way. so when we clall the start method the run method automatically executed
#         for i in range(n):
#             print('Hello',current_thread().getName())
            

# class D:
#     def d(self,n):
#        for i in range(5):
#            print("hi",current_thread().getName())

# c = C()
# d = D()

# t1 = Thread(target=c.c,args=(5,))
# t2 = Thread(target=d.d, args=(10,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('Bye',current_thread().getName())


''' 
>>> Advantages of Multithreading 
1) Enhanceed performance by decreased development time
2) Simplified and streamlined program coding 
3) Simultaneous and parallelized occurrence of tasks
4) Better use of CPU resource 
'''

'''proof - time comparison'''
def d1(n):
    for x in n:
        print(x%2)
def d2(n):
    for x in n:
        print(x%3)
n = [2,4,3,6,7]
f1 = time()
# without using thread
d1(n)
d2(n)
f2 = time()
# with using thread
t1 = Thread(target=d1,args=(n,))
t2 = Thread(target=d2,args=(n,))
t1.start()
t2.start()
t = time()
print(f2-f1,'without threads')
print(t-f2,'with threads')

# f1 = time()
# # without using threads
# # d1(n)
# # d2(n)
# #with using threads
# t1 = Thread(target=d1,args=(n,))
# t2 = Thread(target=d2,args=(n,))
# t1.start()
# t2.start()
# f2 = time()
# print(f2-f1)



