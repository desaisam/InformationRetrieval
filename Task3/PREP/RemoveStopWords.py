# This program removes stop words from both query and corpus

import os
import shutil

pwd = os.getcwd()
# Read the stop word list and store in a list
common_words = []

# This list stores all the queries without stopwords
query_clean = []

fo = open('common_words.txt', 'r')
line = fo.readline()

while line:
    common_words.append(line.strip())
    line = fo.readline()
fo.close()

# Remove stop words from query
# Open the clean query generate from 'Generate_Clean_Query.py'
print('Remove Stop   Words From Query....\n')
query_as_string = ''
fo = open('Clean_Query.txt', 'r', encoding='utf-8')
line = fo.readline()
while line:
    each_query = line.split(' ')
    # Remove common words from each_query
    each_query = [x for x in each_query if x not in common_words]
    for each_term in each_query:
        query_as_string += "".join(each_term) + " "
    query_clean.append(query_as_string.strip())
    query_as_string = ''
    line = fo.readline()
fo.close()

# Write the cleaned queries to a file

fo = open("Query_Without_Stop_Words.txt", 'w')
for num, each in enumerate(query_clean):
    fo.write(str(num + 1) + "." + each)
    if num < len(query_clean) - 1:
        fo.write('\n')
fo.close()

# For lucene

fo = open("Query_Without_Stop_Words_lu.txt", 'w')
for num, each in enumerate(query_clean):
    fo.write(each)
    if num < len(query_clean) - 1:
        fo.write('\n')
fo.close()

if os.path.isdir(pwd + "\\Tokens_Stop"):
    shutil.rmtree((pwd + "\\Tokens_Stop"))
os.makedirs(pwd + "\\Tokens_Stop")
print("Removing Stop words from corpus...\n")
file_contents = ''
each_file_in_list = []
clean_file = []
# Remove stop words from corpus
for each_file in os.listdir(pwd + "\\Tokens"):
    file = open(pwd + "\\Tokens\\" + each_file, encoding="utf8")
    line = file.read()
    each_file_in_list = line.split(' ')
    each_file_in_list = [x for x in each_file_in_list if x not in common_words]
    for each_term in each_file_in_list:
        file_contents += "".join(each_term) + " "
    fi = open(pwd + "\\Tokens_Stop\\" + each_file, 'w')
    fi.write(file_contents)
    # clean_file.append(file_contents.strip())
    file_contents = ''

fo.close()
