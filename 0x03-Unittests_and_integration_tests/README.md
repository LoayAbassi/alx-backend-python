# unittest and integration tests

memorization (caching): avoiding computing same values twice 

def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]  # Return the cached value if it exists
    rest of the code ...
