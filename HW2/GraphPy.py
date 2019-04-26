import requests
from bs4 import BeautifulSoup
import os
import re
from collections import defaultdict

node_dict_bfs = defaultdict(set)
node_dict_focus = defaultdict(set)
graph_dict_bfs = defaultdict(list)
graph_dict_focus = defaultdict(list)

# Open the files
# fh_bfs = open("BFS.txt", "r")
fh_focus = open("FOCUSED.txt", "r")

# List which holds all the urls
list_of_files_bfs = []
list_of_files_focus = []

# Read each url line by line
# url_bfs = fh_bfs.readline()
url_focus = fh_focus.readline()

# Get the current working directory
pwd = os.getcwd()
print("READING EACH FILE.....\n")
# while str(url_bfs):
#     list_of_files_bfs.append(url_bfs.rstrip().split('https://en.wikipedia.org/wiki/')[1] + ".html")
#     url_bfs = fh_bfs.readline()

while str(url_focus):
    list_of_files_focus.append(url_focus.rstrip().split('https://en.wikipedia.org/wiki/')[1] + ".html")
    url_focus = fh_focus.readline()

print("BEGINNING TO SCRAP THE PAGES.....\n")
# for each_file in os.listdir(pwd + "/Urls/"):
#     with open(pwd + "\\Urls\\" + each_file, encoding="utf8") as f:
#         t = f.read()
# # print(t)
#     file = open(pwd + "\\Urls\\" + each_file, encoding="utf8")
#     with open(pwd + "\\Urls\\" + each_file, encoding="utf8") as f:
#         soup = BeautifulSoup(f.read(), 'html.parser')
#         content = soup.find('div', {'id': 'mw-content-text'})
#         for link in content.find_all('a', {'href': re.compile("^/wiki")}):
#             urls = link.get('href').split("#")[0]
#             page_id = urls.split("/wiki/")[1]
#             node_dict_bfs[each_file].add(page_id)










print("DONE WITH SCRAPPING.....\n")
for each_file in os.listdir(pwd + "/Urls/FOCUS/"):
    # with open(pwd + "\\Urls\\" + each_file, encoding="utf8") as f:
    #     t = f.read()
    # print(t)
    # file = open(pwd + "\\Urls\\" + each_file, encoding="utf8")
    with open(pwd + "\\Urls\\FOCUS\\" + each_file, encoding="utf8") as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        content = soup.find('div', {'id': 'mw-content-text'})
        for link in content.find_all('a', {'href': re.compile("^/wiki")}):
            urls = link.get('href').split("#")[0]
            page_id = urls.split("/wiki/")[1]
            node_dict_focus[each_file].add(page_id)
    # link = soup.find_all("a", {'href': re.compile("^/wiki")})

# print(node_dict)

# for k, v in node_dict.items():
#     print(v)
print("SIGH...\n")
print("WRITING THE GRAPH INTO A FILE......")
# for each_link in list_of_files_bfs:
#     for keys, values in node_dict_bfs.items():
#         if each_link.split('.html')[0] in values:
#             graph_dict_bfs[each_link.split('.html')[0]].append(str(keys).split('.html')[0])
print("DONE WRITING THE GRAPH\n")

for each_link in list_of_files_focus:
    for keys, values in node_dict_focus.items():
        if each_link.split('.html')[0] in values:
            graph_dict_focus[each_link.split('.html')[0]].append(str(keys).split('.html')[0])

max_deg = 0

# print(graph_dict_bfs)

# fo = open("G1.txt", 'w')
# for each_node, incoming_nodes in graph_dict_bfs.items():
#     fo.write(str(each_node) + " ")
#     for each_incoming_node in incoming_nodes:
#         fo.write(str(each_incoming_node) + " ")
#     fo.write("\n")
# fo.close()


fo = open("G2.txt", 'w')
for each_node, incoming_nodes in graph_dict_focus.items():
    fo.write(str(each_node) + " ")
    for each_incoming_node in incoming_nodes:
        fo.write(str(each_incoming_node) + " ")
    fo.write("\n")
fo.close()
