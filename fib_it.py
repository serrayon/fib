# Using iteration and a python function 
  # Line 3 defines Fibonacci, which takes a positive interger, n, as an argument
def fibonacci(n):
    # Validate the value of n
    # Line 5 and 6 perform the usual validation of n
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number epected, got "{n}"')
    # Handle the base cases
    # Lines 10 and 11 handle the base cases where n is either 0 or 1
    if n in {0, 1}:
        return n
    #Line 13 defines two local variables, previous and fib_number, and initializes them
    # with the first two numbers in the Fibonacci sequence 
    previous, fib_number = 0, 1
    #line 16 starts a for loop that iterates from 2 to n + 1. The loop uses an 
    #underscore (_) for the loop variable because it's a throwaway variable and you 
    #won't be using this value in the code.
    for _ in range(2, n + 1):
        # line 19 Computes the next Fibonaccy number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number
        
    return fib_number 
    
    
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))


print([fibonacci(n) for n in range(15)])



        