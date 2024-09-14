import requests
from bs4  import  BeautifulSoup
import pandas as pd
import os.path
import shutil
from datetime import datetime


profiles_fqe=[93058,109637,35820,109989,108578]
profiles_cfc=[184209]

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
# CFC rating
# https://www.chess.ca/en/ratings/p/?id=184209
print("canada: Classement CFC:")
print("======================================================================")
def extract_one_cfc(profile):
    lien="https://www.chess.ca/en/ratings/p/?id="+str(profile)
    ##  le problene c est qye ka page ne contient que du js
    print(lien)
    resp=requests.get(lien)
    print("resp",resp.content)
    parser=BeautifulSoup(resp.content, "html.parser")
    parsernom=parser.find_all('td')
    for job_element in parsernom:
        print(job_element, end="\n" * 2)
    nom="toto"
    classement = "23"
    print(parsernom)
    return nom,classement
for id in  profiles_cfc:
    nom,classement=extract_one_cfc(id)
    print (nom,": ",classement)