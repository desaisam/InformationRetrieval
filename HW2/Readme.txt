Built and complied using Python 3.

=====================================================================================================
Please download the following packages to run the program :
numpy
matplotlib
nlkt
os
re
BeautifulSoup
===================================================================================================

Information about the file contents :

Source Codes:
Tokenzation.py -- This is for task1. The program reads the given two files ,
BFS.txt and FOCUSED.txt. Parses the URL and downloads the Raw HTML pages is two seperate folders namely 
{pwd}\URL\FOCUS
{pwd}\URL\BFS.
These are 'Deleted'and 'Created again.

The program later reads from the dir {pwd}\URL\BFS , parses the raw URL's using Beautiful Soup, Tokenises each using NLTK
libray.Also these words / tokens are removed punctaution and converted to lower case as a default setting .
These can be changed by changin the boolean values of of two varaibles 'punctuate' and 'casefold'. A text file with the namd 
of document is created which contains the tokens for each document.


Trigram_Generator.py -- This is also related to task1 . Reads the generate '.txt file' and uses the nltk library to create 
trigrams . This corups totally has 2490666 Trigrams.

Graphy.py --This program reads the downloaded HTML file and generates a incoming Graph. For example : A B C D implies B , C , D 
are incoming to A.
The two places this programs  reads from is : {pwd}\URL\FOCUS
{pwd}\URL\BFS. SO PLEASE RUN "Tokenzation.py" before running the python file Graphy.py.
Two two files generated are : G1.txt and G2.txt

PageRank.py : This is the implementation of Page Rank Algorithm from the Book Croft, Stohment et al.
Uses the Graph G1 , Construts inverted Grapgh of outgoing links and use this in the implementation.

Please contact : desai.sam@husky.neu.edu
8574249461 for any clarifications
