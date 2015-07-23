def isprime(n):
    if n == 1:
        print("1 is special")
        return
    for x in xrange(2, n):
        if n % x == 0:
            print("{} equals {} x {}".format(n, x, n // x))
            return False
    else:
        print(n, " is a prime")
        return True

for n in xrange(1, 20):
    isprime(n)
