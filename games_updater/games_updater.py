from games.models import Game
from utils.game_name_phase import Phase, Names
import ipdb
import datetime
from bets.models import Bet
from championships.models import Championship


def update_games():
    print("="*150)
    print("Server executando")
    print("="*150)
    # prize = {"value": 100}
    # user_to_reward = User.objects.get(username="Gus")
    # trans = TransactionSerializer(data=prize)
    # trans.is_valid(raise_exception=True)
    # trans.save(user=user_to_reward)
    
    
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
            
    # CHAMPIONSHIP HAS 8 GAMES VERIFICATION
    
    champs_all = Championship.objects.all()
    
    for champ in champs_all:
        if champ.teams.count() == 8:
            # EMBARALHAR TIMES ENTRE OS QUATER_UPPER GAMES
            ...        
    
            
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
                    game_to_update_lower = Game.objects.filter(phase=Phase.SEMI_LOWER_1, name=Names.GAME_1, championship=champ)
                    if game_to_update_upper.team_1 == None:
                        game_to_update_upper.team_1 = winner_id
                        game_to_update_upper.save()
                    if game_to_update_lower.team_1 == None:
                        game_to_update_lower.team_1 = looser_id   
                        game_to_update_lower.save()
                    
                        
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
                    game_to_update_lower = Game.objects.filter(phase=Phase.SEMI_LOWER_1, name=Names.GAME_1, championship=champ)
                    if game_to_update_upper.team_2 == None:
                        game_to_update_upper.team_2 = winner_id
                        game_to_update_upper.save()
                    if game_to_update_lower.team_2 == None:
                        game_to_update_lower.team_2 = looser_id
                        game_to_update_lower.save()
                        
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
                    game_to_update_lower = Game.objects.filter(phase=Phase.SEMI_LOWER_1, name=Names.GAME_2, championship=champ)
                    if game_to_update_upper.team_1 == None:
                        game_to_update_upper.team_1 = winner_id
                        game_to_update_upper.save()
                    if game_to_update_lower.team_1 == None:
                        game_to_update_lower.team_1 = looser_id
                        game_to_update_lower.save()
                        
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
                    game_to_update_lower = Game.objects.filter(phase=Phase.SEMI_LOWER_1, name=Names.GAME_2, championship=champ)
                    if game_to_update_upper.team_2 == None:
                        game_to_update_upper.team_2 = winner_id
                        game_to_update_upper.save()
                    if game_to_update_lower.team_2 == None:
                        game_to_update_lower.team_2 = looser_id
                        game_to_update_lower.save()
                        
                        
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
                    game_to_update_lower = Game.objects.filter(phase=Phase.SEMI_LOWER_2, name=Names.GAME_1, championship=champ)
                    if game_to_update_upper.team_1 == None:
                        game_to_update_upper.team_1 = winner_id
                        game_to_update_upper.save()
                    if game_to_update_lower.team_1 == None:
                        game_to_update_lower.team_1 = looser_id
                        game_to_update_lower.save()
                
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
                    game_to_update_lower = Game.objects.filter(phase=Phase.SEMI_LOWER_2, name=Names.GAME_2, championship=champ)
                    if game_to_update_upper.team_2 == None:
                        game_to_update_upper.team_2 = winner_id
                        game_to_update_upper.save()
                    if game_to_update_lower.team_1 == None:
                        game_to_update_lower.team_1 = looser_id
                        game_to_update_lower.save()
                        
                        
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
                game_to_update_lower = Game.objects.filter(phase=Phase.FINAL_LOWER_2, name=Names.GAME_1, championship=champ)
                if game_to_update_upper.team_1 == None:
                        game_to_update_upper.team_1 = winner_id
                        game_to_update_upper.save()
                if game_to_update_lower.team_1 == None:
                        game_to_update_lower.team_1 = looser_id
                        game_to_update_lower.save()
                        
            if game.phase == Phase.SEMI_LOWER_1:
                
                if game.name == Names.GAME_1:
                    
                    winner_id = None
                    looser_id = None
                    if game.team_1 == game.winner:
                        winner_id = game.team_1
                        looser_id = game.team_2
                    elif game.team_2 == game.winner:
                        winner_id = game.team_2
                        looser_id = game.team_1
                        
                    game_to_update_continue_lower = Game.objects.filter(phase=Phase.SEMI_LOWER_2, name=Names.GAME_1, championship=champ)
                    if game_to_update_continue_lower.team_2 == None:
                        game_to_update_continue_lower.team_2 = winner_id
                        game_to_update_continue_lower.save()
                        
                if game.name == Names.GAME_2:
                    
                    winner_id = None
                    looser_id = None
                    if game.team_1 == game.winner:
                        winner_id = game.team_1
                        looser_id = game.team_2
                    elif game.team_2 == game.winner:
                        winner_id = game.team_2
                        looser_id = game.team_1
                        
                    game_to_update_continue_lower = Game.objects.filter(phase=Phase.SEMI_LOWER_2, name=Names.GAME_2, championship=champ)
                    if game_to_update_continue_lower.team_2 == None:
                        game_to_update_continue_lower.team_2 = winner_id
                        game_to_update_continue_lower.save()
                        
            if game.phase == Phase.SEMI_LOWER_2:
                
                if game.name == Names.GAME_1:
                    
                    winner_id = None
                    looser_id = None
                    if game.team_1 == game.winner:
                        winner_id = game.team_1
                        looser_id = game.team_2
                    elif game.team_2 == game.winner:
                        winner_id = game.team_2
                        looser_id = game.team_1
                        
                    game_to_update_continue_lower = Game.objects.filter(phase=Phase.FINAL_LOWER_1, name=Names.GAME_1, championship=champ)
                    if game_to_update_continue_lower.team_1 == None:
                        game_to_update_continue_lower.team_1 = winner_id
                        game_to_update_continue_lower.save()
                        
                if game.name == Names.GAME_2:
                    
                    winner_id = None
                    looser_id = None
                    if game.team_1 == game.winner:
                        winner_id = game.team_1
                        looser_id = game.team_2
                    elif game.team_2 == game.winner:
                        winner_id = game.team_2
                        looser_id = game.team_1
                        
                    game_to_update_continue_lower = Game.objects.filter(phase=Phase.FINAL_LOWER_1, name=Names.GAME_1, championship=champ)
                    if game_to_update_continue_lower.team_2 == None:
                        game_to_update_continue_lower.team_2 = winner_id
                        game_to_update_continue_lower.save()
                
            if game.phase == Phase.FINAL_LOWER_1:
            
                winner_id = None
                looser_id = None
                if game.team_1 == game.winner:
                    winner_id = game.team_1
                    looser_id = game.team_2
                elif game.team_2 == game.winner:
                    winner_id = game.team_2
                    looser_id = game.team_1
                        
                game_to_update_continue_lower = Game.objects.filter(phase=Phase.FINAL_LOWER_2, name=Names.GAME_1, championship=champ)
                if game_to_update_continue_lower.team_2 == None:
                    game_to_update_continue_lower.team_2 = winner_id
                    game_to_update_continue_lower.save()
                
            if game.phase == Phase.FINAL_LOWER_2:
                
                winner_id = None
                looser_id = None
                if game.team_1 == game.winner:
                    winner_id = game.team_1
                    looser_id = game.team_2
                elif game.team_2 == game.winner:
                    winner_id = game.team_2
                    looser_id = game.team_1
                        
                game_to_update_continue_lower = Game.objects.filter(phase=Phase.FINAL_CHAMPIONS, name=Names.GAME_1, championship=champ)
                if game_to_update_continue_lower.team_2 == None:
                    game_to_update_continue_lower.team_2 = winner_id
                    game_to_update_continue_lower.save()
    
    