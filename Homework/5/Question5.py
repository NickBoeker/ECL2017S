def is_prime(n):
  def has_divisor(n,div):
    if n==div:
      res = True
    elif n%div==0:
      res = False
    else:
      res = has_divisor(n,div+1)
    return res

  res = has_divisor(n,2)
  print('{} is '.format(n)+('not prime.','prime.')[res])

is_prime(49)
