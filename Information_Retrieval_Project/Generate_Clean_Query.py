from bs4 import BeautifulSoup
from string import punctuation

# This program generates clean query from the raw query  given to us.
# Open the cacm query text file given to us

fo = open('cacm.query.txt', 'r', encoding="utf-8")
query_with_noise = fo.read()
soup = BeautifulSoup(query_with_noise, 'lxml')
text = soup.find_all('doc')
clean_queries = []
for each_result_set in text:
    query = str(each_result_set.text.strip()).split("\n\n\n")[1]
    # Remove punctuation except hypen
    # Replace with some word which is not common english word to avoid losing data.
    # Encrypting the hyphen with word 'QETUO'
    query = query.replace('-', 'QETUO')
    query = query.translate(str.maketrans('', '', punctuation))
    # Convert to lowe case
    query = query.lower()
    # Remove multiple newline character
    query = query.replace("\n", " ")
    # Trim the tailing and leading white spaces (if any)
    query = query.strip()

    # Replace the substituted string to get the hyphen back
    # Decrypting the data to get the hyphen back
    query = query.replace('qetuo', '-')

    clean_queries.append(query)

fw = open('Clean_Query.txt', 'w', encoding='utf-8')
for num, each_query in enumerate(clean_queries):
    fw.write(each_query)
    if num < len(clean_queries) - 1:
        fw.write("\n")
        # End
fo.close()
fw.close()
