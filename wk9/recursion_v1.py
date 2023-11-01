def factorial(n):
    if isinstance(n,int) and n>0:
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)
    else:
        return 0
