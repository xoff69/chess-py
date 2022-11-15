import requests
from bs4  import  BeautifulSoup
import pandas as pd
import os.path
import shutil
from datetime import datetime



def filesvgname(suffixe):

    now = datetime.now() # current date and time
    time = now.strftime("%Y%m%d-%H%M%S")
    return time+'-'+suffixe


file_name= 'fide.csv'
#sauvegarde du fichier
source=file_name
destination=filesvgname(file_name)
shutil.copyfile(source, destination)

if os.path.isfile(file_name):

    df_reference = pd.read_csv (file_name)
else:
    print("Le fichier reference  n existe pas")
    df_reference = pd.DataFrame(columns=['profileId', 'Nom', 'Standard', 'Rapide', 'Blitz'])

profiles=[45110565,659487,656410,26016460,434523,605506,608742]



def extract_classement(couleur,parser):
    fu = parser.find_all(class_="profile-top-rating-data profile-top-rating-data_"+couleur)
    t = fu[0]
    classement="0"
    for res in t:
        classement=(res.text.strip())
    return classement

def extract_one(profile):
    lien="https://ratings.fide.com/profile/"+str(profile)
    resp=requests.get(lien)
    parser=BeautifulSoup(resp.content, "html.parser")
    fn=parser.find_all(class_="col-lg-8 profile-top-title")
    t=fn[0]
    nom=t.get_text()
    std=extract_classement("gray",parser)
    rapid=extract_classement("red",parser)
    blitz=extract_classement("blue",parser)
    return nom,std,rapid,blitz

def determine_evolution(ancien,nouveau):

    NR="Not rated"
    if str(ancien)==NR:
        ancien="-"
    if str(nouveau) == NR:
        nouveau = "-"

    if ancien==nouveau:
        classement = str(nouveau) + ' ('
        classement=classement+"="
    elif ancien<nouveau:
        classement = str(nouveau) + ' (' + str(ancien) + " "
        classement = classement + "+"
    else:
        classement = str(nouveau) + ' (' + str(ancien) + " "
        classement = classement + "-"
    classement=classement+")"
    return classement

df = pd.DataFrame(columns=['profileId','Nom', 'Standard', 'Rapide','Blitz'])


for id in  profiles:
    nom,std,rapid,blitz=extract_one(id)
    df.loc[len(df)] = [id, nom,std,rapid,blitz]
    a = df_reference.loc[df_reference['profileId']== id]

    if len(a)>0:
        s=(determine_evolution(str(a['Standard'].iloc[0]),std))
        r=(determine_evolution(str(a['Rapide'].iloc[0]),rapid))
        b=(determine_evolution(str(a['Blitz'].iloc[0]),blitz))
        print("      :", nom, " ", s, " ", r, " ", b)
    else:
        print("nouveau:" ,nom," ", std," ", rapid," ", blitz)

df.to_csv(file_name)
