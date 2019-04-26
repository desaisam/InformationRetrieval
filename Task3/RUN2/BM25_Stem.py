import math
import time
import operator
import nltk
import os
import re
import string
import unicodedata
import shutil
from nltk import ngrams

# Create Inverted Index :

start = time.time()
pwd = os.getcwd()
dir_path = pwd + '/STEM_CORPUS'
dict_unigram = {}
# Read all the files one by one
all_files = os.listdir(dir_path)
# Lists to store the unigram, bigram and trigram generated
list_unigram = []

dict_freq = {}
dict_no_terms = {}


# Create unigrams
def unigram(tokens):
    return list(ngrams(tokens, 1))


def create_dictionary_files():
    dict_file_content = {}
    for each_tokenised_file in all_files:
        fh = open(dir_path + '\\' + each_tokenised_file, 'r', encoding='utf-8')
        docId_dupl = each_tokenised_file[:-4]
        docId_dupl = docId_dupl.replace("(", "")
        docId_dupl = docId_dupl.replace(")", "")
        if "," in docId_dupl:
            docId_dupl = docId_dupl.replace(",", "")
        # Remove punctuation other than hypen and use lowercase terms
        str_doc_content_dupl = str(fh.read().lower())
        remove = string.punctuation
        remove = remove.replace("-", "")
        pattern = r"[{}]".format(remove)
        str_doc_content_dupl = re.sub(pattern, "", str_doc_content_dupl)
        dict_file_content[docId_dupl] = str_doc_content_dupl
    return dict_file_content


dict_content = create_dictionary_files()
exclude = set(string.punctuation)


def create_invIndex_unigram(docId_uni, list_unigram_func):
    print("\nCREATING INVERTED INDEX FOR UNIGRAM FOR-->" + docId_uni)
    start_bi = time.time()
    # docId_uni = unicodedata.normalize('NFKD', docId_uni)
    # dict_no_terms[docId_uni] = len(list_unigram_func)
    dict_temp = {}
    counter = 1
    str_doc_content = dict_content[docId_uni]
    dict_no_terms[docId] = len(list_unigram_func)
    for index, each_unigram in enumerate(list_unigram_func):
        pos = index + 1
        if each_unigram not in dict_unigram.keys():
            dict_unigram[each_unigram] = [{'docId': docId_uni, 'freq': 1, 'pos': [pos]}]
        else:
            for index, each_dict in enumerate(dict_unigram[each_unigram]):
                if docId == each_dict['docId']:
                    temp = index
                    break
                temp = -1
            if temp != -1:
                dict_unigram[each_unigram][temp]['freq'] += 1
                list_pos = dict_unigram[each_unigram][temp]['pos']
                list_pos.append(pos)
                dict_unigram[each_unigram][temp]['pos'] = list_pos
            else:
                dict_unigram[each_unigram].append({'docId': docId, 'freq': 1, 'pos': [pos]})
    end_bi = time.time()
    print("\nINVERTED INDEX FOR UNIGRAM COMPLETE IN " + str(end_bi - start_bi) + " Seconds")


def write_to_file(term_type, dict_term):
    # if not os.path.exists(pwd + '//Task1//'):
    #     os.mkdir(pwd + '//Task1//')
    fw = open(pwd + "//" + term_type + "_Stem.txt", "w", encoding="utf-8")
    # str_index = ""
    for key, values in dict_term.items():
        # str_index += key + "-->"
        fw.write(str(key) + "-->")
        for each_dict in values:
            fw.write("(" + str(each_dict["docId"] + "," + str(each_dict['freq']) + ")"))
            #  str_index += "\n"
        fw.write("\n")
    fw.close()


for docId, str_doc_content in dict_content.items():
    list_unigram = list(unigram(nltk.word_tokenize(str_doc_content)))
    # Remove punctutation
    list_unigram = [''.join(each_unigram) for each_unigram in list_unigram if each_unigram not in exclude]
    create_invIndex_unigram(docId, list_unigram)

print("\nWRITING UNIGRAM INV INDEX TO A FILE")
write_to_file("Unigram", dict_unigram)

# Number of terms
fw2 = open(pwd + "\\No_of_terms_Stem.txt", "w", encoding="utf-8")
print("\nWRITING NO OF TERMS TO A FILE")
for keys, values in dict_no_terms.items():
    fw2.write(str(keys) + "-->" + str(values) + "\n")
fw2.close()


# dict_unigram


# Inverted index complete .

# Create Document Frequency
def create_df(term_type):
    dict_doc_freq = {}
    fw = open(pwd + "\\" + term_type + "_Stem.txt", 'r', encoding="utf-8")
    line = fw.readline()
    while line:
        count = 0
        list_of_doc = []
        term = line.split("-->")[0]
        str_doc_freq = line.split("-->")[1].strip()
        str_freq = re.split(r'[()]', str_doc_freq)
        str_freq = [str(x).strip() for x in str_freq if str(x) != ","]
        str_freq = list(filter(None, str_freq))
        for each_doc_freq in str_freq:
            list_of_doc.append(str(each_doc_freq.split(",")[0]))
        count = len(list_of_doc)
        dict_doc_freq[term] = {'doc_list': list_of_doc, 'df': count}
        line = fw.readline()
    return dict_doc_freq


def write_file_df(dict_df, term_type):
    fw = open(pwd + "//" + term_type + "_df_Stem.txt", "w", encoding="utf-8")
    for keys in sorted(dict_df):
        fw.write(str(keys) + " --> (")
        for each in dict_df[keys]['doc_list']:
            fw.write(str(each) + " ")
        fw.write(")-->" + str(dict_df[keys]['df']) + "\n")
    fw.close()


dict_doc = create_df("Unigram")
write_file_df(dict_doc, "Unigram")

# Done with Preprocessing of the indexes
# Declaration of parameters
k1 = 1.2
k2 = 100
b = 0.75
N = 3204
dict_no_terms_doc = {}
dict_term_no_docs = {}
dict_term_doc = {}
dict_doc_score = {}
total = 0
BM25_score_system_name = 'BM25'
# No relevance information hence

# Calculate the average length of the document which is sum of length of documents / N ( Number of documents in the
# corpus)

# Open the document which contains the number of terms in each document
# Its in the format docID-->Number of terms
fo = open("No_of_terms_Stem.txt", 'r', encoding='utf-8')
line = fo.readline().strip()
while line:
    docId = line.split('-->')[0].rstrip().lstrip()
    num_of_terms = line.split('-->')[1].rstrip().lstrip()
    dict_no_terms_doc[docId] = int(num_of_terms)
    total += int(num_of_terms)
    line = fo.readline()
# Find the average length of the document
avdl = total / N

fo.close()
# TO calculate ni easily , store all the data in a dict
# The key of the dict is the docID and the value is number of the '

fo = open("Unigram_df_Stem.txt", 'r', encoding='utf-8')
line = fo.readline().rstrip()
while line:
    term = line.split('-->')[0].strip()
    no_of_doc = int(line.split('-->')[2].strip())
    dict_term_no_docs[term] = no_of_doc
    line = fo.readline()
fo.close()

# Create a dictionary which will be useful to calculate fi
fo = open("Unigram_Stem.txt", 'r', encoding='utf-8')
line = fo.readline().rstrip()
while line:
    term = line.split('-->')[0]
    documents_with_freq = line.split('-->')[1].rstrip()
    dict_term_doc[term] = documents_with_freq
    line = fo.readline()
fo.close()

# Total number of relevant documents for this query
# Dict : key = qid , value = number of relevant documents
dict_qid_rel = {}
# Dict : key = qid , value = list of all relevant dcouments
dict_qid_rel_doc = {}
list_of_all_rel_doc = []
fi = open('cacm.rel.txt', 'r')
line = fi.readline()
while line:
    qid = line.split(" ")[0]
    doc = line.split(" ")[2]
    if qid not in dict_qid_rel.keys():
        dict_qid_rel[qid] = 1
    else:
        dict_qid_rel[qid] += 1
    if qid not in dict_qid_rel_doc.keys():
        dict_qid_rel_doc[qid] = [doc]
    else:
        dict_qid_rel_doc[qid].append(doc)
    if doc not in list_of_all_rel_doc:
        list_of_all_rel_doc.append(doc)
    line = fi.readline()


def calculate_and_writeBM25(Q_func, QId_func):
    print("Calculating BM25 score for  " + Q + " \n")
    dict_doc_score_update = {}
    Q_terms = Q_func.split()

    for each_term in Q_terms:
        list_of_all_docs = []
        dict_doc_freq = {}
        if each_term in dict_term_doc.keys():
            # The term is present in the corpus
            docs_with_freq = dict_term_doc[each_term]
            # Create a list of documents
            list_of_doc_with_freq = docs_with_freq.strip().replace('(', '').replace(')', '*').rstrip('*')
            list_of_doc = list_of_doc_with_freq.rstrip().split('*')
            for each_index in list_of_doc:
                doc = each_index.split(',')[0]
                freq = each_index.split(',')[1]
                dict_doc_freq[doc] = freq
                if doc not in list_of_all_docs:
                    list_of_all_docs.append(doc)
            # Compute the score for each document
            for each_doc in list_of_doc:
                if str(QId_func) not in dict_qid_rel.values():
                    ri = 0
                    R = 0
                else:
                    R = dict_qid_rel[str(QId_func)]
                    if set(dict_qid_rel_doc[str(QId_func)]) & set(list_of_all_docs):
                        ri = len(set(dict_qid_rel_doc[str(QId_func)]) & set(list_of_all_docs))
                    else:
                        ri = 0
                dl = int(dict_no_terms_doc[each_doc.split(',')[0]])
                K = float(k1 * ((1 -     b) + b * (float(dl) / float(avdl))))
                fi = int(dict_doc_freq[each_doc.split(',')[0]])
                qfi = Q_terms.count(each_term)
                ni = dict_term_no_docs[each_term]
                # The formula contains the product of three terms , i call them prod1, prod2, prod3
                prod1 = ((0 + 0.5) / (0.5)) / ((ni + 0.5) / (N - ni + 0.5))
                prod1 = math.log(prod1)
                prod2 = (((k1 + 1) * fi) / (K + fi))
                prod3 = (((k2 + 1) * qfi) / (k2 + qfi))
                score = float(prod1 * prod2 * prod3)
                if each_doc.split(',')[0] in dict_doc_score_update.keys():
                    dict_doc_score_update[each_doc.split(',')[0]] += score
                else:
                    dict_doc_score_update[each_doc.split(',')[0]] = score

    # Sort based on the score
    sorted_dict_doc_freq = sorted(dict_doc_score_update.items(), key=operator.itemgetter(1))
    # Get top 100
    top_100 = sorted_dict_doc_freq[::-1][0:100]
    fw = open(pwd + "//BM25_Scores_Stem.txt", 'a', encoding='utf-8')
    rank = 0;
    fw.write('---------------------Query :' + Q_func + '------------------\n')
    for key, value in top_100:
        rank += 1
        # query_id Q0 doc_id rank BM25_score system_name
        fw.write(str(QId_func )+ " Q0 " + " " + str(key) + " " + str(rank) + " " + str(
            value) + " " + BM25_score_system_name + '\n')
    fw.close()


# Read the query from Queries.txt it should be in the format DocId.DocName
fo = open("cacm_stem.query.txt", 'r', encoding='utf-8')
line = fo.readline()
qid = 1
while line:
    print("READING THE QUERIES...\n")
    QId = qid
    Q = line.strip()
    # Computer the BM25 for Q
    calculate_and_writeBM25(Q, QId)
    line = fo.readline()
    qid += 1
print("---------------------Completed------------")
