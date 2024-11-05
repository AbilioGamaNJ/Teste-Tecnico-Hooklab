import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.reddit.com/r/programming/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')

reddit_content = soup.find_all('shreddit-post')

posts = []
for i in range(3):
  reddit_title = reddit_content[i].get('post-title')
  reddit_up_votes = reddit_content[i].get('score')
  reddit_link_posts = reddit_content[i].get('content-href')
  posts.append([reddit_title, reddit_up_votes , reddit_link_posts])

df = pd.DataFrame(posts, columns=['Título', 'Votos', 'Link' ])
df.to_csv('Reddit_posts.csv')



