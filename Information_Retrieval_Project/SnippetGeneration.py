# Performing Snippet generation

# Read the RAW html from the corpus
import os
import bs4
from bs4 import BeautifulSoup
import string
import operator

dict_doc_snippet = {}
dict_qId_query = {}
string_body = ""
pwd = os.getcwd()
sentences = []
# Key = Sentence , value - signficant factor
dict_senteces = {}
# Read the stop words and store in a list
list_common_words = []
dict_inv_index = {}
translator = str.maketrans('', '', string.punctuation)

fo = open('common_words.txt')
line = fo.readline()
while line:
    list_common_words.append(line.strip())
    line = fo.readline()
fo.close()
# Store the index in  a dict . key = term , value = docId with Frequency
fo = open('Unigram.txt')
line = fo.readline()
while line:
    term = line.split("-->")[0]
    docId = line.split("-->")[1]
    dict_inv_index[term] = docId
    line = fo.readline()
fo.close()

# Store the query in a dict . Key = QId , value = query

fo = open('Clean_Query.txt')
line = fo.readline()
i = 1
while line:
    dict_qId_query[i] = line.strip()
    i += 1
    line = fo.readline()

# Create a dict , key = Qid , value = list of relevant documents
dict_qid_doc = {}
fo = open('LUCENE_Results.txt')
line = fo.readline()
while line:
    if line != "":
        Qid = line.strip().split(' ')[0]
        doc = line.strip().split(' ')[2]
        if Qid not in dict_qid_doc:
            dict_qid_doc[Qid] = [doc]
        else:
            dict_qid_doc[Qid].append(doc)
    line = fo.readline()
dir_path = pwd + "//Snippets//"
if not os.path.exists(dir_path):
    os.mkdir(dir_path)


def calculate_sig(each_sentence, sd, docID):
    fdw = 0
    # split the senteces
    split_setences = each_sentence.strip().split(' ')
    split_setences = list(filter(None, split_setences))
    # Check if each word is a significant word
    # A word is a significant word if frequency of word i
    window_of_words = []
    for each_word in split_setences:

        if each_word.lower() not in list_common_words:
            if sd < 25:
                fdw = 3 - 0.1 * (25 - sd)
            elif 25 <= sd <= 40:
                fdw = 3
            else:
                fdw = 3 + 0.1 * (40 - sd)
            if each_word.lower() in dict_inv_index:
                docId_with_freq = dict_inv_index[each_word.lower()]
                docId_with_freq = docId_with_freq.replace('(', '')
                docId_with_freq = docId_with_freq.replace(')', " ")
                docId_with_freq = docId_with_freq.strip()
                # For this term, create  a dict with key = docId and value frequency
                dict_doc_freq = {}
                list_of_doc_freq = docId_with_freq.split(" ")
                for each_doc_with_freq in list_of_doc_freq:
                    dict_doc_freq[each_doc_with_freq.split(',')[0]] = each_doc_with_freq.split(',')[1]
                if docID.strip() not in dict_doc_freq:
                    freq = 0
                else:
                    freq = dict_doc_freq[docID.strip()]
                if float(freq) > fdw:
                    window_of_words.append('s')
                else:
                    window_of_words.append('w')

    num_significant_words = window_of_words.count('s')
    window_length = len(window_of_words)
    if window_length != 0:
        significant_factor = (num_significant_words * num_significant_words) / window_length
    else:
        significant_factor = 0
    return significant_factor


def highlight_and_write(dict_snippet, query_id):
    # Get the query from query_id
    query = dict_qId_query[int(query_id)]
    query_words = query.split(" ")
    print("Highlighting and writing for query --> " + query + "\n")
    fo = open(dir_path + '//SNIPPET_FOR_QUERY_' + qid + '.txt', 'a', encoding='utf-8')

    # Get the documents retrieved for that query
    rel_doc = dict_qid_doc[query_id]
    # for each document in the retrived list , write the snippet
    for each_rel_doc in rel_doc:
        query_highlight_sentece = []
        processed_snippet = ""
        fo.write("\n==============================================================\n")
        fo.write("SNIPPET FOR DOCUMENT:  " + each_rel_doc + "\n")
        snippet_text = dict_snippet[each_rel_doc]
        snippet_text = str(snippet_text).replace("\n", " ")
        snippet_text = str(snippet_text).replace("  ", " ")
        for each_word in snippet_text.split(" "):
            if each_word == "...":
                query_highlight_sentece.append("\n" + each_word)
            else:
                if each_word.lower() in query_words and each_word.lower() not in list_common_words:
                    query_highlight_sentece.append("***" + each_word + "***")
                else:
                    query_highlight_sentece.append(each_word)

        for each in query_highlight_sentece:
            processed_snippet += each + " "

        fo.write(processed_snippet)


fo.close()

for qid, list_doc in dict_qid_doc.items():
    print("Generating Snippets for " + qid)
    for each_doc in list_doc:
        each_file = each_doc + ".html"
        snippet = ""
        window_of_words = []
        dict_senteces = {}
        # Get each file
        file = open(pwd + "\\RAW_HTML\\" + each_file, 'r', encoding='utf-8')
        soup = BeautifulSoup(file.read(), 'html.parser')
        texts = soup.find('html').text
        texts = str(texts)
        # Remove everything after PM or AM because its just number
        pm_ind = texts.rfind("PM")
        am_ind = texts.rfind("AM")
        if am_ind > pm_ind:
            strip_from = am_ind
        else:
            strip_from = pm_ind
        texts = texts[:(strip_from + 2)]
        # texts = texts.replace(":", " ")
        sentences = texts.split(".")
        # Remove the empty string which is present because of multiple new line character
        sentences = list(filter(None, sentences))
        sentences = [str(x).replace('-', ' ') for x in sentences]
        sentences = [str(x).translate(translator) for x in sentences]
        #  sentences = [str(x).replace('QETUO', '-') for x in sentences]
        # At this stage we have all the senteces for a given document
        # Now compute the significant sentences and chose top three significant senteces for the snippet generation
        sd = len(sentences)
        for each_sentence in sentences:
            # Calculate Significant factor
            significant_factor = calculate_sig(each_sentence, sd, each_doc)
            dict_senteces[each_sentence] = significant_factor
        # Sort the senteces bsaed on value
        sorted_dict = sorted(dict_senteces.items(), key=operator.itemgetter(1), reverse=True)
        # Extract top two sentences
        top_two = sorted_dict[:2]
        for num, each_tuple in enumerate(top_two):
            # Partial Sentence --> 20 words
            if len(each_tuple[0].lower().strip().split()) > 18:
                snippet += " ".join(each_tuple[0].lower().strip().split()[:18])
            else:
                snippet += each_tuple[0].lower().strip()
            if num == 0:
                snippet += " ... "
        # Store the document and its snippet in a dictionary to prevent creating the snippet again
        if each_doc not in dict_doc_snippet:
            dict_doc_snippet[each_doc] = snippet
    highlight_and_write(dict_doc_snippet, qid)
print("---------------Done------------------")
