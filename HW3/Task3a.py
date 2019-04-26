import os
import time
import re
import operator

start = time.time()
pwd = os.getcwd()


def create_tf(term_type):
    dict_term_freq = {}
    fw = open(pwd + "\\Task1\\" + term_type + ".txt", 'r', encoding="utf-8")
    line = fw.readline()

    while line:
        count = 0
        term = line.split("-->")[0]
        # Calculate the frequency
        str_doc_freq = line.split("-->")[1].strip()
        str_freq = re.split(r'[()]', str_doc_freq)
        str_freq = [str(x).strip() for x in str_freq if str(x) != ","]
        str_freq = list(filter(None, str_freq))
        for each_doc_freq in str_freq:
            if len(each_doc_freq.split(",")) > 1:
                count += int(each_doc_freq.split(",")[1])
        dict_term_freq[term] = count
        # print("")
        line = fw.readline()
    dict_term_freq = sorted(dict_term_freq.items(), key=operator.itemgetter(1), reverse=True)
    fw.close()
    # Sort the dictionary
    return dict_term_freq


def write_to_file(dict_tf, term_type):
    if not os.path.exists(pwd + '//Task3//'):
        os.mkdir(pwd + '//Task3//')
    fw = open(pwd + "//Task3//" + term_type + "_tf.txt", "w", encoding="utf-8")
    for keys in dict_tf:
        fw.write(str(keys[0]) + " : " + str(keys[1]) + "\n")
    fw.close()


# Create a tf table for unigram
print("\nCreating tf  table")
dict_term_freq = create_tf("Unigram")

# Write to a file
print("\nWriting the tf table to a file ")
write_to_file(dict_term_freq, "Unigram")

# Create a tf table for bigram
print("\nCreating tf  table")
dict_term_freq = create_tf("Bigram")

# Write to a file
print("\nWriting the tf table to a file ")
write_to_file(dict_term_freq, "Bigram")

# Create a tf table for trigram
print("\nCreating tf  table")
dict_term_freq = create_tf("Trigram")

# Write to a file
print("\nWriting the tf table to a file ")
write_to_file(dict_term_freq, "Trigram")

end = time.time()

print("\nTotal time taken--->" + str(end-start) + "Seconds")