import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def data_parser(url):
    r = requests.get(url, verify=False)
    htmlContent = r.content
    soup = bs(htmlContent, 'html.parser')
    return soup



def fetch_table_by_class(soup, class_name):
    s = soup.find(class_=class_name) # find from class
    headers = s.find_all('th') # all headers i,e  fetch all columns name
    column_name = [] # create empty list to store columns name
    #print(headers)
    for header in headers:
        column_name.append(header.text)

    #print(column_name)      # we get lsit of column name
    rows = []
    table_rows = s.find_all('tr') #find all rows
    for row in table_rows:
        data = row.find_all('td')
        collect_table_data = []
        for i in data:
            collect_table_data.append(i.text)
        rows.append(collect_table_data)   # it will append to the rows of the all pages

    del rows[0]  # for creating dataframe rows and columns should be  same
    return column_name,rows


def save_data_frame(rows,column_name, file_name):
    df = pd.DataFrame(rows, columns=column_name)
    df.to_csv(file_name, sep='\t')
    #print(df.head)

def find_links_of_all_pages(soup, class_name ):
    anchors = soup.find(class_=class_name).find_all('a')
    all_links = set()
    for link in anchors:  # how to scrap all links ?
        if (link.get('href')):
            linkText = link.get('href')
            all_links.add(linkText)
    lst = ["https://aic.mhra.gov.uk/era/pdr.nsf/" + link for link in all_links]  # 
    #print(lst)
    return (lst)




def Scraped_all_pages(all_pages_link):
    # print((all_pages_link))
    all_pages = []
    counter = 0
    for link in all_pages_link:
        counter += 1
        print(counter, link)
        parsed_data = data_parser(link)

        head, row = fetch_table_by_class(parsed_data, 'workspace')

        # print(row)
        all_pages.extend(row)

    # print(all_pages)
    return head,all_pages













parsed_data = data_parser("https://aic.mhra.gov.uk/era/pdr.nsf/name?openpage&start=1&count=200")
all_pages_link = find_links_of_all_pages(parsed_data, 'textbox')
head, all_pages= Scraped_all_pages(all_pages_link)
save_data_frame(all_pages,head,'all_pages_mhrd2.tsv')