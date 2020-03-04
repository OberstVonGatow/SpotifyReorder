# SpotifyReorder
Reorder Spotify Playlists

With this script i reorder my playlists - latest added track on top.

I run this script from a raspberry pi every hour.

You could use every device with Python and a Browser installed (you need the Browser only once for login).



How To:

install Python

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



Notes:
I run the Script with cron every 10 Minutes. (https://www.stetic.com/developer/cronjob-linux-tutorial-und-crontab-syntax/)

Constin-Nox (https://github.com/Costin-Nox) mentioned, that if you run the script with different user you have to take care of the cached token. If you run the Script it will store a .cache-username in the folder you run the script in.
You could modify the Script and add a different cache path like this:

token = util.prompt_for_user_token(username,scope,client_id = client_id,client_secret = client_secret,redirect_uri='http://localhost/', cache_path='/your/file/path/.cache-username')  

docs:
https://github.com/plamere/spotipy/blob/master/spotipy/util.py


