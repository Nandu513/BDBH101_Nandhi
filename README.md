# BDBH101_Nandhi
Worksheet answers


Worksheet 1 for 

BDBH-101 Computer Programming and Operating Systems - Linux and Python

Semester 1: July - Dec 2023

Revised by
Shyam Rajagopalan & Nithya Ramakrishnan,
IBAB, Bengaluru, India

Shell Scripts

Worksheet released: 25 Aug 2024
Submission deadline: 8 Sep 2024
Variables, Conditions and Loops

Write a shell script program to list all executable files available in your system

1. Create a comma separated value (CSV) file called users.csv.  The file should contain a list of userid, username, and userdept. The userid and username separated by a comma (,). The username and the department are separated by colon (:).  Each user is separated by a newline. For example, a sample csv file may look like this
arun,Arun P:Molecular biology
bharath,Bharath Ramesh :Genomics
chithra,Chithra P:Machine Learning
dinesh,Dinesh BJ:Computational Biology
esther:Esther S:Synthetic biology
etc. 

2. Write a script that reads this file and displays userid, username and the department in consecutive lines.  You may want to use the “read” command to read the csv file.

3. Create a text file with the names of the fasta files. The text file looks like the following
B5ZC00.fasta
B5ZC01.fasta
B5ZC02.fasta
B5ZC03.fasta
B5ZC04.fasta
	All these files can be downloaded by appending individual file names to the following URL -  http://www.uniprot.org/uniprot/.   We need to now look for a specific motifs - “YVDRHPDDTINDYLNSI” and “MGNHTWDHPDIFEILTTK” in these files and if they are present, we need to output the name of the file and the exact position in the file (character position). Can you create a bash script for accomplishing this task?

4. Write a script to know if the disk space where the $HOME directory exists crosses a set threshold capacity, say 70%. If yes, print a message to alert the user. 

5. Write a script to show the percentage of home directory usage relative to the root directory.

6. Write a shell script and produce a file that contains the names of all sub folders with size 0 (that is empty subfolders) for a given directory. You can hardcode the given directory into the script for this exercise. Later, we will learn how to accept this from the command line.

7. Write a shell script that will take an input file and remove identical lines (or duplicate lines from the file). You can hardcode the name of the input file into your script for now. Later we will learn how to read this from the command line.

8. Write a shell script that loops through every number 1 through 100 and prints each number to standard output. The script should also conditionally print the number is greater than the given threshold for every number larger than a threshold value. A threshold value can be set in a program to say 90, for example.

9. Write a shell script that greets you based on the current time. The script should call the date command, extract the current hour (look into using %H) and then print the following greeting based on the time. If it is between 5AM (05:00) and 12PM (12:00): Good morning! If it is between 12PM (12:00) and 6PM (18:00): Good afternoon! If it is between 6PM (18:00) and 5AM (5:00): Good night!

10. Given a string representing a DNA sequence, count how many of each nucleotide is present. If the string contains characters that aren't A, C, G, or T then it is invalid and you should signal an error.  You can hardcode a DNA string in your script to test your script.
