from collections import defaultdict
import numpy as np

inLinks = defaultdict(list)
Q = []
I = {}  # Vector to hold the current page Rank estimat  e
R = {}  # The resulting better page rank estimate
RI = {}  # Holds the difference R - I vector
d = 0.15  # Damping factor
# d = 0.25  # Damping factor

# d = 0.35  # Damping factor
# d = 0.5  # Damping factor
x = 0  # Value of I - R Square for calculating
incoming_links = []
outlinks = {}
itercounter = 0
min_itercounter = 4

# Performing 5 iterations
# This functions read the graph and builds a set of
# inputFile = ("G1.txt", 'r')

incomoing_Links = {}


inputFile = open("G2.txt", 'r')
for line in inputFile:
    docs = line.rstrip('\n').split(' ')
    doc = docs[0]
    inComingLinks = docs[1:]  # Q in the pseudo code
    incomoing_Links[doc] = len(inComingLinks)
    for inLink in inComingLinks:
        inLinks[doc].append(inLink)

# P = outlinks.keys()
# print(P)

for key, value in inLinks.items():
    key = outlinks.setdefault(key, [])

for key, value in inLinks.items():
    for link in value:
        if (str(link)) in inLinks:
            outlinks[link].append(key)
# print(outlinks)

P = outlinks.keys()
# Test for reference
# print(inLinks.get('Space_exploration'))
N = len(P)
# print(inComingLinks)
for eachPage in P:
    # I <-- 1 / N
    I[eachPage] = (1 / N)


# End of line 8 in the program
# print(I.get("Space_exploration"))
# Check for convergence using the norm two vector
def is_converged(l2_norm):
    if l2_norm < 0.0005:
        return True
    return False


l2norm = 1
initL2Norm = 0

# Each page has d / N chance of random selection
for eachPage in P:
    R[eachPage] = d / N

while True:
    sum_of_diffIR = 0
    if not is_converged(l2norm) and itercounter < 4:
        # Compute the number of outgoing links for each page P
        # Initial l2 norm
        for page, rank in I.items():
            sum_of_diffIR = sum_of_diffIR + (float(R[page]) - float(I[page])) ** 2
        initL2Norm = sum_of_diffIR ** 0.5
        # print(initL2Norm)

        for eachPage in P:
            # temp holds the Ip / |Q| for each page in P
            temp = 0
            IL = inLinks.get(eachPage)
            for each_outgoing_page in IL:
                # Ignoring Dangling links
                if each_outgoing_page not in P:
                    continue
                Q = outlinks.get(each_outgoing_page)
                temp = temp + (I[str(each_outgoing_page).rstrip()]) / len(Q)
            R[str(eachPage).rstrip()] = ((1 - d) * temp)

            # else:
            #     for each_outgoing_page in P:
            #         temp = temp + (I[str(eachPage).rstrip()]) / len(Q)
            #     R[str(each_outgoing_page).rstrip()] += ((1 - d) * temp)

        # print(R)
        # At this point we are in line 22 of the implementation
        # Calclulate the L2 norm
        # I_vector = list(I.values())
        # R_vector = list(R.values())
        # print(np.asarray(I_vector) - np.asarray(R_vector))
        # l2norm = np.linalg.norm(np.asarray(R_vector) - np.asarray(I_vector) ,2)
        # for page, rank in I.items():
        #     RI[page] = R[page] - I[page]
        #
        # for page, rank in RI.items():
        #     x += float(RI[page]) ** 2
        #
        # l2norm = x ** 0.5

        for key, value in I.items():
            sum_of_diffIR = sum_of_diffIR + (float(I[key]) - float(R[key])) ** 2
        l2norm = sum_of_diffIR ** 0.5

        fo = open("L2NormForG2.txt", "a")
        #fo = open("L2NormForG2.txt", "a")
        fo.write("SUM OF PAGE RANK " + str(sum(R.values())) +"   L2NORM :  " + str(l2norm) + "\n")
        print(l2norm)
        # print(I)
        # Assign new page rank to old one
        I = R.copy()
        # print(l2norm)
        itercounter += 1
    else:
        break
i = 0
file = open("PageRankResultsForG2.txt", "w")
#file = open("PageRankResultsForG2.txt", "w")  Uncomment this for getting report FOr Grapgh G2
# Sort into decending order of values
for page, rank in sorted(I.items(), key=lambda x: -x[1]):
    if i > 50 :
        break
    file.write("https://en.wikipedia.org/wiki/" + page + " ||   Page Rank ||  : " + str(rank) + "\n")
    i += 1

file.close()

fo = open("Top25BasedOnIncomingLinks.txt" , "w")
counter = 0
for page, links in sorted(incomoing_Links.items(), key=lambda x: -x[1]):
    if counter > 25:
        break
    fo.write("https://en.wikipedia.org/wiki/" + page + " ||  Number of incoming links ||  : " + str(links) + "\n")
    counter += 1


# Implementation of Page Rank Algorithm
