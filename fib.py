def fibonacci_of(n):
   if n in {0,1}: 
        return n
   return fibonacci_of(n-1) + fibonacci_of(n-2)

print([fibonacci_of(n) for n in range(15)])


def fib_2(n):
    if n <= 2:
        return 1
    return fib_2(n-1) + fib_2(n-2)

print([fib_2(n) for n in range(15)])

 