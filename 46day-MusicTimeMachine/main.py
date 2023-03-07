from scrap import Scrap
from spotify import Spotify
from date import DateValidator

URL_BILLBOARD = "https://www.billboard.com/charts/hot-100/"

date_input = input("Which year do you want to travel to?\nType the date in the format YYYY-MM-DD: ")

# TODO: Move the date validation to be called into init function.


print("Validating if the date is correct")
try:
    date_validator = DateValidator(date_input)
except:
    raise Exception("Failed to validate the date")
else:
    print("Date validated sucessfully, getting the top 100 from Bilboard website...")
    scrap = Scrap()
    scrap.get_top100(url=f"{URL_BILLBOARD}{date_input}")
    print("Songs from Bilboard scraps sucessfully, connecting to Spotify to create your playlist...")
    spotify = Spotify()
    spotify.create_playlist_top100(date=date_validator.date_input, songs=scrap.song_list, artists=scrap.artist_list)
    print("...Playlist on sportify created sucessfullly, enjoy your songs !!")