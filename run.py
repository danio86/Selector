import random
""" from bs4 import BeautifulSoup 
import requests """
import csv

#url_series = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
#url_movies = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
#url_recipes = 'https://www.tasteofhome.com/collection/our-100-highest-rated-recipes-ever/'

def main():
    """ request = requests.get(url_movies)
    html = request.text """

    """ soup = BeautifulSoup(html, 'html.parser')
    characteristics = soup.select('td.titleColumn')
    print(characteristics[0])
    print(type(characteristics))
    movie_data = characteristics[0].text.split()
    print(movie_data)
    print(len(characteristics)) """

    file = open('test_film.csv')
    rows = csv.reader(file, delimiter=',')
    watch = []

    for row in rows:
        watch.append(row)
     
    keys = watch[0]
    values = watch[1:]
    print(values, 'test')
    
    for item in values[0]:
        val = item.split(',')
        print(val, len(val), 'why?')

    for xy in values:
        print(xy.split(','), len(xy), 'now?')
    
  
    
    
    
main()
