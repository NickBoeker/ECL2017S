def Newton(f, dfdx, x, eps=1E-7, maxit=100):
    if not callable(f): raise TypeError( 'f is %s, should be function or class with __call__' % type(f) )
    if not callable(dfdx): raise TypeError( 'dfdx is %s, should be function or class with __call__' % type(dfdx) )
    if not isinstance(maxit, int): raise TypeError( 'maxit is %s, must be int' % type(maxit) )
    if not test_Newton_div_by_zero(dfdx,x): raise ZeroDivisionError( 'dfdx(%g)=%g - cannot divide by zero' % (x, dfdx(x)) )
    if maxit <= 0: raise ValueError( 'maxit=%d <= 0, must be > 0' % maxit )
    n = 0 # iteration counter
    while abs(f(x)) > eps and n < maxit:
        x = x - f(x)/float(dfdx(x))
        n += 1
    return x, f(x), n

def test_Newton_div_by_zero(dfdx,x):
    success = (True,False)[dfdx(x)==0]
    return success

from math import cos,sin

f = cos
dfdx = lambda x: -1*sin(x)
x=0

x1,f_x,n=Newton(f,dfdx,x)