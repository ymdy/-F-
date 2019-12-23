# -*- coding: utf-8 -*-
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import pprint

client_id = '1c460d05ecb4fffaecb72a83d15d38a'
client_secret = '75316ecb7a59478ca33ca197ef73637d'
artist_id = '36QJpDe2go2KgaRleHCDTp'

client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = spotify.artist_albums(artist_id, album_type='single', country='JP', limit=20)

artist_songs = []
for song in results['items'][:len(results)]:
   data = [
       '曲名：'+ song['name'],
       '発売日：'+ song['release_date'],
       'id：'+ song['id']]
   artist_songs.append(data)
pprint.pprint(artist_songs)

