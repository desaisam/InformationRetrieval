    # Web crawler using Breadth First search algorithm.
    # author sameerdesai

import lxml as lxml
from bs4 import BeautifulSoup
import requests
import re
import time

# This list contains all the urls meeting all the criteria of the assignment, the text file is updated from this
# list .
master_list = []

# This list contains the all the nodes and its children, as the name suggests its a queue.All the crawled links are
# pushed in the queue .
current_queue = []
# This is the seed url. Acts as a root node in the graph.
seed_url = 'https://en.wikipedia.org/wiki/Space_exploration'
# Making http call to the website and download the source of the page.
res = requests.get(seed_url)
html_text = res.text
# Use beautiful soup library to parsr the html page.
soup = BeautifulSoup(html_text, "lxml")

# for link in soup.find_all('a'):
#  print("https://en.wikipedia.org" + str(link.get('href')))
# Adding delay of one second to respect the politeness policy
# time.sleep(1)
regex = "^/wiki"
base_url = "https://en.wikipedia.org"

# The maximum depth of the tree is 6.
max_depth = 6
# The maximum urls this crawler can crawl is.
max_urls = 1000
current_queue.append(seed_url)


def bfs_crawler():
    depth = 1
    url_count = 0
    while depth < max_depth or url_count < max_urls:
        soup_content = soup.find('div', {'id': 'mw-content-text'})
        for link in soup_content.find_all('a', {'href': re.compile(regex)}):
            if (':' in str(link.get('href'))) or ('JPEG' in str(link.get('href'))) and ('jpg' in str(link.get('href'))):
                continue
            if '#' in str(link.get('href')):
                self_ref_url = str(link.get('href'))
                current_queue.append(self_ref_url.split('#')[0])
                url_count = url_count + 1
            current_queue.append(str(link.get('href')))

    url_count = url_count + 1
    depth = depth + 1


    print("---------CRAWLING AT DEPTH-------" + str(depth) + "\n")
    print("---------URLS CRAWLED AT THIS DEPTH" + str(url_count) + "\n")
bfs_crawler()
