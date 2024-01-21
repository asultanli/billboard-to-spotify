from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_id = os.getenv("USER_ID")

sp_oauth = SpotifyOAuth(client_id=client_id,
                        client_secret=client_secret,
                        redirect_uri="http://example.com",
                        scope="playlist-modify-private")

# Get the authorization URL
auth_url = sp_oauth.get_authorize_url()

# Print the authorization URL and ask the user to open it in their browser
print(f"Please visit this URL to authorize your Spotify app: {auth_url}")

# Get the authorization code from the user after they have authorized the app
auth_code = input("Enter the authorization code from the URL: ")

# Exchange the authorization code for access and refresh tokens
token_info = sp_oauth.get_cached_token()

# Use the access token to set up the Spotipy library
sp = spotipy.Spotify(auth=token_info['access_token'])

# Get the user id of the authenticated user
user_info = sp.current_user()
user_id = user_info['id']

# Print the user id
#print(f"Authenticated user's Spotify username (user id): {user_id}")


chosen_time = input("Please enter the date you want to travel to. format: YYYY-MM-DD: ")
URL = "https://www.billboard.com/charts/hot-100/" + chosen_time

response = requests.get(URL)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

songs = soup.select("li ul li h3")
songs_titles = [song.getText().strip() for song in songs]

# Search for each song on Spotify and get the URI
spotify_uris = []
for song in songs_titles:
    try:
        result = sp.search(q=f"track:{song}", type="track", limit=1)
        track_uri = result['tracks']['items'][0]['uri']
        spotify_uris.append(track_uri)
    except IndexError:
        print(f"Song not found on Spotify: {song}")



playlist_name = f"{chosen_time} Billboard 100"
playlist_description = "Billboard Hot 100 Playlist"

# Create a new private playlist
playlist = sp.user_playlist_create(user_id, name=playlist_name, public=False, description=playlist_description)
playlist_id = playlist['id']

# Add each song to the new playlist
sp.playlist_add_items(playlist_id, spotify_uris)

# Print the playlist id
print(f"Playlist created successfully! Playlist ID: {playlist_id}")