import requests
import os

token = os.getenv("SPOTIFY_TOKEN")
api_url = os.getenv("SPOTIFY_URL")


def get_playlists(token, api_url):

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token,
    }

    response = requests.get(api_url + 'users/11143403508/playlists', headers=headers)
    print("playlists :{}\n".format(response.text))

def get_tracks(token, api_url):

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token,
    }

    response = requests.get(api_url + 'artists/11143403508/tracks', headers=headers)
    print("tracks: {}".format(response.text))

get_playlists(token, api_url)
get_tracks(token, api_url)