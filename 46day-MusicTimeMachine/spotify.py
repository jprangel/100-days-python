import os
import spotipy
import spotipy.util as util

class Spotify:
    
    def __init__(self) -> None:
        self.playlist_name = "- Billboard top 100"
        self.playlist_desc = "Playlist created with top 100 billboard songs"
        spotify_scope = "playlist-modify-public"
        spotify_uri = "http://127.0.0.1/callback"
        try:
            spot_client_id = os.environ['SPOTIFY_CLIENTID']
        except:
            raise Exception("Environment variable SPOTIFY_CLIENTID not found")
        try:
            spot_secret_id = os.environ['SPOTIFY_SECRETID']
        except:
            raise Exception("Environment variable SPOTIFY_SECRETID not found")
        try:
            spotify_username = os.environ['SPOTIFY_USERNAME']
        except:
            raise Exception("Environment variable SPOTIFY_USERNAME not found")
        try:
            token = util.prompt_for_user_token(username=spotify_username, 
                                               scope=spotify_scope, 
                                               client_id=spot_client_id,
                                               client_secret=spot_secret_id,
                                               redirect_uri=spotify_uri)
        except:
            os.remove(f".cache-{spotify_username}")
        else:
            self.sp_auth = spotipy.Spotify(auth=token)

    def _get_user_id(self):
        """ Get the spotify userID"""
        print("Gettting Spotify user ID...")
        self.user_id = self.sp_auth.current_user()["id"]
        return True
        
    def _get_tracks_id(self):
        """ Fetch the tracks from Spotify"""
        i = 0
        self.track_id_list = []
        print("Fetching tracks from Spotify...")
        for s in self.song_list:
            a = self.artist_list[i]
            query = f"artist: {a} track: {s} year: {self.year}"
            results = self.sp_auth.search(q=query, type='track', limit=1)
            id = results['tracks']['items'][0]['uri']
            self.track_id_list.append(id)
            print(f"Track number {i+1} fetched...")
            i += 1
        print("...Tracks sucessfully parsed")
        
    def _create_playlist(self):
        """ Create a playlist on Spotify"""
        print("Creating Playlist...")
        playlist_name = f"{self.date} {self.playlist_name}"
        try:
            self._get_user_id()
        except:
            raise Exception("Failed to get the user id, unable to proceed")
        else:
            self.playlist_id = self.sp_auth.user_playlist_create(user=self.user_id, 
                                                                name=playlist_name,
                                                                description=self.playlist_desc,
                                                                public=True)['id']
            print(f"...Playlist created sucessfully {self.playlist_id}")
            return True

    def _add_track_to_playlist(self):
        """ Add the tracks to a playlist on Spotify"""
        print("Adding songs into playlist on Spotify...")
        self.sp_auth.user_playlist_add_tracks(user=self.user_id, playlist_id=self.playlist_id, tracks=self.track_id_list)
        print("Songs added successfully into playlist...")
        return True
    
    def create_playlist_top100(self, artists, songs, date):
        """ Control the creation of the playlist, fetching and adding tracks"""
        self.artist_list = artists
        self.song_list = songs
        self.year = date.split("-")[0]
        self.date = date
        try:
            self._get_tracks_id()
        except:
            raise Exception("Unable to get Spotify tracks")
        try:
            pass
            self._create_playlist()
        except:
            raise Exception("Unable to create the playlist on Spotify")
        try:
            pass
            self._add_track_to_playlist()
        except:
            raise Exception("Unable to add songs into playlist on Spotify")