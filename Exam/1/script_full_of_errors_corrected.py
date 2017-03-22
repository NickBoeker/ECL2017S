#You can't start variable names with a number
a1 = 2
#b hasn't been defined so you can't reference it
a1 = 2
#Code is case sensitive, change one of the Xs to match the other
x = 2
y = x + 4 # is it 6?
#the module is math and you need to import pi as well
from math import tan,pi
#Use python3 print formatting
print(tan(pi))
#Don't overwrtite a function with a variable of your choosing/don't numerically evaluate strings
#Also beginning and ending string requires same choice of either " or '
pi1 = "3.14159"
print (tan(pi))
c = 4**3**2**3
#Make sure parentheses match on either end
_ = ((c-78564)/c + 32)
#Percent signs can't be evaluated for numerics, use decimal instead
discount = .12
#dashes can't be evaluated in numerics, simply use zeros
AMOUNT = 120.00
#dollar signs can't be used in numerics
amount = 120
#Use quotation marks to make it a string
address = 'hpl@simula.no'
#Can't use keywords as variable names, also make sure to use the same string container ends
and1 = 'duck'
class1 = "INF1100, gr 2"
continue_ = x > 0
#This code works by evaluating everything as boolean, fox is rev simply asks if the two variables
# have the same values which they do, it then uses in to see if True is in Persian which it isn't
# since the only item in it is the string 'a human language'
rev = fox = True
Persian = ['a human language']
true = fox is rev in Persian