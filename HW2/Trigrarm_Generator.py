# Please run the Tokenization.py before running this .
import numpy as np
import os
from nltk.util import trigrams
pwd = os.getcwd()
trigrams_map = {}
# temp lst
temp = []
tokens_to_text = " "
count = 0
index = 1
for each_file in os.listdir(pwd + "/Tokens/"):
    file = open(pwd + "\\Tokens\\" + each_file, encoding="utf8")

    temp = temp + list(trigrams(file.read().split()))

print(len(temp))
# for each in temp:
#     if each not in trigrams_map.values():
#         trigrams_map[each] = 1
#         print(count)
#         count +=1
#
#     else:
#         trigrams_map[each] += 1
#         break
from collections import Counter


for each in set(temp):
        trigrams_map[each] = temp.count(each)
#         print(trigrams_map.values())
# print(trigrams_map.keys()[0])

fo  = open("Trigrams.txt", "w")

for key, values in trigrams_map.items():
    fo.write(key , values +"\n")

import numpy as np
import matplotlib.pyplot as plt

