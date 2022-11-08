from games.models import Game
from utils.game_name_phase import Phase, Names
import ipdb
import datetime
from bets.models import Bet
from championships.models import Championship
from bet_types.models import BetType


def update_quarter_games():
    # print("="*150)
    # print("Server executando, looping rodando")
    # print("="*150)
    
    # CHAMPIONSHIP HAS 8 GAMES VERIFICATION
    champs_all = Championship.objects.all()

    for champ in champs_all:
        
        now = datetime.datetime.now().timestamp()
        champ_date_in_sec = datetime.datetime(
            champ.initial_date.year, 
            champ.initial_date.month, 
            champ.initial_date.day
        ).timestamp()
        
        if champ.teams.count() == 8 and champ_date_in_sec < now:
            # VERIFICAR INITIAL DATE
            
            game_to_avaliate = Game.objects.get(phase=Phase.QUARTERS_UPPER, name=Names.GAME_1, championship=champ)
            if game_to_avaliate.team_1 == None:
                # EMBARALHAR TIMES ENTRE OS QUATER_UPPER GAMES
                teams_champ = [c for c in champ.teams]
                teams_champ.sort()
                game_to_update = Game.objects.get(phase=Phase.QUARTERS_UPPER, name=Names.GAME_1, championship=champ)
                game_to_update.team_1 = teams_champ[0]
                game_to_update.team_2 = teams_champ[1]
                game_to_update.save()
                bet = {
                "team_1": teams_champ[0],
                "team_2": teams_champ[1]
                }
                bet_created = Bet.objects.create(**bet, game=game_to_update)
                bet_type_1 = {
                    "team": teams_champ[0]
                }
                bet_type_2 = {
                    "team": teams_champ[1]
                }
                BetType.objects.create(**bet_type_1, bet=bet_created)
                BetType.objects.create(**bet_type_2, bet=bet_created)
                game_to_update = Game.objects.get(phase=Phase.QUARTERS_UPPER, name=Names.GAME_2, championship=champ)
                game_to_update.team_1 = teams_champ[2]
                game_to_update.team_2 = teams_champ[3]
                game_to_update.save()
                bet = {
                "team_1": teams_champ[2],
                "team_2": teams_champ[3]
                }
                bet_created = Bet.objects.create(**bet, game=game_to_update)
                bet_type_1 = {
                    "team": teams_champ[2]
                }
                bet_type_2 = {
                    "team": teams_champ[3]
                }
                BetType.objects.create(**bet_type_1, bet=bet_created)
                BetType.objects.create(**bet_type_2, bet=bet_created)
                game_to_update = Game.objects.get(phase=Phase.QUARTERS_UPPER, name=Names.GAME_3, championship=champ)
                game_to_update.team_1 = teams_champ[4]
                game_to_update.team_2 = teams_champ[5]
                game_to_update.save()
                bet = {
                "team_1": teams_champ[4],
                "team_2": teams_champ[5]
                }
                bet_created = Bet.objects.create(**bet, game=game_to_update)
                bet_type_1 = {
                    "team": teams_champ[4]
                }
                bet_type_2 = {
                    "team": teams_champ[5]
                }
                BetType.objects.create(**bet_type_1, bet=bet_created)
                BetType.objects.create(**bet_type_2, bet=bet_created)
                game_to_update = Game.objects.get(phase=Phase.QUARTERS_UPPER, name=Names.GAME_4, championship=champ)
                game_to_update.team_1 = teams_champ[6]
                game_to_update.team_2 = teams_champ[7]
                game_to_update.save()
                bet = {
                "team_1": teams_champ[6],
                "team_2": teams_champ[7]
                }
                bet_created = Bet.objects.create(**bet, game=game_to_update)
                bet_type_1 = {
                    "team": teams_champ[6]
                }
                bet_type_2 = {
                    "team": teams_champ[7]
                }
                BetType.objects.create(**bet_type_1, bet=bet_created)
                BetType.objects.create(**bet_type_2, bet=bet_created)