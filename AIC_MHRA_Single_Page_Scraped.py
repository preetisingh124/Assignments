from Scraping_functions  import Extractor, Pages, Scraper
s = Scraper()
p = s.get_parsed_data("https://aic.mhra.gov.uk/era/pdr.nsf/name?openpage&start=1&count=200")
h,r = Extractor.table_extractor(p)
s.make_dataframe(header = h, extracted_rows=r)
s.save('aic_MHRA.tsv')
