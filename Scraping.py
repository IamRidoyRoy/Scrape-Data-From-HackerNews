# Here i will scraping data from hacker News
import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.find(id="score_33788208"))
# print(soup.select('.score'))
# print(soup.select('#score_33788208'))
link = soup.select('.titleline')[0]
vote = soup.select('.score')[0]
print(link, vote)
# print(link)
