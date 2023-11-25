import requests
from bs4  import  BeautifulSoup
import pandas as pd
import os.path
import shutil
from datetime import datetime


profiles_fqe=[93058,109637,35820,109989,108578]


print("quebec: Classement FQE:")
print("======================================================================")
def extract_one_fqe(profile):
    lien="https://www.fqechecs.qc.ca/membres/index.php?Id="+str(profile)
    resp=requests.get(lien)
    parser=BeautifulSoup(resp.content, "html.parser")
    parsernom=parser.find_all(class_="text-left text-dark pb-4")
    nom = parsernom[0].get_text()
    parserClassement=parser.find_all('td',class_="text-center")
    classement = parserClassement[0].get_text()

    return nom,classement
for id in  profiles_fqe:
    nom,classement=extract_one_fqe(id)
    print (nom,": ",classement)