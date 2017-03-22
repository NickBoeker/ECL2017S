1 -  Assembly is the closest, FORTRAN is the oldest  
2 -  C is an ancestor of python  
3 -  1st - everything is local so you have version control but only for one person.
     2nd - everything is on everyone's computer including the server so there is less chance of file loss.  
	 3rd - All the files are on the server and you download the ones you need from there based on the versions you need.
4 - git tag -l  
5 - print('Python Is Great For String Manipulation.'.replace(' ','-').lower()[::-1])  
6 - Syntax, Runtime, semantic  
7 - No they are not mutable but they can be redefined.  
8 - attached file  
9 - A - For list objects when you assign the same list to multiple variables without explicitly defining them you are referencing the same list as the variable names are just aliases  
    B - When you redefine b as a combination of a and a it creates the new list in a new memory address so they are no longer aliases  
10 - they are aliases and you could create individual ones using a = list(b) where b is the old list and a is the new list  
11 - attached file  
12 - A1 - answer_status='correct' if abbr=='ECL' else 'wrong'
     A2 - answer_status=('correct','wrong')[abbr!='ECL']
     B  - Tuple - print(('You answer is correct','wrong buddy...try again')[answer!='correct'])
13 - No, one is considering memory ids and one is considering the tuple contents
14 - lambda g:x**2+4*x+1  
15 - [a,b] = [b,a]  
     [a,b] = (a,b)  