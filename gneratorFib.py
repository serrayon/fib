def fibonacci(max):
  a,b = 0,1
  while a < max:
    yield a 
    a,b = b,a+b 
    
 
    #create generator of fib numbers smaller than 1 million
fibonacci_generator = fibonacci(1000000)
    #print out the sequence
for fibonacci_number in fibonacci_generator:
      print(fibonacci_number)
    
#yield is like return but it wont make a copy of the list or array
#it takes less memory but it can only be called once, in order to 
#call it again you have to create new variable 

#this will print out the numbers but in a list [ ]
my_fibonacci_list = list(fibonacci(100000))
print("My fibonacci list: {0}".format(my_fibonacci_list))

#print out odd fibs 
fibonacci_odds_list = [x for x in fibonacci(100000) if x%2!=0]
print("The odds number are: {0}".format(fibonacci_odds_list))

#functions based on iterables like min,max,sum
print("The min number is: {0}".format(min(fibonacci(1000000))))
print("The max number is: {0}".format(max(fibonacci(1000000))))
print("The sum of is: {0}".format(sum(fibonacci(1000000))))
