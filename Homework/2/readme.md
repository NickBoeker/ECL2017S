Nick Boeker  

A -  

```bash  
$ git branch test1 master  
$ git branch test2 master  
```  
B -  
```bash  
$ git checkout test1  
Switched to branch 'test1'  
$ cd Homework/2/  
$ touch test.txt  
```
C -  
```bash
$ gedit test.txt  
```  
D -  
```bash
$ git add -A  
$ git commit -m "Created text.txt for branch test1"  
[test1 2d6f106] Created text.txt for branch test1  
 1 file changed, 1 insertion(+)  
 create mode 100644 Homework/2/test.txt  
```
E -  
```bash
$ git checkout test2  
Switched to branch 'test2'  
$ ls  
readme.md  
```
You no longer see test.txt in the folder as you are on a different branch. Since test.txt was created after test1 and test2 were branched that means that it wasn't present when test2 was created and therefore is not there.  
F -  
```bash
$ touch test.txt  
$ gedit test.txt  
```
G -  
```bash
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
```
H -  
```bash
$ git checkout master  
Switched to branch 'master'  
Your branch is up-to-date with 'origin/master'.  
$ git merge test1  
Updating 999c304..2d6f106  
Fast-forward  
 Homework/2/test.txt | 1 +  
 1 file changed, 1 insertion(+)  
 create mode 100644 Homework/2/test.txt  
```
I -  
```bash
$ ls  
readme.md  test.txt  
```
The test.txt file has appeared in master since we merged the changes.  
J -  
```bash
$ git merge test2  
Auto-merging Homework/2/test.txt  
CONFLICT (add/add): Merge conflict in Homework/2/test.txt  
Auto-merging Homework/2/readme.md  
CONFLICT (content): Merge conflict in Homework/2/readme.md  
Automatic merge failed; fix conflicts and then commit the result.  
```
The error appears because the two branches have files by the same names with different contents.  
K -  
```bash
$ git checkout test2
Homework/2/readme.md: needs merge
Homework/2/test.txt: needs merge
error: you need to resolve your current index first
```
L -  
```bash
$ git status  
On branch master  
Your branch is ahead of 'origin/master' by 2 commits.  
  (use "git push" to publish your local commits)  
You have unmerged paths.  
  (fix conflicts and run "git commit")  

Unmerged paths:  
  (use "git add <file>..." to mark resolution)  

	both modified:   readme.md  
	both added:      test.txt  

no changes added to commit (use "git add" and/or "git commit -a")  
```
Because as stated above there are files with the same name and differing contents.  
M -  
```bash
$ gedit test.txt
```
N -  
```bash
$ git status  
On branch master  
Your branch is ahead of 'origin/master' by 2 commits.  
  (use "git push" to publish your local commits)  
You have unmerged paths.  
  (fix conflicts and run "git commit")  

Unmerged paths:  
  (use "git add <file>..." to mark resolution)  

	both modified:   readme.md  
	both added:      test.txt  

no changes added to commit (use "git add" and/or "git commit -a")  
$ git add -A  
$ git commit -m "Fixed merge errors in test.txt"  
[master 64d55ad] Fixed merge errors in test.txt  
$ git checkout test2
Switched to branch 'test2'
```
O -  
```bash
$ git branch -d test1  
error: The branch 'test1' is not fully merged.  
If you are sure you want to delete it, run 'git branch -D test1'.  
```
P -  
```bash
$ git checkout master  
Switched to branch 'master'  
Your branch is ahead of 'origin/master' by 4 commits.  
  (use "git push" to publish your local commits)  
$ git branch -d test1  
Deleted branch test1 (was 2d6f106).  
$ git branch  
* master  
  test2  
```
Q -  
I would assume it was due to the fact that test1 was succesfully merged into master but not into test2.  
R -  
```bash
$ git checkout test2  
Switched to branch 'test2'  
$ git branch -d test2  
error: Cannot delete the branch 'test2' which you are currently on.  
```
S -  
```bash
$ git checkout master  
Switched to branch 'master'  
Your branch is ahead of 'origin/master' by 5 commits.  
  (use "git push" to publish your local commits)  
$ git branch -d test2  
Deleted branch test2 (was 7a65888).  
$ git branch  
* master  
```
T -  
```bash
$ git add -A  
$ git commit  
On branch master  
Your branch is ahead of 'origin/master' by 7 commits.  
  (use "git push" to publish your local commits)  
nothing to commit, working directory clean  
$ git push  
```
