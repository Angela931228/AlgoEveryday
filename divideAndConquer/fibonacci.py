def fib(n):
    f = [0]*n
    if n <= 1:
        return f
    f[1] = 1
    for i in range(2, n):
        f[i] = f[i-1] + f[i-2]
    return f

def fib_recur(n):
    l = [0,1]
    if n <= 1:
        return l[:n]
    for i in range(2, n):
        l.append(_fib_recur(i-1) + _fib_recur(i-2))
    return l

def _fib_recur(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f = _fib_recur(n-1) + _fib_recur(n-2)
    return f


def fib_cache(n):
    l = [0,1]
    if n <= 1:
        return l[:n]
    _fib_cache(n-1, l)
    return l

def _fib_cache(n, l):
    if len(l)-1 >=n:
        return l[n]
    f = _fib_cache(n-1, l) + _fib_cache(n-2, l)
    l.append(f)
    return f


#dynamic programming
print(fib(12))
#recursion
print(fib_recur(12))
#recursion with memorization
print(fib_cache(12))