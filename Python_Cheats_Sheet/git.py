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
"""