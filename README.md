# top200nba
top 200 nba player seasons between 00-19

To run a days stats, python get-stats.py

This will remove the randomly selected game from the players data/{player_name}.json file. 

You can test this with: grep -o game_score data/{player_name}.json | wc -l .

Every player starts with 32 games, after running get-stats.py once it should running the above command should return 31 if that player was active today. 

Schedules are set in schedules.json, feel free to edit this. Right now, half the league is M-W-F-Sun and the other half is Tu-Th-Sat-Sun. 
