# Web crawler using Breadth Depth  First search algorithm.
# author sameerdesai

# import lxml as lxml
# Used beautiful soup library to parse the HTML page.
from bs4 import BeautifulSoup
import requests
import re
import time
import codecs

start = time.time()
# The main stack which has the webpages along with the information of its depth
frontier_stack = []
# The final list which stores the urls , used to write them into files
url_list = []
# Counter which tracks the depth of the tree
depth_counter = 0
max_depth = 6
# Init the counter to 1
url_count = 1
max_urls = 1000
seed_url = '/wiki/Space_exploration'
regex = "^/wiki"
base_url = "https://en.wikipedia.org"
frontier_stack.append([seed_url, 1])
# Copy of the frontier stack to remove the duplicates.
frontier_queue_copy = []


def save_as_html(url):
    fo = codecs.open(url.split("/")[2] + "_dfs.html", 'w', "utf-8")
    fo.write(str(requests.get(base_url + url).text))
    fo.close()


def dfs_crawler(current_root):
    global url_count
    # current_depth = frontier_stack[-1][1]
    # current_depth = current_root[1]
    # Base case 1 : stop when maximum depth is reached.
    if current_root[1] > 5:
        return

    # current_root = base_url + current_root
    current_root_url = base_url + current_root[0]
    # Adding politeness of one second
    time.sleep(1)
    res = requests.get(current_root_url)

    html_text = res.text
    soup = BeautifulSoup(html_text, "html.parser")
    soup_content = soup.find('div', {'id': 'mw-content-text'})
    for link in soup_content.find_all('a', {'href': re.compile(regex)}):
        if url_count > max_urls:
            break
        # Handle redirect links
        class_type = link.get('class')
        if class_type is not None:
            if str('mw-redirect') in class_type:
                continue
        # Ignore links of images and :
        if (':' in str(link.get('href'))) or ('JPEG' in str(link.get('href'))) and ('jpg' in str(link.get('href'))):
            continue
        # Avoid duplicates.
        if (link.get('href')) in frontier_queue_copy:
            continue
        # Handle subsection of the same page
        # if '#' in str(link.get('href')):
        #    self_ref_url = str(link.get('href'))
        #    url_count = url_count + 1
        #    if url_count > max_urls:
        #        break
        #   frontier_stack.append([self_ref_url.split('#')[0], current_root[1] + 1])
        current_url = str(link.get('href'))

        url_count = url_count + 1
        # Stop crawling when maximum is reached
        if url_count > max_urls:
            break
        # Handle subsection of the same page
        # Uncomment the following three lines to download the crawled html files
        fo = codecs.open(current_url.split("/")[2] + "_dfs.html", 'w', "utf-8")
        fo.write(str(requests.get(base_url + current_url).text))
        fo.close()
        frontier_stack.append([current_url.split('#')[0], current_root[1] + 1])
        frontier_queue_copy.append(current_url)

        current_depth = current_root[1] + 1
        # Recursively call the dfs_crawler by passing new root every time until the depth is six
        dfs_crawler([current_url, current_depth])
    # Base case 2 , when the node has crawled all the links.This functions call returns to previous function call,
    # so that the previous node will crawl the remaining links.
    return


dfs_crawler([seed_url, 1])

for each_crawled_url in frontier_stack:
    url_list.append(base_url + each_crawled_url[0])
    # print(each_crawled_url)
    # Uncomment to see the list of all crawled urls and corresponding depth in console.
    #   for i in url_list:
    #    print(i)
    # Write to a file the list of all crawled urls.
file = open("dfs_crawler.txt", 'w')
for i in url_list:
    file.write((str(i)) + "\n")
file.close()

end = time.time()

print("********TOTAL TIME TAKEN********  " + str(end - start) + "  seconds")
