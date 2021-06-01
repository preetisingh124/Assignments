import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Lists_of_hospitals_in_Europe"
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')

anchors = soup.find_all('a')
all_links = set()
for link in anchors:  # how to scrap all links ?
    if (link.get('href')):
        linkText = link.get('href')
        all_links.add(linkText)
print(all_links)
lst = ["https://en.wikipedia.org"+ link for link in all_links] #
print(lst)


exit()
def linkmaker(url,all_links):
    lst = ["https://en.wikipedia.org" + link for link in all_links]
    return lst
