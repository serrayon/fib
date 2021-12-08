#Fibonacci sequence in python
class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]
        
    # line 9 defines another special method, .__call__(). this method turns the 
    # instances of fib into callable objects 
    def __call__(self, n):
        #Validate the value of n 
        # line 12 and 13 validate the value of n by using a conditional statement.
        # if n is not a positive integer number, then teh method raises a ValueError
        if not (isinstance(n, int) and n >= 0):
            raise ValueError('Positive integer number expected, got "{n}"')
        #check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            #Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)
            
        return self.cache[n]
    
    
fibonacci_of = Fibonacci()
        
print(fibonacci_of(5))
print(fibonacci_of(6)) 
print(fibonacci_of(7)) 

print([fibonacci_of(n) for n in range(15)]) 

     
    #line 3 defines the class initializer,.__init__(). It's a special method that you can 
    #use to initialize your class instances. Special methods are sometimes referred to as 
    #dunder methds
    
    # line 4 creates the .cache instance attribute, which means that whenever you 
    #create a fibonacci object, there will be a cache for it. This attribute
    #initially contains teh firs numbers in the fib sequence 
        
    #line 15 defines a conditional statement to check for those Fibonacci numbers 
    # that were already calculated and are available in .cache. if the 
    #number at index n is already in .cache, then line 16 returns it. 
    #otherwise, line 19 computes the number, and line 20 appends to .cache 
    #so you don't have to compute again.
        
            
            
