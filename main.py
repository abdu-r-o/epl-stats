import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_table(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_position(soup, club):
    tables = soup.find("pre")
    table = tables.string
    location = table.find(club)
    return(table[location-3])

def get_next(soup):
    tags = soup('a')
    link = tags[1].get('href',None)
    return ("http://www.rsssf.com/engpaul/FLA/"+link)

if __name__ == '__main__':
    starting_website = input("Starting website: ")
    club = input("What Club: ")
    count = input("How many years: ")
    count = int(count)
    soup = get_table(starting_website)
    print(starting_website[33:40], get_position(soup,club))
    url = get_next(soup)
    for i in range(count):
        if url == "http://www.rsssf.com/engpaul/FLA/league.html":
            print("2008 reached, no more data")
            break
        soup = get_table(url)
        print(url[33:40], get_position(soup, club))
        url = get_next(soup)
