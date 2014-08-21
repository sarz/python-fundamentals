__author__ = 'Sarah Ismail'

# Following hitch hiker's guide instructions to scrape: http://docs.python-guide.org/en/latest/scenarios/scrape/

#4 things you can do with a document:
# from requests import get, put, post, delete
#Another way to do it
#from requests import get
#r = get('http://www.reddit.com/r/python')

#****r = requests.get('http://statsforchange.org')
#****print 'status:', r.status_code
#****print 'initial text:', r.text[:40]
#****tree = html.fromstring(r.text)

#stripped_url = 'http://statsforchange.org/partners'.split('//')[1]
#print stripped_url
#replaced_url = stripped_url.replace('/', '_')
#print replaced_url

import io

#test_urls = ['http://statsforchange.org', 'http://sfbay.craigslist.org/mca/']



#import csv
#with open('/home/oski/Desktop/Shared/sf_Programming_Dlab/python websites.csv', 'rb') as f:
#    reader = csv.reader(f)
#    for row in reader:
#        print row


from lib_scrape_our_interests import save_web_to_file

#Chaining (parsimony of functions):
with io.open('/home/oski/Desktop/python-fundamentals/Scraping/urls', 'r', encoding='utf8') as url_list:
    test_urls = url_list.readlines()
for curr_url in test_urls:
    curr_url.strip()
    curr_url = curr_url.strip()
    # save_web_to_file(curr_url)
    #Dav# r = requests.get

##########urls = io.open('').readlines()

#***print tree.body.text_content()








