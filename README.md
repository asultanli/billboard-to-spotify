# Spotify Billboard Playlist Creator

A Python script to create a Spotify playlist based on Billboard Hot 100 songs for a specific date.

## Overview

This script utilizes BeautifulSoup and Spotipy to scrape Billboard Hot 100 songs for a given date and create a Spotify playlist with those songs.

## Features

- Fetches Billboard Hot 100 songs for a specified date.
- Searches for each song on Spotify and retrieves its URI.
- Creates a private Spotify playlist with the fetched songs.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or later installed
- [Spotify Developer Account](https://developer.spotify.com/dashboard/) with a registered application
- Billboard website access

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/asultanli/spotify-billboard-playlist.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Spotify application credentials:

   ```env
   CLIENT_ID=your_client_id
   CLIENT_SECRET=your_client_secret
   USER_ID=your_spotify_username
   ```

4. Run the script:

   ```bash
   python main.py
   ```

## Usage

1. Run the script and follow the prompts.
2. Visit the provided authorization URL in your browser and authorize the app.
3. Enter the authorization code back in the terminal.
4. Input the date for the Billboard Hot 100 songs.
5. The script will create a private Spotify playlist with the fetched songs.

## Author

- Sultanli Aykhan

