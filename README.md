# Masterclass

This repo contains guides to Tasks 1-6 for the Masterclass. In each folder, there are the necessary files and READMEs related to each task. Please see below for a preview for each task.

## Task 1: Shell Commands
Write a short series of shell commands in a single line, to list out the processes that belong to "root" and print out the PID , owner and name of process

## Task 2: Git
Set up an account on Github. Create a README markdown file. Clone the repository to your local machine. Add new files to your machine. Commit and push then changes back to the remote repository.

## Task 3: Docker
### Task 3A
1.  Explain the difference between an image and a container
2.  Give some advantages of using containers
3.  How can the security of containers be compromised?
4.  How is Docker different from Vagrant?

### Task 3B
Install Docker on your local machine. Pull the rocker/rstudio image to your local machine. Create a container for the image. Access the application from your browser.

### Task 3C
Set up a docker-compose file for the image in Task 3B. Demonstrate that containers can be started up with docker-compose.

## Task 4: Data Formats
### Task 4A
Given the data in a CSV, write a short Python snippet to read the CSV, extract only the 3rd and 1st fields (in that order) and write the output in JSON. Bonus: Write in XML

### Task 4B
Given the data in a CSV, write a bash shell script, using regular expressions to replace the ID with "XXXXX". You mar assume IDs have 6-7 digits with an optional letter.

## Task 5: Organising Data - Databases and Data Warehouses
### Task 5A
Pull the Postgres image from DockerHub. Clone the DB scripts from GitHub. Run the SQL scripts to create a database and insert rows.

### Task 5B
Provide a code segment in Python to query Database

## Task 6: Building Models and Microservices
### Task 6A
Write a function that reverses a sequence of characters in input data. Package the function into a Flask app that accepts user-input characters. Test the Flask app. Open the browser to load the app. Key in a sequence of characters and submit. The app should return the sequence of characters in reverse.

### Task 6B
Set up a Docker container for Postgres. Set up a Docker container for PostgREST. Show how the API can be queried to list the first 10 rows of a table.
