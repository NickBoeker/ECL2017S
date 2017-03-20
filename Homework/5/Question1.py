#!usr/bin/env python

def fib(n):
    if n == 'stop':
        res = -1
        return res
    try:
        n = int(n)
    except ValueError:
        print('The input argument {} is not a non-negative integer'.format(n))
        res = -2
        return res
    if int(n) < 0:
        print('The input argument {} is not a non-negative integer'.format(n))
        res = -2
        return res
    res = fibSeq(int(n))
    return res

def fibSeq(n):
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fibSeq(n-1)+fibSeq(n-2)
    return res

i = 1
while i == 1:
    n = input('Please enter a non-negative integer or stop: ')
    res = fib(n)
    if res == -2:
        continue
    elif res == -1:
        break
    else:
        print('Fib({}) = {}'.format(n,res))
