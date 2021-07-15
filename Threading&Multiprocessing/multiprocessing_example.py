from multiprocessing import Process, Value, Array, Lock
import os
import time

def add_100(numbers, lock):
    for i in range(100):
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1
            time.sleep(0.01)


if __name__ == "__main__":
    # Create a variable that will be share between processes
    # shared_number = Value('i', 0)

    # Create an array that will be share between processes
    shared_array = Array('d', [0.0, 1000.0, 200.0])
    print('Numbers at beginning is', shared_array[:])
    
    lock = Lock()

    p1 = Process(target=add_100, args=(shared_array,lock))
    p2 = Process(target=add_100, args=(shared_array,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Numbers at end is', shared_array[:])
    # Print a value diferent to 200 because a race condition happens

    print('end of processes')
