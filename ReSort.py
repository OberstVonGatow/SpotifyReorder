# coding=utf-8
import sys
import spotipy
import spotipy.util as util
from time import sleep


def check_tracks(sp, results, first_date, counter):
    for i, item in enumerate(results['items']):
        temp_date = item['added_at']
        if temp_date > first_date:
            track = item['track']
            print(counter, track['artists'][0]['name'], track['name'])
            sp.user_playlist_reorder_tracks(
                username, playlist['id'], counter, 0, 1)
            sleep(0.5)
            first_date = temp_date
        counter += 1
    return counter


if __name__ == '__main__':

    scope = 'playlist-modify-private playlist-read-collaborative playlist-modify-public playlist-read-private playlist-modify-private'

##########################################
#   EDIT HERE
    username = 'XXXXXXXX'
    playlistarray = [
        'PLAYLISTNAME1'.decode('utf-8'),
        'PLAYLISTNAME2'.decode('utf-8'),
        'PLAYLISTNAME99'.decode('utf-8'),
    ]
    client_id = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
    client_secret = 'XXXXXXXXXXXXXXXXXXXXXXXX'
##########################################

    token = util.prompt_for_user_token(
        username, scope, client_id=client_id, client_secret=client_secret, redirect_uri='http://localhost/')
    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.current_user_playlists(limit=50, offset=0)
        while playlists:
            for i, playlist in enumerate(playlists['items']):
                if playlist['owner']['id'] == username and playlist['name'] in playlistarray:
                    
                    results = sp.user_playlist_tracks(username, playlist['id'], limit=100)
                    first_date = results['items'][0]['added_at']
                    tracks = results
                    counter = 0
                    counter = check_tracks(sp, tracks, first_date, counter)
                    while tracks['next']:
                        tracks = sp.next(tracks)
                        counter = check_tracks(sp, tracks, first_date, counter)

            if playlists['next']:
                playlists = sp.next(playlists)
            else:
                playlists = None
    else:
        print("Can't get token for", username)
