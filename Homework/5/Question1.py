#!usr/bin/env python

def fib(n):
    if n == 'stop':
        res = 'why pls'
        #break
    elif n.isdigit() and n.find('.') ==-1:
        res = fibSeq(int(n))
        print('Fib({})={}'.format(n,res))
        n = input('Please enter another non-negative integer or stop: ')
        fib(n)
    else:
        print('The input argument {} is not a non-negative integer'.format(n))
        n=input('Please enter non-negative integer or stop: ')
        fib(n)

def fibSeq(n):
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fibSeq(n-1)+fibSeq(n-2)
    return res

n = input('Please enter a non-negative integer or stop: ')
fib(n)
