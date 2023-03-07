import re
import pandas as pd
import os
import requests
import json
import urllib.request
from pathlib import Path

user="deriveepartielle"
PGNDirectory="./PGN"
## sourc https://gist.github.com/DataSherlock/58e6285dbd11cbba9d29b32c5480521d

def getPGN(user):
    """This function accesses the chess.com public API and downloads all the PGNs to a folder"""
    pgn_archive_links = requests.get("https://api.chess.com/pub/player/"+user+"/games/archives", verify=False)
    if not os.path.exists(PGNDirectory):
        os.makedirs(PGNDirectory)

    for url in json.loads(pgn_archive_links.content)["archives"]:
        print(url)
        filepath = PGNDirectory + "/"+ url.split("/")[7]+url.split("/")[8]+'.pgn'
        my_file = Path(filepath)
        if not my_file.is_file():
            urllib.request.urlretrieve(url+'/pgn',filepath)

getPGN(user)