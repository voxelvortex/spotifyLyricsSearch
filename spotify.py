import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def test(CID, CSEC):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=CID, client_secret=CSEC))
    plist = spotify.playlist("7LMG1XkTVmupLNxnrlfx6J")
    print(1)
    print(plist["tracks"]["items"][0])
