import random
from bs4 import BeautifulSoup 
import requests

#url_series = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
url_movies = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
#url_recipes = 'https://www.tasteofhome.com/collection/our-100-highest-rated-recipes-ever/'

def main():
    request = requests.get(url_movies)
    html = request.text

    soup = BeautifulSoup(html, 'html.parser')
    #print(soup)
    characteristics = soup.select('td.titleColumn')
    print(characteristics)

main()