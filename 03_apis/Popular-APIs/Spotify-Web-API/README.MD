# Spotify Web API

## Table Of Contents
- [Further Reading]()
    - [Getting Started with the Web API](https://developer.spotify.com/documentation/web-api/quick-start/)
    
    - [Spotify Data Project Part 1 — from Data Retrieval to First Insights](https://towardsdatascience.com/spotify-data-project-part-1-from-data-retrieval-to-first-insights-f5f819f8e1c3)

[Spotify Web API](https://developer.spotify.com/documentation/web-api/)

# Data Retrieval
* Create account at [developer.spotify.com](https://developer.spotify.com/).

* Go to [Spotify Web API Console](https://developer.spotify.com/console/) and start exploring the different API endpoint

# Python Library for Data Retrieval
* [Spotify](https://spotipy.readthedocs.io/en/2.22.1/)
* Once you installed Spotipy, the below code is sufficient to get it up and running (use your own cid and secret from your Spotify developer account):

# API Endpint Reference
* Albums
* Artists
* Browse
* Follow
* Library
* Personalization
* Player
* Playlist
* Search
* Tracks
* User Profiles


# Using search Endpoint
* The search endpoint is fairly easy to use as there are only 2 required parameters: q and type. The first one can be any keyword such as ‘roadhouse blues’ or ‘2018’. The type can be album, artist, playlist or track.

* There are also a couple of limitations with this endpoint:
    - limit: a maximum of 50 results can be returned per query
    - offset: this is the index of the first result to return, so if you want to get the results with the index 50–100 you will need to set the offset to 50 etc.