__author__ = 'Suman'

# Import required libraries
from bs4 import BeautifulSoup
from alchemyapi import AlchemyAPI
import urllib


def getcontent(url):
    """
    Get the required contents from the given URL
    """
    try:
        page = urllib.urlopen(url)
        soup = BeautifulSoup(page.read())
        soup = soup.find('div', {"class": "rightMainText"}).findAll('p')
        return soup
    except ValueError:
        print '%s is not a valid URL.' % url
    finally:
        page.close()


def analysecontent(content):
    """
    Process/Analyse the extracted contents with Alchemy API
    Assumption: api_key.txt with a valid key is available from where this program is getting executed.
    """
    print('Processing extracted text with AlchemyAPI...')
    alchemyapi = AlchemyAPI()
    response = alchemyapi.keywords('text', content, {'maxRetrieve': 10})
    if response['status'] == 'OK':
        print('---------------------------------')
        print('## Keywords      ## Relevance')
        for keyword in response['keywords']:
            print("{0}: {1}".format(keyword['text'].encode('utf-8'), keyword['relevance']))
        print('---------------------------------')
    else:
        print('Error in keyword extraction call: ', response['statusInfo'])

if __name__ == '__main__':
    url = "http://www.jbhunt.com/transportation_management/?src=subnav"
    analysecontent(getcontent(url))


#OUTPUT LOOKS LIKE BELOW:
#~~~~~~~~~~~~~~~~~~~~~~~~~
#Processing extracted text with AlchemyAPI...
#---------------------------------
## Keywords      ## Relevance
#exceptional customer: 0.921079
#shipment management: 0.865203
#powerful interface: 0.807243
#way: 0.519236
#experience: 0.499111
#simple: 0.497795
#---------------------------------


