# Web crawler using Breadth First search algorithm.
# author sameerdesai


# Used beautiful soup library to parse the HTML page.
from bs4 import BeautifulSoup
import requests
import re
import time
import codecs

start = time.time()
# Frontier acts a queue
frontier_queue = []
# Copy oof frontier to remove duplicates from the queue. There is a trade off between time and space,
# I could have used orderedDict but its slower compared to list.
# Since already a delay is added to respect the politeness policy i believed to compromise space wrt to time.
frontier_queue_copy = []
# The main list which stores all the visited nodes.
url_list = []
depth_counter = 0
max_depth = 6
max_urls = 1000
seed_url = '/wiki/Space_exploration'
seed_depth = (seed_url, depth_counter)
# res = requests.get(seed_url)
# html_text = res.text
# soup = BeautifulSoup(html_text, "lxml")
regex = "^/wiki"
base_url = "https://en.wikipedia.org"
frontier_queue.append([seed_url, 1])
frontier_queue_copy.append(seed_url)


def save_as_html(url):
    fo = codecs.open(url.split("/")[2] + ".html", 'w',"utf-8")
    fo.write(str(requests.get(base_url + url).text))
    fo.close()


def bfs_crawler():
    url_count = 1
    while url_count <= max_urls:

        current_depth = frontier_queue[0][1]
        if current_depth > max_depth:
            break
        # Breadth First search algorithm.
        current_seed = base_url + str(frontier_queue[0][0])
        url_list.append(base_url + frontier_queue.pop(0)[0])
        # Adding politeness of one second
        time.sleep(1)
        res = requests.get(current_seed)
        html_text = res.text
        soup = BeautifulSoup(html_text, "html.parser")
        # Mine only from content portion.
        soup_content = soup.find('div', {'id': 'mw-content-text'})
        for link in soup_content.find_all('a', {'href': re.compile(regex)}):
            # Handle redirect links
            class_type = link.get('class')
            if class_type is not None:
                if str('mw-redirect') in class_type:
                    continue
            # Ignore links of images and :
            if (':' in str(link.get('href'))) or ('JPEG' in str(link.get('href'))) and ('jpg' in str(link.get('href'))):
                continue
            # Avoid duplicates
            if (link.get('href')) in frontier_queue_copy:
                continue
            # Handle subsection of the same page
            if '#' in str(link.get('href')):
                self_ref_url = str(link.get('href'))
                url_count = url_count + 1
                if url_count > max_urls:
                    break

                frontier_queue.append([self_ref_url.split('#')[0], current_depth + 1])
                frontier_queue_copy.append(self_ref_url)
                save_as_html(self_ref_url)
                continue

            url_count = url_count + 1
            # Crawl upto 1000 urls
            if url_count > max_urls:
                break
            frontier_queue.append([str(link.get('href')), current_depth + 1])
            frontier_queue_copy.append(str(link.get('href')))
            save_as_html(str(link.get('href')))
            # Uncomment the below print statements to find out the depth.
            # print("Crawled : " + str(link.get('href')) + " Count : " + str(url_count) + " Depth: " + str(
            #   frontier_queue[0][1]))
    # After crawling 1000 urls , append the remaining urls into the visited list 
    for each_crawled_url in frontier_queue:
          url_list.append(base_url + each_crawled_url[0])
        # print(str(each_crawled_url) + "\n")

    # Uncomment to see the list of all crawled urls in console.
    # for i in url_list:
    #    print(i)
    # Write to a file the list of all crawled urls.
    file = open("bfs_crawler.txt", 'w')
    for i in url_list:
        file.write((str(i)) + "\n")
    file.close()


bfs_crawler()


end = time.time()

print("********TOTAL TIME TAKEN********  " + str(end - start) + "  seconds")
