import re
from celery import shared_task
from django.apps import apps
import json
from django.conf import settings
from bs4 import BeautifulSoup
import requests

import requests
from django.utils.timezone import now


def scrape_function():
    base_url = "https://www.imdb.com"

    headers = {
        "authority": "www.imdb.com",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "navigate",
        "sec-fetch-dest": "document",
        "accept-language": "en-US,en;q=0.9",
    }

    params = (("ref_", "nv_mv_250"),)
    response = requests.get(
        "https://www.imdb.com/chart/top", headers=headers, params=params
    )
    if response.status_code != 200:
        raise Exception("Couldn't fetch IMDB page")

    soup = BeautifulSoup(response.content, "lxml")
    all_movies_tag = soup.find("tbody", class_="lister-list")
    movies_tags = all_movies_tag.find_all("tr")
    Movie = apps.get_model("movies", "Movie")

    created_movies = 0
    updated_movies = 0
    for rank, movie_tag in enumerate(movies_tags):
        movie_image = (
            movie_tag.find("td", class_="posterColumn").find("img").attrs["src"]
        )
        movie_title_tag = movie_tag.find("td", class_="titleColumn").find("a")
        movie_title = movie_title_tag.get_text().strip()
        movie_link = f"{base_url}{movie_title_tag.attrs['href']}"
        movie_rating_text = (
            movie_tag.find("td", class_=re.compile("imdbRating"))
            .find("strong")
            .get_text()
            .strip()
        )
        movie_rating = float(movie_rating_text)
        movie_ranking = rank + 1

        movie, created = Movie.objects.update_or_create(
            title=movie_title,
            defaults={
                "title": movie_title,
                "link": movie_link,
                "rating": movie_rating,
                "rank": movie_ranking,
                "last_seen": now(),
            },
        )
        if created:
            created_movies += 1
        else:
            updated_movies += 1
    return [created_movies, updated_movies]


@shared_task
def scrape_imdb():
    created_movies, updated_movies = scrape_function()
    return f"Movie Scrape done. {created_movies} movies created, {updated_movies} movies updated."
