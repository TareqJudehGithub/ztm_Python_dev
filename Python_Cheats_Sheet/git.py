"""
- .gitignore
- In your project folder, create a .gitignore file
  $ touch .gitignore
  $ inside .gitignore, include all files and folder that you do
  not wish to push to GitHub.
    .gitignore
    /venv
    /__pycache__

- Each time we push to github, we need to turn ON our venv
- $ source venv/Scripts/activate
- Now, type the following in order
  $ git config --global user.email tareq.judeh@outlook.com
  $ git config --global user.name TareqJudehGithub
  $ git config --global push.default matching
  $ git init
  - git with initialize a new repository (master)
  - create a new repo over GitHub (I named mine flask_blog_2021).
  - Back in the project folder, run:
  -change to main branch
  $ git branch -M main
  $ git remote add origin https://github.com/TareqJudehGithub/flask_blog_2021.git
  $ git push -u origin main
  
  We could also change the default branch name when running 'git init'
  $ git config --global init.defaultBranch main
  
  $ git log displays all past commits in details. To leave the log, simply 
    press 'Q' button on your keyboard.
    
  Creating new branches and merging with the original
  
  To create a new branch:
  $ git checkout -b <branch_name> 
  - After adding new features, add & commit the new changes:
  $ git add .git
  $ git commit -m "Added new features."
  - Now, switch back to the original branch:
  $ git checkout <main_branch_name>
  - After that, merge the new branch with the original:
  $ git merge <branch_name>
  finally, push to GitHub:
  $ git push original main
  
  
  Deleting data
  $ git rm <filename>
  git rm also automatically executes "git add <filename>" command.
  
  Revert changes 
  $ git reset --hard HEAD~1
  --hard HEAD~1 means go back 1 commit earlier
  
  Deleting branches
  To delete a branch that we no longer need:
  - First, make sure that you're no longer on that branch, using 
    $ git checkout <branch_name>
  - Then type $ git branch -D <branch_to_delete>
  
  
  (Unstaged changes) 
  Revert back to the latest committed Git branch if we still did not 'git add'
  these changes.
  $ git checkout -- .
  OR
  $ git checkout -- <filename>  
    In case we just needed to undo changes for a specific file.
  With this command, we undo any changes made to our project added after the
  last committed operation.
  
  Staged changes (Undo $ git add .)
  
  
  git credential reject => ENTER
  host=github.com => ENTER
  protocol=https => ENTER
  
  
  Downloading a GitHub remote project into our local machine
  $ git clone <repository_link> .
  We added ". space" to instruct Git to clone the GitHub repository into the GitHub
  Current folder.
  
"""