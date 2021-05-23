import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Lists_of_hospitals_in_Europe'
response = requests.get(url)

tables = pd.read_html(response.text)

tables[0].to_csv("test1.csv")

