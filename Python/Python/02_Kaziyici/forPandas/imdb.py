from requests import get
from bs4 import  BeautifulSoup
from time import time, sleep
from os import system
from random import randint
from warnings import warn

# Redeclaring the lists to store data in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

# Preparing the monitoring of the loop
start_time = time()
requests = 0

pages = [str(i) for i in range(1,5)]
years_url = [str(i) for i in range(2015,2021)]

# For every year in the interval 2015-2020
for year_url in years_url:
    # For every page in the interval 1-4
    for page in pages:
        headers = {"Accept-Language": "en-US, en;q=0.5"}
        # Make a get request
        response = get('http://www.imdb.com/search/title?release_date=' + year_url +
        '&sort=num_votes,desc&page=' + page, headers = headers)

        # Pause the loop
        sleep(randint(1,2))

        # Monitor the requests
        requests += 1
        elapsed_time = time() - start_time
        system('clear')
        print(f'Request:{requests}; Frequency: {requests/elapsed_time} requests/s')

        # Throw a warning for non-200 status codes
        if response.status_code != 200:
            warn(f'Request: {requests}; Status code: {response.status_code}')

        # Break the loop if the number of requests is greater than expected
        if requests > 15:
            warn('Number of requests was greater than expected.')
            break

        # Parse the content of the request with BeautifulSoup
        page_html = BeautifulSoup(response.text, 'html.parser')

        # Select all the 50 movie containers from a single page
        mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

        # For every movie of these 50
        for container in mv_containers:
            # If the movie has a Metascore, then:
            if container.find('div', class_ = 'ratings-metascore') is not None:

                # Scrape the name
                name = container.h3.a.text
                names.append(name)

                # Scrape the year
                year = container.h3.find('span', class_ = 'lister-item-year').text
                years.append(year)

                # Scrape the IMDB rating
                imdb = float(container.strong.text)
                imdb_ratings.append(imdb)

                # Scrape the Metascore
                m_score = container.find('span', class_ = 'metascore').text
                metascores.append(int(m_score))

                # Scrape the number of votes
                vote = container.find('span', attrs = {'name':'nv'})['data-value']
                votes.append(int(vote))

import pandas as pd

movie_ratings = pd.DataFrame({
    'movie': names,
    'year': years,
    'imdb': imdb_ratings,
    'metascore': metascores,
    'votes': votes
})

print(movie_ratings)


print(movie_ratings.describe().loc[['min', 'max'], ['imdb', 'metascore']])
movie_ratings['n_imdb'] = movie_ratings['imdb'] * 10
movie_ratings.head(3)


import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (16,4))
ax1, ax2, ax3 = fig.axes
ax1.hist(movie_ratings['imdb'], bins = 10, range = (0,10)) # bin range = 1
ax1.set_title('IMDB rating')
ax2.hist(movie_ratings['metascore'], bins = 10, range = (0,100)) # bin range = 10
ax2.set_title('Metascore')
ax3.hist(movie_ratings['n_imdb'], bins = 10, range = (0,100), histtype = 'step')
ax3.hist(movie_ratings['metascore'], bins = 10, range = (0,100), histtype = 'step')
ax3.legend(loc = 'upper left')
ax3.set_title('The Two Normalized Distributions')
for ax in fig.axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
plt.show()