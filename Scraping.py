# Here i will scraping data from hacker News
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.find(id="score_33788208"))
# print(soup.select('.score'))
# print(soup.select('#score_33788208'))


links = soup.select('a')
subline = soup.select('.subline')
# print(links, votes)


def createCustomNews(links, subline):
    h_news = []

    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        # points = votes[idx].getText()

        vote =subline[idx].select('.score')
        
        if len(vote): 
            # to replace points to empty 
            points = int(vote[0].getText().replace(' points', ''))   
            print(points)

        #create here a dictionary to create a tile and link list 
        h_news.append({'title': title, 'links': href})
    
    return h_news

createCustomNews(links, subline)
# print(obj)

