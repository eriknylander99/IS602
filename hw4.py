__author__ = 'Erik Nylander'

# Import the necessary modules.
try:
    import bs4
except ImportError:
    print 'Beautiful Soup is not installed.'
import urllib2
from alchemyapi import AlchemyAPI

def remove_attrs(soup):
    for tag in soup.findAll(True):
        tag.attrs = {}
    return soup


def html_clean(soup):
    for script in soup(['script', 'style', '[document]', 'head', 'title', 'ul']):
        script.decompose()
    return soup


def read_universe(url):
    try:
        page = urllib2.urlopen(url)
    except ValueError:
        print '%s is not a valid website.' % url
    soup = bs4.BeautifulSoup(page.read())
    soup = html_clean(soup)
    text = soup.get_text()
    # Rewrite as for loops or try to understand. Possible break at Tagged as?
    lines = (line.strip() for line in text.splitlines())
    blocks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(block for block in blocks if block)
    print text


if __name__ == '__main__':
    url = 'http://www.universetoday.com/114304/meet-laniakea-our-home-supercluster/'
    read_universe(url)

