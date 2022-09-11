#Define a function that returns the fribonacci series of a given number
def fribonacciFun(n):
    if n < 0:
        return None
    fb1 = 1
    fb2 = 1
    if n > 2:
        for i in range(3, n + 1):
            fb = fb1 + fb2
            fb1, fb2 = fb2, fb
    return fb2
for i in range(1, 10):
    print("Frib ", i, "--->", fribonacciFun(i))
#Con recursividad:
#def fib(n):
#   if n < 1:
#       return None
#   if n < 3:
#       return 1
#   return fib(n - 1) + fib(n - 2)
