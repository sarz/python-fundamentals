__author__ = 'Sarah Ismail'

# Following hitch hiker's guide instructions to scrape: http://docs.python-guide.org/en/latest/scenarios/scrape/

from lxml import html
import requests
import io


def save_web_to_file(url, ):
    '''Use requests to fetch url, then save to a file'''
    r = requests.get(url)
    #need to pull a file to save to
    #Might be a problem if URL doesn't start with http://
    stripped_url = url.split('//')[1]
    filename = stripped_url.replace('/', '_')
    #Context manager, opening file, and closing it again
    with io.open(filename, 'w', encoding='utf8') as outfile:
        outfile.write(r.text)

    print "I successfully downloaded", url


