#!/usr/bin/python
from bs4 import BeautifulSoup
from urllib.request import urlopen
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import operator
url=urlopen("https://en.wikipedia.org/wiki/Machine_learning")
s=BeautifulSoup(url)
data=s.body.get_text()
l=data.split()
print(len(l))
c=Counter(l).most_common(20)
two_d_array=np.array(c)
plt.title("top 20 elements")
plt.pie(two_d_array[:,1],labels=two_d_array[:,0],autopct="%1.1f%%")
plt.show()
more_than_3=Counter(l)
dictt={}
for i,j in dict(more_than_3).items():  #key and the count no.
    if j>3:
        dictt[i]=j
sorted_d=sorted(dictt.items(),key=operator.itemgetter(1))
plt.xlabel("words")
plt.ylabel("repeatation")
arr=np.array(sorted_d)
plt.scatter(arr[:,0],arr[:,1])
plt.show()
links=[]
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    links.append(link.get('href'))
l1=np.array(links)
print(l1)
