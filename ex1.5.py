import timeit
import matplotlib.pyplot as plt

fibTimes = []
fibOptTimes = []

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

def fib(n,cache = {0:0, 1:1}):
    if n not in list(cache.keys()):
        cache[n] = fib(n-1,cache) + fib(n-2,cache)
    return cache[n]

for i in range(36):
    time = timeit.timeit(lambda:func(i), number = 1)
    fibTimes.append(time)

for i in range(36):
    time = timeit.timeit(lambda:fib(i), number = 1)
    fibOptTimes.append(time)

plt.scatter(range(36), fibTimes, color = 'b', label = "Non-Optimized")
plt.scatter(range(36), fibOptTimes, color = 'r', label = "Optimized")
plt.legend()
plt.xlabel('n')
plt.ylabel('Time to find the nth value of the fib sequence')
plt.show()
