from threading import Timer
from django.shortcuts import get_object_or_404
from transactions.serializers import TransactionSerializer
from games.models import Game
import datetime
from users.models import User
from bets.models import Bet


def run():
    Timer(10800, run).start()
    # print("Din din na conta do pai")
    # user = get_object_or_404(User, id="2bd4a6c8-0d74-4731-bd46-440c2641917a")

    # money = {"value": 100}

    # serializer = TransactionSerializer(data=money)
    # serializer.is_valid(raise_exception=True)
    # serializer.save(user=user)
    games = Game.objects.exclude(initial_date=None)
    now_in_sec = datetime.datetime.now().timestamp()
    for game in games:
        game_date_in_sec = datetime.datetime(
            game.initial_date.year, 
            game.initial_date.month, 
            game.initial_date.day
        ).timestamp()
        if game_date_in_sec >= now_in_sec:
            bet_to_close = Bet
        
