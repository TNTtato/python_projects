# Return a list of the n first terms of fibonacci series

def fib(n):
  if n == 1:
    return [0, 1]
  
  listre = fib(n - 1)
  listre.append(listre[-1] + listre[-2])
  return listre

print(fib(8))