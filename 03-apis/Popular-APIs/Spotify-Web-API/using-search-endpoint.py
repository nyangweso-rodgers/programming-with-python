import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials 
cid ="xx" 
secret = "xx" 
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)