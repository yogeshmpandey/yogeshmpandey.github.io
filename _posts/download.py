"""
A script to download all images from a web page
"""
import string
import requests
from bs4 import BeautifulSoup
i=4547
r = requests.get('http://boards.4chan.org/gif/thread/6927605/asian-oillotion')
soup =BeautifulSoup(r.content)

for link in soup.find_all("a", class_="fileThumb"):
    i=i+1
    print link
    p = link.get('href')
    print p
    p=string.replace(p,"//", "http://");
    print p
    data=requests.get(p).content
    
    filename=str(i)+"image.webm"
    
    with open(filename, 'wb') as f:
            f.write(data)

