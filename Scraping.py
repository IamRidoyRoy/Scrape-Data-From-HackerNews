# Here i will scraping data from hacker News
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.find(id="score_33788208"))
# print(soup.select('.score'))
# print(soup.select('#score_33788208'))


links = soup.select('a')
subline = soup.select('.subtext')
# print(links, votes)


# crtete a sort function to sort the list  
def sort_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def createCustomNews(links, subline):
    h_news = []

    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        # points = votes[idx].getText()

        vote =subline[idx].select('.score')
        
        if len(vote): 
            # to replace points to empty 
            points = int(vote[0].getText().replace(' points', '')) 
            if points > 99: 
                print(points)

            #create here a dictionary to create a tile and link list 
            h_news.append({'title': title, 'links': href })
    
    return sort_by_votes(h_news)

obj = createCustomNews(links, subline)
pprint.pprint(obj)

