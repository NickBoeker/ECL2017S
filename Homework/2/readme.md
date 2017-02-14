Nick Boeker  

A -  

'''bash  
$ git branch test1 master  
$ git branch test2 master  
'''  
B -  
'''bash  
$ git checkout test1  
Switched to branch 'test1'  
$ cd Homework/2/  
$ touch test.txt  
'''
C -  
'''bash
$ gedit test.txt  
'''  
D -  
'''bash
$ git add -A  
$ git commit -m "Created text.txt for branch test1"  
[test1 2d6f106] Created text.txt for branch test1  
 1 file changed, 1 insertion(+)  
 create mode 100644 Homework/2/test.txt  
'''
E -  
'''bash
$ git checkout test2  
Switched to branch 'test2'  
$ ls
readme.md
'''
You no longer see test.txt in the folder as you are on a different branch. Since test.txt was created after test1 and test2 were branched that means that it wasn't present when test2 was created and therefore is not there.  
F -  
'''bash
$ touch test.txt
$ gedit test.txt
