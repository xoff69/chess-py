import requests
from datetime import datetime

fname="C:\\Users/xoffp/Downloads/xoff-qc21_lichess"+datetime.now().strftime("%Y_%m_%d")+".pgn"
url="https://lichess.org/api/games/user/xoff_qc21?tags=true&clocks=false&evals=false&opening=true&perfType=ultraBullet%2Cbullet%2Cblitz%2Crapid%2Cclassical%2Ccorrespondence%2Cstandard"
print(fname)

r = requests.get(url)
with open(fname,'wb') as f:
  f.write(r.content)

print("fini")