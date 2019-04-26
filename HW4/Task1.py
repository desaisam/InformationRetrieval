import time
import nltk
import os
import re
import string
import unicodedata
from nltk import ngrams
# Read the
# Tokens from the files
# Timer starts
start = time.time()
pwd = os.getcwd()
dir_path = pwd + '/Corpus'


# Read all the files one by one
all_files = os.listdir(dir_path)
# Lists to store the unigram, bigram and trigram generated
list_unigram = []
list_bigram = []
list_trigram = []
# list_of_pos = []

# dict_freq stores dcoId as key and frequency as values
dict_freq = {}

# dict_unigram, dict_bigram and dict_trigram has key
dict_unigram = {}
dict_bigram = {}
dict_trigram = {}
dict_uni_pos = {}
# dict_posIndex key : Values :
dict_posIndex = {}
# Storing the number of terms in each document as seperate data structure. Here i have chosen a dictionary
dict_no_terms = {}
dict_content = {}


# Create unigrams
def unigram(tokens):
    return list(ngrams(tokens, 1))


# Create bigrams
def bigram(tokens):
    return list(ngrams(tokens, 2))


# Create trigrams
def trigram(tokens):
    return list(ngrams(tokens, 3))


def write_to_file(term_type, dict_term):
    if not os.path.exists(pwd + '//Task1//'):
        os.mkdir(pwd + '//Task1//')
    fw = open(pwd + "//Task1//" + term_type + ".txt", "w", encoding="utf-8")
    # str_index = ""
    for key, values in dict_term.items():
        # str_index += key + "-->"
        fw.write(str(key) + "-->")
        for each_dict in values:
            fw.write("(" + str(each_dict["docId"] + "," + str(each_dict['freq']) + ")"))
            #  str_index += "\n"
        fw.write("\n")
    fw.close()


file_count = 0


# Creating a dictionary to avoid reading files again and again

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


def create_invIndex_unigram(docId_uni, list_unigram_func):
    print("\nCREATING INVERTED INDEX FOR UNIGRAM FOR-->" + docId_uni)
    start_bi = time.time()
    # docId_uni = unicodedata.normalize('NFKD', docId_uni)
    #dict_no_terms[docId_uni] = len(list_unigram_func)
    dict_temp = {}
    counter = 1
    str_doc_content = dict_content[docId_uni]
    # for word in set(str_doc_content.split()):
    # list_of_pos = [w.start() for w in re.finditer(word, str_doc_content)]
    # list_unigram_func = list(unigram(nltk.word_tokenize(str_doc_content)))
    # list_unigram_func = [''.join(each_unigram) for each_unigram in list_unigram_func]
    # set_unigrams = set()
    dict_no_terms[docId] = len(list_unigram_func)
    for index, each_unigram in enumerate(list_unigram_func):
        pos = index + 1
        # list_of_pos = [w.start() for w in re.finditer(each_unigram, str_doc_content)]
        # list_of_pos = [i + 1 for i, x in enumerate(list_unigram) if x == each_unigram]
        # set_unigrams.add()
        # count = list_unigram_func.count(each_unigram)
        # list_of_pos = []
        #list_of_pos = [i + 1 for i, x in enumerate(str_doc_content.split()) if x == each_unigram]
        # custom_dict = {'docId': docId_uni, 'freq': 1, 'pos': list_of_pos}
        if each_unigram not in dict_unigram.keys():
            dict_unigram[each_unigram] = [{'docId' : docId_uni, 'freq': 1,'pos' : [pos]}]
            # list_temp.add(docId_uni)
            # dict_temp[each_unigram] = list_temp
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


def create_invIndex_bigram(docId_bi, list_bigram_func):
    print("\nCREATING INVERTED INDEX FOR BIGRAM FOR-->" + docId_bi)
    start_bi = time.time()
    # list_bigram_func = list(bigram(nltk.word_tokenize(str_doc_content)))
    # set_bigram = set(list_bigram_func)
    # count_bi = list_bigram.count(each_bigram)
    for each_bigram in list_bigram_func:
        # count_bi = list_bigram_func.count(each_bigram)
        # custom_dict = {'docId': docId_bi, 'freq': count_bi}
        each_bigram = each_bigram[0] + " " + each_bigram[1]
        if each_bigram not in dict_bigram.keys():
            dict_bigram[each_bigram] = [{'docId' : docId_bi, 'freq': 1}]
        else:
            for index, each_dict in enumerate(dict_bigram[each_bigram]):
                if docId_bi == each_dict['docId']:
                    temp = index
                    break
                temp = -1

            if temp != -1:
                dict_bigram[each_bigram][temp]['freq'] += 1

            else:
                dict_bigram[each_bigram].append({'docId': docId_bi, 'freq': 1})

    end_bi = time.time()
    print("\nINVERTED INDEX FOR BIGRAM COMPLETE IN " + str(end_bi - start_bi) + " Seconds")


def create_invIndex_trigram(docId_tri, list_trigram_func):
    print("\nCREATING INVERTED INDEX FOR TRIGRAM FOR-->" + docId_tri)
    start_tri = time.time()
    # list_trigram_func = list(trigram(nltk.word_tokenize(str_doc_content)))
    # set_trigram = set(list_trigram_func)
    # count_tr = list_bigram.count(each_trigram)
    for each_trigram in list_trigram_func:
        # count_tr = list_trigram_func.count(each_trigram)
        # custom_dict = {'docId': docId_tri, 'freq': count_tr}
        each_trigram = each_trigram[0] + " " + each_trigram[1] + " "+ each_trigram[2]
        if each_trigram not in dict_trigram.keys():
            dict_trigram[each_trigram] = [{'docId': docId_tri, 'freq': 1}]
        else:
            for index, each_dict in enumerate(dict_trigram[each_trigram]):
                if docId_tri == each_dict['docId']:
                    temp = index
                    break
                temp = -1

            if temp != -1:
                dict_trigram[each_trigram][temp]['freq'] += 1

            else:
                dict_trigram[each_trigram].append({'docId': docId_tri, 'freq': 1})
    end_tri = time.time()
    print("\nINVERTED INDEX FOR TRIGRAM COMPLETE IN " + str(end_tri - start_tri) + " Seconds")


# for each_tokenised_file in all_files:
#     file_count += 1
#     cutom_dict = {}
#     fh = open(dir_path + '\\' + each_tokenised_file, 'r', encoding='utf-8')
#     docId = each_tokenised_file[:-4]
#     docId = docId.replace("(", "")
#     docId = docId.replace(")", "")
#     str_doc_content = str(fh.read().lower())
#     list_unigram = list(unigram(nltk.word_tokenize(str_doc_content)))
#     list_unigram = [''.join(each_unigram) for each_unigram in list_unigram]
#     fh.seek(0)
#     list_bigram = list(bigram(nltk.word_tokenize(str_doc_content)))
#     # list_bigram = [[(str(x).lower(), str(y).lower()) for x, y in element ] for element in list_bigram]
#     fh.seek(0)
#     list_trigram = list(trigram(nltk.word_tokenize(str_doc_content)))
#     fh.close()
#
#     # Task 1b) Calculate the number of each terms in the document
#     # Sum of length of list_unigram + list_bigram + list_trigram
#
#     terms_in_each_document = len(list_unigram) + len(list_bigram) + len(list_trigram)
#     dict_no_terms[docId] = terms_in_each_document
#
#     # Build inverted index for each unigram in the current file
#     # docId_inside_list = ""
#     set_unigrams = set(list_unigram)
#     for each_unigram in set_unigrams:
#         # each_unigram_cleaned = ''.join(each_unigram)
#         count = list_unigram.count(each_unigram)
#         list_of_pos = [i + 1 for i, x in enumerate(list_unigram) if x == each_unigram]
#         if docId in "":
#             continue
#         if "," in docId:
#             docId = docId.replace(",", "")
#         custom_dict = {'docId': docId, 'freq': count, 'pos': list_of_pos}
#         if each_unigram not in dict_unigram.keys():
#             dict_unigram[each_unigram] = [custom_dict]
#         else:
#             dict_unigram[each_unigram].append((custom_dict))
#     print("\nBigram Index Begins")
#     set_bigram = set(list_bigram)
#     print("\nDone with Unigram..")
#     for each_bigram in set_bigram:
#         count = list_bigram.count(each_bigram)
#         if "," in docId:
#             docId = docId.replace(",", "")
#         # list_of_pos = [i + 1 for i, x in enumerate(list_bigram) if x == each_bigram]
#         custom_dict = {'docId': docId, 'freq': count}
#         if each_bigram not in dict_bigram.keys():
#             dict_bigram[each_bigram] = [custom_dict]
#         else:
#             dict_bigram[each_bigram].append(custom_dict)
#
#     print("\nDone with Bigram..")
#
#     # Removes duplicates
#     set_trigram = set(list_trigram)
#     print("\nTrigram Index Begins")
#     for each_trigram in set_trigram:
#
#         count = list_trigram.count(each_trigram)
#         # list_of_pos = [i + 1 for i, x in enumerate(list_trigram) if x == each_trigram]
#         if "," in docId:
#             docId = docId.replace(",", "")
#         custom_dict = {'docId': docId, 'freq': count}
#         if each_trigram not in dict_bigram.keys():
#             dict_trigram[each_trigram] = [custom_dict]
#         else:
#             dict_trigram[each_trigram].append(dict(custom_dict))

def write_posInd(dict_unigram_pos):
    fw = open(pwd + "//Task1//" + "Positional_Index.txt", "w", encoding="utf-8")
    # str_index += key + "-->"
    for key , value in dict_unigram_pos.items():
        fw.write(str(key) + "-->")
        for each_dict in value:
            # str(each_dict["docId"]).replace("(", "")
            # str(each_dict["docId"]).replace(")", "")
            fw.write(str("( " + str(each_dict["docId"]) + ","))
            #
            for index, item in enumerate(each_dict["pos"]):
                if index == 0:
                    fw.write(str(item) + " ")
                else:
                    fw.write(str(each_dict["pos"][index] - each_dict["pos"][index - 1]) + " ")

            # for each_pos in each_dict["pos"]:
            #     fw.write(str(each_pos) + " ")
            fw.write(")")
            #  str_index += "\n"
        fw.write("\n")
    fw.close()


dict_content = create_dictionary_files()
exclude = set(string.punctuation)
for docId, str_doc_content in dict_content.items():
    list_unigram = list(unigram(nltk.word_tokenize(str_doc_content)))
    # Remove punctutation
    list_unigram = [''.join(each_unigram) for each_unigram in list_unigram if each_unigram not in exclude]
    # list_bigram = list(bigram(nltk.word_tokenize(str_doc_content)))
    # list_trigram = list(trigram(nltk.word_tokenize(str_doc_content)))
    create_invIndex_unigram(docId, list_unigram)
    # create_invIndex_bigram(docId, list_bigram)
    create_invIndex_trigram(docId, list_trigram)


print("\nWRITING UNIGRAM INV INDEX TO A FILE")
write_to_file("Unigram", dict_unigram)
# dict_bigram_re = create_invIndex_bigram(dict_content)
print("\nWRITING BIGRAM INV INDEX TO A FILE")
write_to_file("Bigram", dict_bigram)
# dict_trigram_re = create_invIndex_trigram(dict_content)
print("\nWRITING TRIGRAM INV INDEX TO A FILE")
write_to_file("Trigram", dict_trigram)
print("\nWRITING POSITIONAL INV INDEX TO A FILE")
write_posInd(dict_unigram)

if not os.path.exists(pwd + '//Task1//'):
    os.mkdir(pwd + '//Task1//')
fw2 = open(pwd + "//Task1//No_of_terms.txt", "w", encoding="utf-8")
print("\nWRITING NO OF TERMS TO A FILE")
for keys,values in dict_no_terms.items():
    fw2.write(str(keys)+"-->"+str(values) + "\n")
fw2.close()
end = time.time()

print("\nTotal Time taken : " + str((end - start) / 60) + "minutes")
# import winsound
#
# frequency = 2500  # Set Frequency To 2500 Hertz
# duration = 2000  # Set Duration To 1000 ms == 1 second
# winsound.Beep(frequency, duration)
