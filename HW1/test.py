
# CRAWLING USING DFS

import requests
from bs4 import BeautifulSoup
import time
import re


visited = []
frontier = []
max_links =1000
max_depth = 6

# For storing the max depth
depth = 0

# words to be excluded from the url
excluded = ['mailto:', 'favicon', '.ico', ':',
            '.jpg', '.jpeg', '.png', '.gif', '#', '?',	
            '.pdf', '.doc']

# opening the file before starting execution
filename = 'Dfs.txt'
openfile = open(filename, 'w')


# This function first gets the desired urls and then crawls them in DFS order
# Seed_pack stores the URL and it's current depth from the seed
def clean_and_crawl(seed_pack):
    # Depth is a global variable used to store the current depth.
    global depth
    # fetching url to be crawled
    seed = seed_pack[0]
    # fetching the depth
    depth_t = seed_pack[1]
    if depth_t > max_depth:
        return
    # politeness policy
    time.sleep(1)
    page = requests.get(seed)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Getting links only from the content block and not the links from the left margin or the footer.
    content = soup.find('div', {'id': 'mw-content-text'})

    # Getting only the links that start with /wiki
    for link in content.find_all('a', {'href': re.compile("^/wiki")}):

        # Ignoring the data in urls post #
        urls = link.get('href').split('#')[0]

        # Ignoring images, files with ':' etc. Check excluded list.
        if not any(word in urls for word in excluded):
            classes = link.get('class')

            # Ignoring page redirects
            if (classes == None) or (not 'mw-redirect' in link.get('class')):

                # continue only if the given url is not visited
                if urls not in visited:

                    # if we have not already crawled 1000 urls
                    if len(visited) < max_links:
                        urls = "https://en.wikipedia.org" + urls

                        # create the new url pack with the url and depth
                        url_pack = [urls, depth_t + 1]

                        # if the next url is not on a depth greater than max depth,
                        # only then continue
                        if depth_t + 1 <= max_depth:

                            # append the url_pack to frontier
                            frontier.append(url_pack)

                            # update the max depth
                            depth = depth_t

                            # crawl the url, calling DFS recursively
                            dfs(url_pack)


# This function is called recursively for crawlable urls from clean and crawl.
# There is mutual recursion between the two functions.
def dfs(url):

    depth = url[1]
    if depth > max_depth:
        return
    if(len(visited)  >= max_links):
        return

    if url[0] not in visited:
        # append the url_pack to visited
        visited.append(url[0])
        # write the url to the text file
        row = str(url[0]) + "\n"
        openfile.write(row)
        clean_and_crawl(url)
    return


# This function calls the recursive DFS function
def dfs_crawl(seed_pack):
   # start = time.clock()
    global depth

    # Main function that gets url in DFS order
    dfs(seed_pack)

    # write the max depth to the file
    openfile.write("Max Depth: " + str(depth))

    # close the file
    openfile.close()
    # print time.clock() - start

# This is the main function used for executing the code.
def main():
    seed1 = "https://en.wikipedia.org/wiki/Solar_eclipse"
    # frontier.append([seed, 1])
    dfs_crawl([seed1, 1])


main()


