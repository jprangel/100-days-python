from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
movie_title = [m.getText() for m in all_movies]
movies = movie_title[::-1]

with open("movies.txt", mode="w") as file:
    for m in movies:
        file.write(f"{m}\n")
