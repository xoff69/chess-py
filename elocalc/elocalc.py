K=20
classement_depart=1431

def evalNewRating(cl_adv,resultat):
    expected = 1 / (1 + 10 ** ((cl_adv - classement_depart) / 400))
    return   classement_depart + K * (resultat - expected)


# tournoi elo opponent
elo_opp=[[1422,0],[1410,1],[1420,1],[1420,0],[1420,1]]

# calcul cumul

cl=0
for cpl in  elo_opp:
    cl+=classement_depart-evalNewRating(cpl[0],cpl[1])

print("classement apres= ",classement_depart-cl, " delta =",-cl)