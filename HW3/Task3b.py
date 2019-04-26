import os
import time
import re


start = time.time()
pwd = os.getcwd()


def create_df(term_type):
    dict_doc_freq = {}
    fw = open(pwd + "\\Task1\\" + term_type + ".txt", 'r', encoding="utf-8")
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


def write_file(dict_df, term_type):
    if not os.path.exists(pwd + '//Task3//'):
        os.mkdir(pwd + '//Task3//')
    fw = open(pwd + "//Task3//" + term_type + "_df.txt", "w", encoding="utf-8")
    for keys in sorted(dict_df):
        fw.write(str(keys) + " --> (")
        for each in dict_df[keys]['doc_list']:
            fw.write(str(each) + " ")
        fw.write(")-->" + str(dict_df[keys]['df']) + "\n")
    fw.close()

print("\nCREATING  DOCUMENT FREQUENCY FOR UNIGRAM")
dict_doc = create_df("Unigram")
write_file(dict_doc, "Unigram")
print("\nCREATING  DOCUMENT FREQUENCY FOR BIGRAM")
dict_doc = create_df("Bigram")
write_file(dict_doc, "Bigram")
print("\nCREATING  DOCUMENT FREQUENCY FOR TRIGRAM")
dict_doc = create_df("Trigram")
write_file(dict_doc, "Trigram")
end = time.time()
print("\nTOTAL TIME TAKEN  " +str(end-start)+ " seconds")