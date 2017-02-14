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
'''
G -  
'''bash
$ git checkout test1  
error: The following untracked working tree files would be overwritten by checkout:  
	Homework/2/test.txt  
Please move or remove them before you can switch branches.  
Aborting  
$ git add -A  
$ git commit -m "Created test.txt for branch test2"  
[test2 b11f6ba] Created test.txt for branch test2  
 2 files changed, 40 insertions(+), 1 deletion(-)  
 rewrite Homework/2/readme.md (100%)  
 create mode 100644 Homework/2/test.txt  
$ git checkout test1  
'''
H -  
'''bash
$ git checkout master  
Switched to branch 'master'  
Your branch is up-to-date with 'origin/master'.  
$ git merge test1  
Updating 999c304..2d6f106  
Fast-forward  
 Homework/2/test.txt | 1 +  
 1 file changed, 1 insertion(+)  
 create mode 100644 Homework/2/test.txt  
'''
I -  
'''bash
$ ls  
readme.md  test.txt  
'''
The test.txt file has appeared in master since we merged the changes.  
J -  
'''bash
