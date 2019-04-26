import os
import re
import time

pwd = os.getcwd()

start = time.time()


def decode(pos_list_new):
    for i in range(len(pos_list_new)):
        pos_list_new[i] = int(pos_list_new[i])
    else:
        pos_list_new[i] = int(pos_list_new[i]) + int(pos_list_new[i - 1])

    return pos_list_new


def conjuctive_proximity(word1, word2, k):
    if not os.path.exists(pwd + '//Task2//'):
        os.mkdir(pwd + '//Task2//')

    doc_name = word1 + "_" + word2 + "_" + str(k) + "_N.txt"
    fh2 = open(pwd + "//Task2//" + doc_name, "w", encoding="utf-8")
    dict_word1 = create_dict_pos(word1)
    dict_word2 = create_dict_pos(word2)

    key_word1, values_word1 = dict_word1.keys(), dict_word1.values()
    key_word2, values_word2 = dict_word2.keys(), dict_word2.values()

    for each_key_word in key_word1:
        delta_list = []
        temp = set()
        if each_key_word in key_word2:
            pos_list = dict_word1[each_key_word]
            pos_list = pos_list[0].split(" ")
            pos_list = decode(pos_list)

            pos_list2 = dict_word2[each_key_word]
            pos_list2 = pos_list2[0].split(" ")
            pos_list2 = decode(pos_list2)

            for each_pos in pos_list:
                for i in range(k):
                    if each_key_word not in temp:
                        if each_pos + i in pos_list2:
                            print("\nFound a document. Writing to a file. . .")
                            temp.add(each_key_word)
                            fh2.write(str(each_key_word) + "\n")
                            break
                        if each_pos - i in pos_list2:
                            print("\nFound a document. Writing to a file. . .")
                            temp.add(each_key_word)
                            fh2.write(str(each_key_word) + "\n")
                            break

    fh2.close()


def create_dict_pos(word):
    dict_doc_pos = {}
    fh = open(pwd + "//Task1//Positional_Index.txt", "r", encoding="utf-8")
    line = fh.readline()
    while line:
        # print(line)
        if str(line).split("-->")[0] == str(word):
            str_doc_pos = str(line).split("-->")[1].rstrip()
            str_list = re.split(r'[()]', str_doc_pos)
            str_list = [str(x).strip() for x in str_list if str(x)]
            str_list = list(filter(None, str_list))
            for each_str in str_list:
                doc_Id = each_str.split(",")[0]
                pos = each_str.split(",")[1:]
                dict_doc_pos[doc_Id] = pos
            line = fh.readline()
        else:
            line = fh.readline()
    return dict_doc_pos


# Uncomment list of documents that contain bothspace and missionwithin k= 6
conjuctive_proximity("space", "mission", 6)

# Uncomment list of documents that contain bothspace and missionwithin k= 12
conjuctive_proximity("space", "mission", 12)

# Uncomment to Find the list of documents that contain bothearthand orbitwithin k=5
conjuctive_proximity("earth", "orbit", 5)

# Uncomment to Find the list of documents that contain bothearthand orbitwithin k=10
conjuctive_proximity("earth", "orbit", 10)

end = time.time()

print("\nTime taken to run this program " + str(end - start) + " seconds")
