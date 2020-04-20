import json
import datetime
from random import seed
from random import shuffle

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

NEWLINE = "\n"

today = datetime.date.today()
day_of_week = today.weekday()
week = 0
#day_of_week override
#day_of_week = 0

def main():
    todays_file = open(f"{today}.csv","w")
    with open("schedule.json") as json_file:
        schedules = json.load(json_file)
        for schedule in schedules:
            player = schedule[0]
            if schedule[day_of_week + 1] == 1:
                player_stats = []
                with open(f"data/{player}.json") as player_file:
                    player_stats = json.load(player_file)
                    shuffle(player_stats)
                    selection = player_stats.pop()
                    todays_file.write(f"{player},{day_of_week + week},{selection[GAME_SCORE]},{selection[MP]},{selection[FG]},{selection[FGA]},{selection[FT]},{selection[FTA]},{selection[FG3]},{selection[PTS]},{selection[TRB]},{selection[AST]},{selection[STL]},{selection[BLK]}{NEWLINE}")
                playerFile = open(f"data/{player}.json", "w")
                newJson = json.dumps(player_stats)
                playerFile.write(newJson)
                playerFile.close()
    todays_file.close()

if __name__ == '__main__':
    main()
