Prerequsites : ***IMPORTANT** Please run this program ONLY on 64bit compiler.This program was run on version 3.3
Packages to install : nltk

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Structure of the assignment :
Task1.py --> Runs the program to generate the deliverables demanded in section of the assignment.
	    The output is stores in the folder Task1. The contents of this folder is discussed later.
Task2.py --> Generate deliverables demanded in section2 of the assignment.
	     Output is stored in the folder Task2 . The contents of this folder is discussed later.
Task3a.py and Task3b.py -->Generate deliverables demanded in section3 of the assignment.
	   	          output is stored in the folder Task3 . The contents of this folder is discussed later.

Tokens --> This folder contains the tokensied output generated in prevoius assigment.
	   **The program fails if is doesn't find this folder . So make sure this folder is present before you run**
Task1  --> This folder contains 5 files
	  1) Unigram.txt : The unigrams generated in the form  unigram -->(docId, frequency)
	  2) Bigram.txt : The bigrams generated in the form bigram --> (docId, frequency)
	  3) Trigram.txt : The Trigrams generated in the form trigram -->(docId, frequency)  	
	  4) Positional_Index.txt : Contains unigrams and its positions encoded using d-gap. Its in the form unigram --> (docId, pos1 pos1 + delta ..)
	  5) No_of_terms.txt : Contains number of unigrams in the corpus.

Task2 --> Contains four text files 
	  1)earth_orbit_5_N : documents containing the words earth and orbit with proximity window 5
	  2)earth_orbit_10_N : documents containing the words earth and orbit with proximity window 10
	  3)space_mission_12_N :  documents containing the words space and mission with proximity window 12
	  4)space_mission_6_N : documents containing the words space and mission with proximity window 6
Task3 --> Contains six text files 
	  1)Unigram_tf : Unigram with its frquency in the corpus
	  2)Unigram_df : Unigram with its document frequency in the form (unigram)--> (doc1, doc2, doc3)-->count	
	  3)Bigram_tf	: Bigram with its frquency in the corpus
	  4)Bigram_df  : Bigram with its document frequency in the form (unigram)--> (doc1, doc2, doc3)-->count
	  5)Trigram_tf : Trigram with its frquency in the corpus
	  6)Trigram_df : Trigram with its document frequency in the form (unigram)--> (doc1, doc2, doc3)-->count
	  7)Unigram_Stop : Contains stop words for unigram
	  8)Bigram_Stop : Contains stop words for bigram
	  9)Trigram_Stop : Contains stop words for trigram
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Design Decisions :
All the three requirements are spread across three seperate python files.
Choice of data structure to store inverted index : dict with key being the term ( unigram, bigram or trigram) and value being list of dictionaries . Each dictionary is in the form of
key : docId , key : frequenct , key : pos (only for unigram)

Why this decision ?
It was imperative for me to store the docId, unigram , positions and freq in a single location.
Other data structures that was considerd is key : unigram and value : dictionary1,dictionary2,dictionary3,.. etc.

The code obeys modularity since each operation is seperated into a function.
Some points about Task1.py : 
list_(uni)(bi)(tri)gram gets the tokensied form using nltk package.
create_InvIndex_unigram : Generates the dictionary which has all the details for that unigram
similary create_invIndex_bigram and create_invIndex_trigram serve the same purpose
These functions has two parameters 1) lsit of terms and 2) the docId

The function write_to_file writes the generated inverted index to a file. 
This program takes around 7 minutes to complete.

Some points about Task2.py:
conjuctive_proximity : Cacluates if two words are at a proximity k , where k is a window, If true it writes the file to a output text file.
decode : this function takes the postions encoded usign d gap and decodes to actual positions
you can check for other words by calling this function : conjuctive_proximity(word1, word2,k)

Some points about Task3a.py This program generates the term and its frequency table.
Some points about Task3b.pyt This program generates the term and its document frequency table.

Issues faced :
Initially the program took 40 mins to run due to poor choice of finding positions. I iterated again in the loop causing lot of overhead. This was overcome by using enumerate in the forloop
Memory not sufficient error when the program was executed using python 32 bit .
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Disclaimer : I ave used fellows corpus after getting a go ahead from the professor and the TA.
In case of any dicrepency/clarifications please contact me : desai.sam@husky.neu.edu
							     8574249461

