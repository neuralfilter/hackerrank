def fibo(n):
    if n == 1:
        return 1
    else:
        return n + fibo(n-1)

def seq(z):
    if z == 1:
        return 1
    else:
        return z * seq(z-1)
