Files and descriptions : 
===================================================================================================================================================================
HW4.java  : This is the implementaion of Luecne Search. Similar to implementation is Assignemnt4. 
BIG BANG THEORY_LUCENE.txt : This is the result of the query big bang theory using Lucene model, contains top 100 documents with score and rank
HUBBLE SPACE TELESCOPE_LUCENE.txt : This is the result of the query "hubble space telescope" using Lucene model, contains top 100 documents with score and rank
INTERNATIONAL SPACE STATION_LUCENE.txt : This is the result of the query "international space station" Lucene model, contains top 100 documents with score and rank
MARS EXPLORATORY MISSIONS_LUCENE.txt : This is the result of the query "mars exploratory missions" Lucene model, contains top 100 documents with score and rank
MILKY WAY GALAXY_LUCENE.txt : This is the result of the query "milky way galaxy" using Lucene model, contains top 100 documents with score and rank
Queries_Lu.txt : Contains the Queries for Lucene. This is refered in HW.java. 
BIG BANG THEORY_BM25.txt : This is the result of the query big bang theory using BM25 model, contains top 100 documents with score and rank
HUBBLE SPACE TELESCOPE_BM25.txt : This is the result of the query "hubble space telescope" using BM25 model, contains top 100 documents with score and rank
INTERNATIONAL SPACE STATION_BM25.txt : This is the result of the query "international space station" BM25 model, contains top 100 documents with score and rank
MARS EXPLORATORY MISSIONS_BM25.txt : This is the result of the query "mars exploratory missions" BM25 model, contains top 100 documents with score and rank
MILKY WAY GALAXY_BM25.txt : This is the result of the query "milky way galaxy" using BM25 model, contains top 100 documents with score and rank
BM25.py : Implmentation of BM25 ranking algorithm using Python 3. 
Unigram_df.txt : This contains the docment frequency of the unigram. Format : unigram-->(doc1 doc2..)-->df
No_of_terms.txt : This contains the number of unigrams in each document of the corpus.
Unigram.txt : This contains the Inverted list of in the format unigram --> (docID, tf)
Queries.txt : Contains the Queries for BM25 . BM25.py uses this fle to read the queries.
Task1.py : This program generates the inverted index (Unigram.txt) and a document which contains the number of terms in each document(No_of_terms.txt)
Task3b.py : This program generates the docId and df information.(Unigram_df.txt) 
Comparison.txt : Comparision of the results of the Lucene and BM25 results.
Impl.txt : This document contains the short report on implmentation.
===================================================================================================================================================================
How to setup and run ?
>Install Python3.
>Import NLTK
> Run Task1.py : Make sure you all files of the corpus in a folder called "Corpus" in the same directory where this src code is present.After successfully running this ,
you should get the two files mentioned above.
> Run Task3b.py 
Please make sure you have No_of_terms.txt, Unigram_df.txt,Unigram_df.txt
>Run BM25.py : This program generates 5 tables (txt files mentioned above) . The name of the file generated is in the format : Query_name(uppercase)_BM25.txt
> Run H4.java : This program generates 5 tables (txt files mentioned above0. The name of the file generated is in the format : Query_name(Uppercase)_Lucene.txt
===================================================================================================================================================================