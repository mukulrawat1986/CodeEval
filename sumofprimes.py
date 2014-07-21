import sys

def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(xrange(i*i, np1, i))
    return ",".join([str(i) for i in filter(None, s)])

l = sieve(10000).split(',')

print sum([int(l[i]) for i in xrange(1000)])
