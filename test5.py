import requests
from bs4 import BeautifulSoup

def crawling_sites(url):
    response = requests.request('GET', url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    titles = soup.select('div.row div.col-sm-8')
    places_title = []
    
    for one in titles:
       places_title.append(one.get_text().strip())
       
    return places_title


url = 'http://www.koreatriptips.com/tourist-attractions.html'
print(crawling_sites(url))