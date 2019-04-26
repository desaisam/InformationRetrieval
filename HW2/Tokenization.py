import requests
import os
import shutil
import codecs
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
import nltk
from bs4.element import Comment

nltk.download('punkt')

# Default settings perform both puncuaate and case fold
punctuate = True
casefold = True

# List which has all the name of the files
# list_of_files = ['Garc%C3%ADa_Jofre_de_Loa%C3%ADsa.html']
list_of_files = []
list_of_files_focus = []
# Build a String with the desired elements
title_for_tokenizer = ""
read_file = open("BFS.txt", "r")
url = read_file.readline()
pwd = os.getcwd()

read_file_focus = open("FOCUSED.txt", "r")

# print(os.getcwd())
# if os.path.isdir(pwd + "\\Urls"):
#     shutil.rmtree((pwd + "\\Urls"))
# os.makedirs(pwd + "\\Urls\\BFS")
# print("Downloading Document \n......")
#
# while url.rstrip():
#     # print(url.split("https://en.wikipedia.org/wiki/")[1].rstrip())
#     split_until_wiki = url.split("https://en.wikipedia.org/wiki/")[1]
#     # Need to remove special characters from the path
#     if "/" in split_until_wiki:
#         fresh_url = ""
#         for str1 in split_until_wiki.split("/"):
#             fresh_url += str1.rstrip() + "_"
#         split_until_wiki = fresh_url
#     file_name = split_until_wiki.rstrip()
#     file_path = os.path.join(os.getcwd() + "\\Urls\\BFS", file_name).rstrip()
#     # write_file = open(file_path, "w")
#     write_file = codecs.open(file_path + ".html", 'w', "utf-8")
#     write_file.write(str(requests.get(url.rstrip()).text).rstrip())
#     # print(file_name)
#     list_of_files.append(file_name + ".html")
#     # print (list_of_files)
#     url = read_file.readline()
#
# read_file.close()
# # print(fh.read())


read_file_focus = open("FOCUSED.txt", "r")
url = read_file_focus.readline()
pwd = os.getcwd()

print(os.getcwd())

os.makedirs(pwd + "\\Urls\\FOCUS")
print("Downloading Document \n......")

while url.rstrip():
    # print(url.split("https://en.wikipedia.org/wiki/")[1].rstrip())
    split_until_wiki = url.split("https://en.wikipedia.org/wiki/")[1]
    # Need to remove special characters from the path
    if "/" in split_until_wiki:
        fresh_url = ""
        for str1 in split_until_wiki.split("/"):
            fresh_url += str1.rstrip() + "_"
        split_until_wiki = fresh_url
    file_name = split_until_wiki.rstrip()
    file_path = os.path.join(os.getcwd() + "\\Urls\\FOCUS", file_name).rstrip()
    # write_file = open(file_path, "w")
    write_file_focus = codecs.open(file_path + ".html", 'w', "utf-8")
    write_file_focus.write(str(requests.get(url.rstrip()).text).rstrip())
    # print(file_name)
    list_of_files_focus.append(file_name + ".html")
    # print (list_of_files_focus)
    url = read_file_focus.readline()

read_file.close()


# Read the each document from the path.
# Tokenisation begins from here
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

#
# print("Starting Generate Tokens....\n")
# if os.path.isdir(pwd + "\\Tokens"):
#     shutil.rmtree((pwd + "\\Tokens"))
# os.makedirs(pwd + "\\Tokens")
#
# string_for_title = ""
# string_body = ""
# string_anchor = ""
# string_content = ""
#
# for each_file in os.listdir(pwd + "/Urls/BFS/"):
#     file = open(pwd + "\\Urls\\BFS\\" + each_file, encoding="utf8")
#     soup = BeautifulSoup(file.read(), 'html.parser')
#     texts = soup.findAll(text=True)
#     visible_texts = filter(tag_visible, texts)
#     # Get the title from Beautiful Soup
#     # Uncomment below line to fetch all the text content of the html page
#     # This process consumes lot of time, hence commented for *TESTING PURPOSE ONLY*
#     string_body += u" ".join(t.strip() for t in visible_texts)
#
#     title = soup.find('title').string
#     string_for_title = (str(title).split("- Wikipedia")[0])
#     # print(tokenizer.tokenize(title_for_tokenizer))
#     content = soup.find('div', {'id': 'mw-content-text'})
#     for link in content.find_all('a'):
#         title = link.get('title')
#         if title is None:
#             continue
#         string_anchor += title + " "
#
#     content = soup.find('div', {'id': 'mw-content-text'})
#     for link in content.find_all('p'):
#         title = link.get('title')
#         if title is None:
#             continue
#         string_content += title + " "
#
#     final_string = string_for_title + string_anchor + string_body
#     tokenizer = RegexpTokenizer(r'\w+')
#     output_string = ""
#     nltk_tokens = tokenizer.tokenize(final_string)
#     token_list = list(set(nltk_tokens))
#     # Check for duplicates here
#     for token_as_string in token_list:
#         output_string += token_as_string + " "
#
#     if casefold:
#         output_string.casefold()
#     if punctuate:
#         if output_string[((len(output_string)) - 1):(len(output_string))] == ",":
#             output_string = output_string[:(len(output_string) - 1)]
#     fo = open(pwd + "\\Tokens\\" + each_file.split(".html")[0] + ".txt", "a", encoding="utf8")
#     for each_string in output_string:
#         fo.write(each_string)
#     fo.close()
#     print("Just wrote to File \n")
#     final_string = " "
#     string_for_title = ""
#     string_body = ""
#     string_anchor = ""
#     string_content = ""
