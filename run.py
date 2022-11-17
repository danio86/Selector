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
        """ print(len(watch)) """
    print(watch[0], len(watch[0]))
    print(watch[2]) 
    print(len(watch[2]))   
    keys = watch[0]
    
    """ print(watch[0:2]) """
    for item in watch:
        """ print(item[0], 'test') """

    
   
    
    """ type(file)
    csvreader = csv.reader(file)
    print(csvreader)
 """
main()