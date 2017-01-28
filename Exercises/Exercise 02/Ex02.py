from threading import Thread
import threading

j = 0
lock = threading.Lock()

def thread_1_function():
    global j
    for i in range(0,100001):
        lock.acquire()
        j+=1
        lock.release()

def thread_2_function():
    global j
    for i in range(-100000,0):
        lock.acquire()
        j-=1
        lock.release()

def main():
    thread_1 = Thread(target = thread_1_function, args = (),)
    thread_1.start()
    thread_2 = Thread(target = thread_2_function, args = (),)
    thread_2.start()

    thread_1.join()
    thread_2.join()
    print(j)

main()