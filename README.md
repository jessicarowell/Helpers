# Summary of contents

This repository holds my helper functions, which are various functions or short scripts I write to help me with general tasks.
I try to keep them generic. In fact, some of these originated as very specific scripts that I have stripped down because I a) had time to do so, and b) saw their potential future usefulness.

I will try to keep them well-commented and complete, but do note that this repository is more an attempt to preserve my own sanity and less an attempt at trying to make useful things for others. 

## Brief description of scripts and files

`make_directories.py`
This script organizes files into directories. I wrote it to accommodate a tool that requires fastq files to be arranged in separate directories with the same sample ID as the fastq file.  It identifies the files from a user-provided keyword (e.g. 'fastq') and creates directories with the names of those files (n directories for n files).  Then it moves each file(s) into the corresponding directory.

`undo_make_directories.py`
Anticipating the need to undo the action described above, should the tool not work, I also wrote this script which sort-of does the reverse. It identifies a list of directories based on a keyword (e.g. 'IlluminaRun3'), moves all the files out of those directories, and then optionally deletes the empty directories, moves all the files out of those directories, and then (optionally) deletes the empty directories.

`my_modules.py`
Contains useful functions I've written and use in many of my scripts.

`loan_calculator.py`
A very basic loan calculator that allows you to input one extra additional payment (made in month 1) and to add extra monthly payments (applied every month for the lifetime of the loan). Run `python loan_calculatoy.py -h` to see a description of input arguments. Written in about half an hour on python 3.8.10, so not a very sophisticated script but does what I needed.