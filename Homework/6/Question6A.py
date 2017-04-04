def is_prime(n):
    
    is_prime = True
    
    def is_divisible(n,divisor):
        if n<(divisor-1)*divisor: return False
        if n%divisor==0: return True
        else:
            divisor += 1
            return is_divisible(n,divisor)

    if is_divisible(n,divisor=2): is_prime=False
    return is_prime

def get_primes(n):
    count = 0
    if n == 1:
        return count
    else:
        if is_prime(n):
            count = 1
        n -= 1
        return count + get_primes(n)
    
def is_prime_for(n):
    for div in range(2,n):
        if n%div==0:
            return False
    return True
    

def get_primes_for(n):
    count = 0
    for idx in range(3,n):
        if is_prime_for(idx):
            count += 1
    return count