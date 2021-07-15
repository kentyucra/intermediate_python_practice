from threading import Thread, Lock, local
import time

database_value = 0


# Everytime we acquire we have to release
def increase(lock):
    global database_value

    lock.acquire()
    local_copy = database_value

    # processing
    local_copy += 1
    time.sleep(0.1)

    database_value = local_copy
    lock.release()

# increase is equivalent to increase1
def increase1(lock):
    global database_value

    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


if __name__ == "__main__":
    print('start value', database_value)

    lock = Lock()

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)
