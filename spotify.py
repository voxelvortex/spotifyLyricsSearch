import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_data(CID, CSEC, playlist_uri):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=CID, client_secret=CSEC))
    data = spotify.playlist("7LMG1XkTVmupLNxnrlfx6J")
    return data


def get_name_and_artist(data):
    track = data["tracks"]["items"][0]
    return track["track"]["name"], track["track"]["artists"][0]["name"]
