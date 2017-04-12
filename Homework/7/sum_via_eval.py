import sys

lst = sys.argv[1:]
str1 = " ".join(lst)
summ = eval(str1.replace(" ","+"))
print("The sum of ",str1," is ",summ)