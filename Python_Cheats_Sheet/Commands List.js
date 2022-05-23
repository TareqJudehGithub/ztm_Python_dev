//Control + Shift + ~ to start the terminal
// dir to browse all file and folders.
//cd to move up into a folder
//cd <drive letter>cd E:  to a diff directory
//cd .. exit the current folder to the one before
//cd\   exit to the root directory.
//clear clears the terminal screen
//cd ~ takes us to the machine user folder directory..

//mkdir <folder name>   to create a new dir
//echo <file name>   to create a new file
//start  <file name> opens a file
//mv    to rename a file.  mv fileA.exe fileB.exe
//rm <filename>  to delete a file.
//rm -r [folder name] to delete a folder

//open -a "Sublime Text"    to open the Sublime app
// code    to open VS Code
//code <file name> opens a file.
//pwd displays the current directory path
//exit  exits the terminal
// use Up arrow and tab for repitition. and calling on previous lines
//$ notepad bash_profile to enter the bash profile and install new add ons.
//$ source bash_profile  reloads our profile

//Github commands and how to upload a project:
//After creating a new project, copy the needed link from Github under 
// "Clone or download" button. make sure u click on https first.
//from Terminal, go to ur project files folder using cd.
//run: get clone <project path>  or the link u copied from the Github website: 
//see below:
//git clone https://github.com/TareqJudeh75/Background--Generator.git
//a new folder named Background--generator will be created next to ur project files.
//go inside Background--generator, and run:
//(master =)
//***then, run git status
//*** after that, run git add <filename> to add all needed project files.
//***now, run git commit -m "Adding starting project"
//git config --global user.name TareqJudeh75 to login on github
//*** finally, run git push so we need to let github.com that these r the changes.
//for others to work on the same file, they should repeat the above steps.
//*** these are the 4 steps needed each time we change and need to upload these changes
// into github.

//*** git pull to update the file from github. use that each time u start working on the project.
//Master branch, is the main authority.. how our website will look.
// we can create on a sub branch, without affecting the Master branch (what the user sees).
// only when its tested and finished, we can bring it back(merg) to the Master branch.
//to create a new branch:
// inside the project github folder, run:  git branch <branch name> this will create
//a new branch within the Master branch.
//then, run git branch to make sure the new branch has been created successfully.
//after that, run:  git checkout <the new branch name>
// or git checkout -b <branch name>
//git diff to look at whats changed on the project 
// after updating the project files, run again the needed Github upload steps,
// then after u run the git push command, run the following:
//git push --set-upstream origin littleFeature

