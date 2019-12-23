import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

client_id = '1c460d05ecb4fffaecb72a83d15d38a'
client_secret = '75316ecb7a59478ca33ca197ef73637d'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()