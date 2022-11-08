from games.models import Game
import datetime
from bets.models import Bet

def update_bets():
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
            