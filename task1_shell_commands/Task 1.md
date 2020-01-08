#   Task 1
Write a short series of shell commands in a single line, to list out the processes that belong to "root" and print out the PID , owner and name of process

##  Create a bash shell
In Windows: `New-Item [name_of_script].sh` <br />
In Mac: `touch [name_of_script].sh`

##  Type in the following lines:
`#!/bin/bash/`
Type in she-bang. Tells the program to interpret the script with when executed

## Execute in BASH
`ps axco pid,command,user | grep root`

`ps axco pid`   to list processes by process ID (PID) <br />
`grep root`     to search in the root directory

##  To run the script:
In a Terminal, `cd` to directory of script, and type in the following:
`bash [name_of_script].sh`
