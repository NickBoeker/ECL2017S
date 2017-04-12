import sys

try:
   v0 = int(sys.argv[1])
   t = int(sys.argv[2])
except IndexError:
   print("Both v0 and t must be supplied on the command line")
   print("v0 = ?")
   v0 = int(input())
   print("t = ?")
   t = int(input())

g = 9.81

   
if t>2*v0/g:
    raise ValueError("t needs to be between 0 and 2*v0/g = {}".format(2*v0/g))
   
y = v0*t - 0.5*g*t**2
print(y)