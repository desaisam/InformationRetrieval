# Generate the corpus using the raw html
import requests
import os
import shutil
import codecs
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
import nltk
from bs4.element import Comment
from string import punctuation

nltk.download('punkt')

# Default settings perform both puncuate and case fold
punctuate = True
casefold = True

list_of_files = []
list_of_files_focus = []
# Build a String with the desired elements
title_for_tokenizer = ""
pwd = os.getcwd()


# Tokenization begins from here
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


# Method which removes duplicates whilst preserving the order
def remove_dupliates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


print("Starting Generate Tokens....\n")
if os.path.isdir(pwd + "\\Tokens"):
    shutil.rmtree((pwd + "\\Tokens"))
os.makedirs(pwd + "\\Tokens")

string_for_title = ""
string_body = ""
string_anchor = ""
string_content = ""

for each_file in os.listdir(pwd + "\\RAW_HTML"):
    file = open(pwd + "\\RAW_HTML\\" + each_file, encoding="utf8")
    soup = BeautifulSoup(file.read(), 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    # Get the title from Beautiful Soup
    string_body += u" ".join(t.strip() for t in visible_texts)
    # Generate Tokens
    final_string = string_body
    tokenizer = RegexpTokenizer(r'\w+')
    output_string = ""
    nltk_tokens = tokenizer.tokenize(final_string)

    # Remove Duplicates

    token_list = remove_dupliates(nltk_tokens)
    # Check for duplicates here
    for token_as_string in token_list:
        output_string += token_as_string + " "

    if casefold:
        output_string = output_string.lower()
    if punctuate:
        output_string.replace('-', 'qetuo')
        output_string = output_string.translate(str.maketrans('', '', punctuation))
        output_string.replace('qetuo', '-')
    fo = open(pwd + "\\Tokens\\" + each_file.split('.html')[0] + ".txt", "a", encoding="utf8")
    for each_string in output_string:
        fo.write(each_string)
    fo.close()
    print("Finished writing to file... \n")
    # Resetting all the values for the next iterations
    final_string = " "
    string_for_title = ""
    string_body = ""
    string_anchor = ""
    string_content = ""
