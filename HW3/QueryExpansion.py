import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from itertools import islice
import operator
import os

pwd = os.getcwd()
# Create a list of stop words
list_of_stop_words = []
with open("Stop_words.txt", 'r', encoding='utf-8') as file:
    list_of_stop_words = [line.strip().rstrip().lstrip() for line in file]

# print(list_of_stop_words)

# Get the queries from the queries.txt file
queries = []
query_expanded = []
top_n_doc = []
dict_terms = {}

with open("Queries.txt", 'r', encoding='utf-8') as file:
    queries = [line.strip() for line in file]
    # print(queries)


def get_top_N_docs(query, n):
    with open(query + ".txt", 'r') as myfile:
        # Get top ten documents for that query
        top_n_doc = [str(next(myfile)).strip().split('.txt')[0].split(".")[1] for x in range(n)]
    return top_n_doc


# This method calculates the tf of each term in the top 10 documents for that particular query
def term_frequency(query, list_of_documents):
    dict_term_tf = {}
    for each_document in list_of_documents:
        each_document = each_document.replace("_", " ")
        fo = open(pwd + "\\Corpus\\" + each_document + ".txt", 'r', encoding="utf-8")
        doc_content = str(fo.read().lower())
        doc_content_tokens = nltk.word_tokenize(doc_content)
        #   doc_content_tokens = doc_content.split(" ")
        for term in doc_content_tokens:
            if term.lower() not in list_of_stop_words and term not in query.lower():
                if term not in dict_term_tf:
                    dict_term_tf[term] = 1
                else:
                    dict_term_tf[term] += 1
    # Sort the dictionary based on the number of keys
    dict_term_tf_sorted = sorted(dict_term_tf.items(), key=operator.itemgetter(1), reverse=True)
    return dict_term_tf_sorted


# Expand the query , dict_terms : the sorted dictionary containing most frequent words, k : number of terms upto
# which the query will be expanded
def expand_query(query, list_terms_freq, k):
    # n_items = take(k, dict_terms.iteritems())
    # n_items = {k: dict_terms[k] for k in dict_terms.keys()[:2]}
    print("Expanding the query upto " + str(k) + " terms... \n")
    expanded_query1 = query
    query_terms = [x[0] for x in list_terms_freq][:k]
    for each_term in query_terms:
        expanded_query1 = expanded_query1 + " " + str(each_term)

    return str(expanded_query1).rstrip()


# After the iteration the list query_expanded will have all the expanded query.
for each_query in queries:
    # Get the top ten documents for the query
    print("Finding the relevant documents....\n")
    top_docs = get_top_N_docs(each_query, 10)
    # For each of the Top ten documents find the most frequent words , avoiding the stop words
    print("Finding the most frequent words in the corpus....\n")
    dict_tf = term_frequency(each_query, top_docs)
    query_exp = expand_query(each_query, dict_tf, 7)
    query_expanded.append(query_exp)

# Write the expanded query to the file

fo = open("Expaded_Query.txt", 'w', encoding="utf-8")

for each in query_expanded:
    fo.write(each + "\n")
