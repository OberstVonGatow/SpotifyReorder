# SpotifyReorder
Reorder Spotify Playlists

With this script i reorder my playlists - latest added track on top.
I run this script from a raspberry pi every hour.
You could use every device with Python and a Browser installed (you need the Browser only once for login).

How To:

install Spotipy https://github.com/plamere/spotipy

Create an Account at https://developer.spotify.com/dashboard/

Create a Client ID
  Application name: ReSort
  Application description: ReSort Playlists
  Redirect URIs: http://localhost/
  
In Dashboard click "SHOW CLIENT SECRET".


Copy Client ID and Client Secret in the Python File ReSort.py.

Rename Playlistname and Username in File ReSort.py

run Pyton Script in CMD Window

Browser should open where you can login

-> you should get redirected to http://localhost/.......

Copy the whole URL and Paste in CMD Windows
