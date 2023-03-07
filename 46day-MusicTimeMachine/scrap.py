from bs4 import BeautifulSoup
from conn import Conn

class Scrap:
    
    def __init__(self) -> None:
        self.conn = Conn()
    
    def _get_website(self):
        website = self.conn.get_request(self.url)
        self.soup = BeautifulSoup(website, "html.parser")
        return self.soup
    
    def _get_songs(self):
        all_songs = self.soup.select(".c-title.a-no-trucate.a-font-primary-bold-s.u-letter-spacing-0021")
        self.song_list = [s.getText().strip() for s in all_songs]
        return True
    
    def _get_artist(self):
        all_artists = self.soup.select(".c-label.a-no-trucate.a-font-primary-s")
        self.artist_list = [s.getText().strip() for s in all_artists]
        return True
    
    def get_top100(self, url: str):
        self.url = url
        self._get_website()
        self._get_artist()
        self._get_songs()