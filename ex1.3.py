def fib(n,cache = {0:0, 1:1}):
    if n not in list(cache.keys()):
        cache[n] = fib(n-1,cache) + fib(n-2,cache)
    return cache[n]