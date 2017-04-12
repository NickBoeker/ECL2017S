import sys

lst = sys.argv[1:]
str1 = " ".join(lst)
lst = [int(i) for i in lst]
summ = sum(lst)
print("The sum of ",str1," is ",summ)