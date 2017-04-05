1 - This block only runs if the program is called by the program itself.  If it is called from a different program the __name__ property will be the program it is called from.  
2A - from myModule import myfunc as f  
2B - myModule  
3 - summ=[even[i]+odd[i]for i in range(5)]  
4 - Infinitely, you are looking at the number of items in myList and adding one each time you run the list, resulting in an infinite loop.  