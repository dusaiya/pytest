# encoding: utf-8
'''
Created on 2017年6月21日

@author: alibaba

python的多线程明显有问题
等待时间内的20s, 其他线程无法获取锁。

'''

import threading
import time
import os

# This function could be any function to do other chores.
def doChore():
    time.sleep(1)
    print time.time()

# Function for each thread
def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()                # Lock; or wait if other thread is holding the lock
        if i != 0:
            i = i - 1                 # Sell tickets
            print(tid,':now left:',i,';time:',time.time()) # Tickets left
            ##doChore()                 # Other critical operations
        else:
            print("Thread_id",tid," No more tickets",';time:',time.time())
            os._exit(0)              # Exit the whole process immediately
        lock.release()               # Unblock
        doChore()                    # Non-critical operations

# Start of the main function
i    = 100                           # Available ticket number 
lock = threading.Lock()              # Lock (i.e., mutex)

# Start 10 threads
for k in range(10):
    new_thread = threading.Thread(target=booth,args=(k,))   # Set up thread; target: the callable (function) to be run, args: the argument for the callable 
    new_thread.start()   