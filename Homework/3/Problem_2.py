#!/usr/bin/env python

from platform import python_version
print('This is Python version',python_version(),'\n')

mainString = "Python is the best language for String manipulation!"

print(mainString,'\n')

print(mainString[::-1],'\n')

print(mainString[::-2],'\n')

print(mainString.swapcase(),'\n')

print("The sentence '"+mainString+"' contains \n{} 'a' letters, and \n{} 'A' letters!\n".format(mainString.count('a'),mainString.count('A')))

print(mainString.replace(' ', '\n'),'\n')

print(mainString.replace(' ', '\n').upper())