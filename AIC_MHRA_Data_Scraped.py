from Scraping_basics_functions import data_parser,fetch_table_by_class, save_data_frame,find_links_of_all_pages,Scraped_all_pages

parsed_data = data_parser("https://aic.mhra.gov.uk/era/pdr.nsf/name?openpage&start=1&count=200")
all_pages_link = find_links_of_all_pages(parsed_data, 'textbox')
head, all_pages= Scraped_all_pages(all_pages_link)
save_data_frame(all_pages,head,'all_pages_mhrd2.tsv')
