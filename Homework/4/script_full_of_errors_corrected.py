#you can't lead a variable name with a number
a1 = 2
#Tries to find a variable named b to copy the value of, have a character instead
a1 = 'b'
x = 2
#Looks for a variable X when we have one by the name x
y = x + 4 # is it 6?
#the module is math not Math, also we need to inmport pi
from math import tan,pi
#Previously was in python 2.7 formatting for print, has to be called as a function in python 3
print(tan(pi))
#Have to use the same string identifiers for beginning and end, also don't use predefined variable names for your own names
p1 = "3.14159"
print(tan(pi))
c = 4**3**2**3
#Too many parentheses, alternatively you could've added an opening one somewhere
_ = ((c-78564)/c + 32)
# % represents modulo not percent so you have to represent your percent as a decimal
discount = .12
# - minus is the subtraction operator and expects another argument, replace with 0s
AMOUNT = 120.00
# you can't represent dollars in an integer.  instead show it in your print statment
amount = 120
#Make sure your strings are strings
address = 'hpl@simula.no'
#and is a keyword, do not use for variable names, also no variable by name of duck
and1 = 'duck'
#Please stop using keywords as variable names, also I don't know what that first character was but have a string
class1 = "’INF1100, gr 2"
continue_ = x > 0
rev = fox = True
Persian = ['a human language','']
#THis works because python can cast a string as a bool and then all the variable types match up.  Also the keyword is True not true
true = fox is rev in Persian