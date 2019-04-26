from bs4 import BeautifulSoup
import nltk
import os

pwd = os.getcwd()
import nltk.tokenize

if not os.path.exists(pwd + '//STEM_CORPUS//'):
    os.mkdir(pwd + '//STEM_CORPUS//')
string_body = ''
file = open('cacm_stem.txt', 'r', encoding="utf8")
# Read everything
text = file.read().strip()
str_content = ''
for each in text.split('#'):
    if each != "":
        docId = each.replace('\n', " ").strip().split(" ")[0]
        docId = docId.zfill(4)
        content = each.replace('\n', " ").strip().split(" ")[1:]
        for each in content:
            str_content += " " + each
        fo = open(pwd + "//STEM_CORPUS//" + "CACM-" + docId + '.txt', 'w')
        print('Creating file ' + docId + '\n')
        fo.write(str_content.strip())
        str_content = ''

