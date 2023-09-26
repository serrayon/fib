class Fib():
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        if not (isinstance(n, int) and n >= 0):
            raise TypeError(f'You messed up')
        if n < len(self.cache):
            return self.cache[n]
        else:
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)
        return self.cache[n]

fibster = Fib()  # Instantiate the Fib class
#input prompt 
user_input = input("Enter a positive integer to calculate Fibonacci: ")
try:
    n = int(user_input)
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        result = fibster(n)
        print(f"The Fibonacci number for {n} is {result}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
