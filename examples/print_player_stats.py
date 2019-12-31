import os
import json

from yahoo_fantasy_api import league, game, team
from yahoo_oauth import OAuth2

if not os.path.exists('oauth2.json'):
    creds = {'consumer_key': 'my_key', 'consumer_secret': 'my_secret'}
    with open('oauth2.json', "w") as f:
        f.write(json.dumps(creds))

oauth = OAuth2(None, None, from_file='oauth2.json')
gm = game.Game(oauth, 'nhl')
ids = gm.league_ids()
print(ids)
# 53432
lg = league.League(oauth,'396.l.53432')
my_team: team.Team= lg.to_team(lg.team_key())
roster = my_team.roster(lg.current_week())

stats = lg.player_stats([roster[0]['player_id']])
pass