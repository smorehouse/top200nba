import requests
from bs4 import BeautifulSoup
import json

MP = "mp"
FG = "fg"
FGA = "fga"
FG3 = "fg3"
FT = "ft"
FTA = "fta"
TRB = "trb"
AST = "ast"
STL = "stl"
BLK = "blk"
PTS = "pts"
GAME_SCORE = "game_score"

GAME_SEASON = "game_season"
RANKER = "ranker"

inputFile = open("players.txt","r")
for line in inputFile:
    player = line.split(',')[0]
    year = line.split(',')[1].rstrip()
    url = f"https://www.basketball-reference.com/players/b/{player}/gamelog/{year}/"
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find(id='pgl_basic')
    body = table.find('tbody')
    rows = body.findAll('tr')
    playerFile = open(f"{player}-{year}.txt", "w")
    gameList = []
    for row in rows:
        ranker = row.findAll("th", {"data-stat": RANKER})[0].text
        if ranker != "Rk":
            game_season = row.findAll("td", {"data-stat": GAME_SEASON})[0].text
            if game_season:
                game = {}
                game[MP] = row.findAll("td", {"data-stat": MP})[0].text
                game[FG] = row.findAll("td", {"data-stat": FG})[0].text
                game[FGA] = row.findAll("td", {"data-stat": FGA})[0].text
                game[FG3] = row.findAll("td", {"data-stat": FG3})[0].text
                game[FT] = row.findAll("td", {"data-stat": FT})[0].text
                game[FTA] = row.findAll("td", {"data-stat": FTA})[0].text
                game[TRB] = row.findAll("td", {"data-stat": TRB})[0].text
                game[AST] = row.findAll("td", {"data-stat": AST})[0].text
                game[STL] = row.findAll("td", {"data-stat": STL})[0].text
                game[BLK] = row.findAll("td", {"data-stat": BLK})[0].text
                game[PTS] = row.findAll("td", {"data-stat": PTS})[0].text
                game[GAME_SCORE] = row.findAll("td", {"data-stat": GAME_SCORE})[0].text
                jsonDict = json.dumps(game)
                playerFile.write(jsonDict)
    playerFile.close()
inputFile.close()
