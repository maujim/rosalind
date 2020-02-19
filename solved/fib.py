def fibonacci_rabbits(n,k):
    if n in {1,2}:
        return 1
    else:
        return fibonacci_rabbits(n-1,k) + k*fibonacci_rabbits(n-2, k)

m = 31
l = 2
print(fibonacci_rabbits(m,l))
