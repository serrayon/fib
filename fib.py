def fibonacci_of(n):
   if n in {0,1}: 
        return 1
   return fibonacci_of(n-1) + fibonacci_of(n-2)

print([fibonacci_of(n) for n in range(15)])


def fib_2(n):
    if n <= 2:
        return 1
    return fib_2(n-1) + fib_2(n-2)

print([fib_2(n) for n in range(15)])

cache = {0: 0, 1: 1}
def fib_3(n):
    if n in cache:    #BASE CASE
        return cache[n]
    # compute and cashe the fibonaccci number
    cache[n] = fib_3(n-1) + fib_3(n-2) #recursive case
    return cache[n]

print([fib_3(n) for n in range(6)])
print([fib_3(6)])
def fib_4(n, memo={ 0:0,1:1}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_4(n-1, memo) + fib_4(n-2, memo)
    return memo[n]

#print([fib_4(n) for n in range(23)])
print([fib_4(6)])
print([fib_4(n) for n in range(7)])   

 
