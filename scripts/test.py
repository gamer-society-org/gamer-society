from threading import Timer
from django.shortcuts import get_object_or_404
from transactions.serializers import TransactionSerializer
from games.models import Game
from utils.game_name_phase import Phase, Names
import ipdb
import datetime
from users.models import User
from bets.models import Bet
from teams.models import Team
from championships.models import Championship


def run():
    print('+'*100)
    # GAMES INITIAL DATE VERIFICATION
    games = Game.objects.exclude(initial_date=None)
    now_in_sec = datetime.datetime.now().timestamp()
    for game in games:
        game_date_in_sec = datetime.datetime(
            game.initial_date.year, 
            game.initial_date.month, 
            game.initial_date.day
        ).timestamp()
        if game_date_in_sec >= now_in_sec:
            bet_to_close = Bet.objects.get(id=game.bet.id)
            if bet_to_close.is_active:
                bet_to_close.is_active = False
                bet_to_close.save()
            
    # GAMES WINNER VERIFICATION
    champs = Championship.objects.all()
    games_winners = Game.objects.exclude(winner=None)
    
    for champ in champs:
        games_winners = Game.objects.exclude(winner=None).filter(championship=champ)
        for game in games_winners:
            
            if game.phase == Phase.QUARTERS_UPPER:
                
                if game.name == Names.GAME_1:
                    
                    winner_id = None
                    looser_id = None
                    if game.team_1 == game.winner:
                        winner_id = game.team_1
                        looser_id = game.team_2
                    elif game.team_2 == game.winner:
                        winner_id = game.team_2
                        looser_id = game.team_1
                    
                    game_to_update_upper = Game.objects.filter(phase=Phase.SEMI_UPPER, name=Names.GAME_1, championship=champ)
                    game_to_update_lower = Game.objects.filter(phase=Phase.SEMI_LOWER, name=Names.GAME_1, championship=champ)
                    if game_to_update_upper.team_1 == None:
                        game_to_update_upper.team_1 = winner_id
                    if game_to_update_lower.team_1 == None:
                        game_to_update_lower.team_1 = looser_id    
                    
                        
                if game.name == Names.GAME_2:
                    
                    winner_id = None
                    looser_id = None
                    if game.team_1 == game.winner:
                        winner_id = game.team_1
                        looser_id = game.team_2
                    elif game.team_2 == game.winner:
                        winner_id = game.team_2
                        looser_id = game.team_1
                    
                    game_to_update_upper = Game.objects.filter(phase=Phase.SEMI_UPPER, name=Names.GAME_1, championship=champ)
                    game_to_update_lower = Game.objects.filter(phase=Phase.SEMI_LOWER, name=Names.GAME_1, championship=champ)
                    if game_to_update_upper.team_2 == None:
                        game_to_update_upper.team_2 = winner_id
                    if game_to_update_lower.team_2 == None:
                        game_to_update_lower.team_2 = looser_id
                        
                if game.name == Names.GAME_3:
                    
                    winner_id = None
                    looser_id = None
                    if game.team_1 == game.winner:
                        winner_id = game.team_1
                        looser_id = game.team_2
                    elif game.team_2 == game.winner:
                        winner_id = game.team_2
                        looser_id = game.team_1
                    
                    game_to_update_upper = Game.objects.filter(phase=Phase.SEMI_UPPER, name=Names.GAME_2, championship=champ)
                    game_to_update_lower = Game.objects.filter(phase=Phase.SEMI_LOWER, name=Names.GAME_2, championship=champ)
                    if game_to_update_upper.team_1 == None:
                        game_to_update_upper.team_1 = winner_id
                    if game_to_update_lower.team_1 == None:
                        game_to_update_lower.team_1 = looser_id
                        
                if game.name == Names.GAME_4:
                    
                    winner_id = None
                    looser_id = None
                    if game.team_1 == game.winner:
                        winner_id = game.team_1
                        looser_id = game.team_2
                    elif game.team_2 == game.winner:
                        winner_id = game.team_2
                        looser_id = game.team_1
                    
                    game_to_update_upper = Game.objects.filter(phase=Phase.SEMI_UPPER, name=Names.GAME_2, championship=champ)
                    game_to_update_lower = Game.objects.filter(phase=Phase.SEMI_LOWER, name=Names.GAME_2, championship=champ)
                    if game_to_update_upper.team_2 == None:
                        game_to_update_upper.team_2 = winner_id
                    if game_to_update_lower.team_2 == None:
                        game_to_update_lower.team_2 = looser_id
                        
                        
            if game.phase == Phase.SEMI_UPPER:
                if game.name == Names.GAME_1:
                    winner_id = None
                    looser_id = None
                    if game.team_1 == game.winner:
                        winner_id = game.team_1
                        looser_id = game.team_2
                    elif game.team_2 == game.winner:
                        winner_id = game.team_2
                        looser_id = game.team_1
                    
                    game_to_update_upper = Game.objects.filter(phase=Phase.FINAL_UPPER, name=Names.GAME_1, championship=champ)
                    if game_to_update_upper.team_1 == None:
                        game_to_update_upper.team_1 = winner_id
                
                if game.name == Names.GAME_2:
                    winner_id = None
                    looser_id = None
                    if game.team_1 == game.winner:
                        winner_id = game.team_1
                        looser_id = game.team_2
                    elif game.team_2 == game.winner:
                        winner_id = game.team_2
                        looser_id = game.team_1
                        
                    game_to_update_upper = Game.objects.filter(phase=Phase.FINAL_UPPER, name=Names.GAME_1, championship=champ)
                    if game_to_update_upper.team_2 == None:
                        game_to_update_upper.team_2 = winner_id
                        
                        
            if game.phase == Phase.FINAL_UPPER:
                winner_id = None
                looser_id = None
                if game.team_1 == game.winner:
                    winner_id = game.team_1
                    looser_id = game.team_2
                elif game.team_2 == game.winner:
                    winner_id = game.team_2
                    looser_id = game.team_1
                    
                game_to_update_upper = Game.objects.filter(phase=Phase.FINAL_CHAMPIONS, name=Names.GAME_1, championship=champ)
                if game_to_update_upper.team_1 == None:
                        game_to_update_upper.team_1 = winner_id
                
    
    
    Timer(30, run).start()