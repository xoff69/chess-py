import chess.pgn
import requests
from datetime import datetime
import csv


username="deriveepartielle"

print("Debut ",username)
fname="C:\\Users/xoffp/Downloads/"+username+"_lichess"+datetime.now().strftime("%Y_%m_%d")+".pgn"
url="https://lichess.org/api/games/user/"+username+"?tags=true&clocks=false&evals=false&opening=true&perfType=ultraBullet%2Cbullet%2Cblitz%2Crapid%2Cclassical%2Ccorrespondence%2Cstandard"
print(fname)

r = requests.get(url)
with open(fname,'wb') as f:
  f.write(r.content)

print("Fin ",username)
player = username
filePgn = open(fname)
def extractStatWhite(data):
    tot=data[0]+data[1]+data[2]
    pcentWorD = 0
    if tot != 0:
        pcentWorD=(data[0]+data[1])/tot
    return "{:.2f}".format(pcentWorD*100)
def extractStatBlack(data):
    tot=data[0]+data[1]+data[2]
    pcentWorD=0
    if tot!=0:
        pcentWorD=(data[1]+data[2])/tot
    return "{:.2f}".format(pcentWorD*100)
def extractNFirstMoves(game,n=2):
    moves = []
    nbmoves = 0
    board = game.board()
    for move in game.mainline_moves():
        moves.append(board.san(move))
        board.push(move)
        nbmoves += 1
        if nbmoves ==n:
            break

    return moves

def fillStatOnResult(stat,result):
    if (result == 0.):
        stat[2] += 1
    else:
        if (result == 1.):
            stat[0] += 1
        else:
            stat[1] += 1
    return stat

def calc1Month(dateTarget):

    count = 0
    countWhite = 0
    countBlack = 0
    # white
    state4c5=[0,0,0]
    state4e5=[0,0,0]
    state4e6=[0,0,0]
    state4d6=[0,0,0]
    state4d5=[0,0,0]
    state4c6=[0,0,0]
    #black
    statd4d5=[0,0,0]
    statNf3=[0,0,0]
    state4 =[0,0,0]
    statc4=[0,0,0]
    # nostat
    nostat=0

    while True:

        game = chess.pgn.read_game(filePgn)
        if game is None:
            break
        count += 1
        # check if the game is in the wanted month.year
        d = game.headers["Date"][0:7]

        if d == dateTarget:
            result = game.headers["Result"]
            resd=0.5
            if result=="1-0":
                resd=1.
            else:
                if result=="0-1":
                    resd=0

            moves = extractNFirstMoves(game)

            first = moves[0]
            second = moves[1]

            if game.headers["White"] == player:
                countWhite += 1


                if first=="e4":
                    match second:
                        case "c5":
                            statc5=fillStatOnResult(state4c5,resd)

                        case "e5":
                            state4e5=fillStatOnResult(state4e5,resd)
                        case          "e6":
                            state4e6 = fillStatOnResult(state4e6, resd)
                        case     "c6":
                            state4c6 = fillStatOnResult(state4c6, resd)
                        case "d6":
                            state4d6 = fillStatOnResult(state4d6, resd)
                        case "d5":
                            state4d5 =  fillStatOnResult(state4d5, resd)
                        case _:
                            nostat+=1


            if game.headers["Black"] == player:
                countBlack += 1
                match first:
                    case "d4":
                            statd4d5 = fillStatOnResult(statd4d5, resd)
                    case     "Nf3":
                            statNf3 = fillStatOnResult(statNf3, resd)
                    case "e4":
                            state4= fillStatOnResult(state4, resd)
                    case "c4":
                            statc4 = fillStatOnResult(statc4, resd)
                    case     _:
                            nostat += 1
    print("Stats : draws are counted positively.")
    print("count=", count)
    print("countWhite=", countWhite)
    print("countBlack=", countBlack)
    print("Na")
    print("NoStat :", nostat)
    return state4c5,    state4e5,    state4e6,    state4d6,    state4d5,    state4c6,    statd4d5,    statNf3,state4,statc4



with open('results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date","Black vs 1. e4", "Black vs 1. d4","Black vs 1. Nf3","Black vs 1. c4", "White: Sicilian", "White: vs e5", "White: Caro", "White: French", "White: Scandi", "White: d6"])

    dateTargets = ["2024.01" ,"2024.02","2024.03","2024.04","2024.05","2024.06","2024.07","2024.08"]
    for dateTarget in dateTargets:
        print("date=",dateTarget)
        state4c5, state4e5, state4e6, state4d6, state4d5, state4c6, statd4d5, statNf3, state4, statc4=calc1Month(dateTarget)
        writer.writerow([dateTarget,extractStatBlack(state4),extractStatBlack(statd4d5),extractStatBlack(statNf3),extractStatBlack(statc4),extractStatWhite(state4c5),extractStatWhite(state4e5),extractStatWhite(state4c6),extractStatWhite(state4e6),extractStatWhite(state4d5),extractStatWhite(state4d6)])