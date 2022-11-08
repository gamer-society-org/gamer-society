from games.models import Game
from utils.game_name_phase import Phase, Names
from championships.models import Championship


def update_semi_foward_games():    
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
                    
                    game_to_update_upper = Game.objects.get(phase=Phase.SEMI_UPPER, name=Names.GAME_1, championship=champ)
                    game_to_update_lower = Game.objects.get(phase=Phase.SEMI_LOWER_1, name=Names.GAME_1, championship=champ)
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
                    
                    game_to_update_upper = Game.objects.get(phase=Phase.SEMI_UPPER, name=Names.GAME_1, championship=champ)
                    game_to_update_lower = Game.objects.get(phase=Phase.SEMI_LOWER_1, name=Names.GAME_1, championship=champ)
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
                    
                    game_to_update_upper = Game.objects.get(phase=Phase.SEMI_UPPER, name=Names.GAME_2, championship=champ)
                    game_to_update_lower = Game.objects.get(phase=Phase.SEMI_LOWER_1, name=Names.GAME_2, championship=champ)
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
                    
                    game_to_update_upper = Game.objects.get(phase=Phase.SEMI_UPPER, name=Names.GAME_2, championship=champ)
                    game_to_update_lower = Game.objects.get(phase=Phase.SEMI_LOWER_1, name=Names.GAME_2, championship=champ)
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
                    
                    game_to_update_upper = Game.objects.get(phase=Phase.FINAL_UPPER, name=Names.GAME_1, championship=champ)
                    game_to_update_lower = Game.objects.get(phase=Phase.SEMI_LOWER_2, name=Names.GAME_1, championship=champ)
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
                        
                    game_to_update_upper = Game.objects.get(phase=Phase.FINAL_UPPER, name=Names.GAME_1, championship=champ)
                    game_to_update_lower = Game.objects.get(phase=Phase.SEMI_LOWER_2, name=Names.GAME_2, championship=champ)
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
                    
                game_to_update_upper = Game.objects.get(phase=Phase.FINAL_CHAMPIONS, name=Names.GAME_1, championship=champ)
                game_to_update_lower = Game.objects.get(phase=Phase.FINAL_LOWER_2, name=Names.GAME_1, championship=champ)
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
                        
                    game_to_update_continue_lower = Game.objects.get(phase=Phase.SEMI_LOWER_2, name=Names.GAME_1, championship=champ)
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
                        
                    game_to_update_continue_lower = Game.objects.get(phase=Phase.SEMI_LOWER_2, name=Names.GAME_2, championship=champ)
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
                        
                    game_to_update_continue_lower = Game.objects.get(phase=Phase.FINAL_LOWER_1, name=Names.GAME_1, championship=champ)
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
                        
                    game_to_update_continue_lower = Game.objects.get(phase=Phase.FINAL_LOWER_1, name=Names.GAME_1, championship=champ)
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
                        
                game_to_update_continue_lower = Game.objects.get(phase=Phase.FINAL_LOWER_2, name=Names.GAME_1, championship=champ)
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
                        
                game_to_update_continue_lower = Game.objects.get(phase=Phase.FINAL_CHAMPIONS, name=Names.GAME_1, championship=champ)
                if game_to_update_continue_lower.team_2 == None:
                    game_to_update_continue_lower.team_2 = winner_id
                    game_to_update_continue_lower.save()
    
    