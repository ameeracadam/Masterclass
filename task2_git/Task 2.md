#   Task 2

##  1. Set up an account on Github
In your browser, navigate to [Github](https://github.com). At the main page, enter a **username**, **password**, **email account**, and click on **Sign Up for GitHub**.

## 2. Create a README markdown file
Markdown is a light-weight and easy to use syntax for styling all forms of writing on the Github platform. Before creating a README markdown file, you need to first create a new  remote repository. 

Click on the 'Create New Repository' button. You will need to enter in a mandatory repository name. Set the repo owner to yourself (default). Set the repository to **Public**. Check the box that initializes the repository with a README. The README allows you to clone your remote repository to your local machine.

## 3. Clone the repository to your machine
From the repo that was created, obtain the HTTP line
In the Terminal, type in the following command line:

`git clone [HTTPS_from_Github]`

The repo will be cloned to your machine in a folder with the same title as the repo.

## 4. Add new files on your machine
You can add any file to the repository folder in your machine. For instance, you can add type in a simple 'Hello World' Python file, or another markdown and place it into the repository folder.

## 5. Commit the changes
Before commiting to the repository, you need to stage the files that you've added to your local machine. In your terminal, `cd` into the repository folder in your local machine and type in the following command line:

`git add .` Stages the commit for all files in folder <br />
`git add '[file_name]'` To commit just one file

This adds the file to your local machine and stages the commit.
To unstage a file, type in `git reset HEAD [File_Name]`

Commit your added file to the repo on your local machine by typing in the following command line:

`git commit -m "Added a file"`

This commits the tracked changes and prepares them to be pushed to a remote repository (i.e. the repo on Github)

## 6. Push changes back to the repo
To push your commits to your repo on Github, type in the following command line in your Terminal:

`git push origin [your_branch_name]`

This pushes the changes made in your local repository to a remote repository you specified as the origin.