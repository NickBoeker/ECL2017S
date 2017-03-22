def findSmallerPrimes(n):
    if n == 1:
        #block code
        n=0
    else:
        if isPrime(n)==True:
            print(n)
        findSmallerPrimes(n-1)
    
def isPrime(n):
    def isDivisor(n,div):
        if n == div:
            return True
        elif n%div==0:
            return False
        else:
            return isDivisor(n,div+1)
    return isDivisor(n,2)
n = input('Enter an integer number: ')
print('Here is a list of all prime numbers smaller than {}:'.format(n))
findSmallerPrimes(int(n))