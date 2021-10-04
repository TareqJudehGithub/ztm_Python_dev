"""SSH

- move to the root directory, and create a hidden ssh folder:
  $ cd ~
  $ mkdir .ssh
  $ cd .ssh
- create a key
  $ ssh-keygen
  >>> enerating public/private rsa key pair.
  >>> Enter file in which to save the key (/c/Users/USER10/.ssh/id_rsa): 
  don't fill in a pass, just hit Enter twice.
  - ssh-keygen generates two keys: id_rsa.pub and id_rsa.private
  - use catalog on the public key, and copy it's content:
    $ cat id_rsa.pub
  - on GitHub website, go to Settings> SSH and GPG keys.
  - Now, click on New SSH key and paste your key.
  - Finally, in your project folder Git repository, type the following:
    $ eval $(ssh-agent)
    $ ssh-add ~/.ssh/id_rsa_github
  
  And that's it. Now we have a secure SSH connection to GitHub.


"""