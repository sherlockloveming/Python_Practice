def fib(n):
    if type(n)!=int:
      raise TypeError("please type an integer")
    if n<1:
      raise ValueError("please type a positive number")
    if n==1 or n==2:
      return 1
    else:
      return fib(n-1)+fib(n-2)

                      
