import time
from threading import Thread
from multiprocessing import Pool

COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


print('Started...')

# Single threaded application

start = time.time()
countdown(COUNT)
end = time.time()

print('Time taken in seconds -', end - start)

# Multi-threaded application

t1 = Thread(target=countdown, args=(COUNT, ))
t2 = Thread(target=countdown, args=(COUNT, ))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)

print('End.')
