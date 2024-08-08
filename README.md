# biofilm

https://www.microbiologyresearch.org/content/journal/mgen/10.1099/mgen.0.000598

This is the paper, go down to the data section, it has an ncbi link
Click on SRA-run selector at the bottom, then download the metadata and the accession list

The accession list contains the list of the labels/names of where the data is at, now we run scripts to download/access this data

First, we have to download the SRA toolkit (this link) and unzip it

Then we go to settings and add it as a path (the bin directory in the SRA toolkit folder; …/bin”
“Open the Start Menu and search for "Environment Variables".
Click on "Edit the system environment variables".
In the System Properties window, click on "Environment Variables".
In the Environment Variables window, find the "Path" variable in the "System variables" section and select it.
Click "Edit", then "New", and add the path to the SRA Toolkit’s bin directory.
Click "OK" to close all the windows.”

Remember to restart a new terminal

Now we run the prefetch and fastq-dump commands, can use a script
script is attached to the github

GITHUB:
going to do this two ways
first, made this repository online on git, and added the first readme. 
then, i ran
git clone (link); followed by cd; followed by git status to check, then we can do any changes, git add, (git status), git commit -m "name"; then git push origin main

other way: ill make another git repository just for the my-datascience-app2 dockerfile (it might be big so ill put it separately)
link here: https://github.com/CZTKG/my-datadocker.git

note, the git push origin (branchname) was master or main




