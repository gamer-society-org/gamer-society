from django.test import TestCase
from championships.models import Championship
from games.models import Game
from bets.models import Bet
from users.models import User
from bet_types.models import BetType


class BetTypeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.staff_data = {
            "username": "igorribeiro",
            "nickname": "eved_igor",
            "password": "1234",
            "birthday": "1999-08-27",
            "email": "igor@mail.com",
            "is_player": False,
            "is_staff": True,
        }

        cls.championship_data = {
            "name": "The Last of Us II",
            "initial_date": "2023-01-01",
            "e_sport": "Counter Strike",
            "entry_amount": 10,
            "prize": 1000,
        }
        cls.user_staff = User.objects.create_user(**cls.staff_data)

        cls.championship = Championship.objects.create(
            **cls.championship_data,
            staff_owner_id=cls.user_staff.id,
        )

        cls.game_data = {
            "name": "Game 1",
            "phase": "Quartas Upper",
        }

        cls.game = Game.objects.get_or_create(
            **cls.game_data,
            championship=cls.championship,
        )[0]

        cls.bet_data = {
            "team_1": "Vagalumes",
            "team_2": "Estaladores",
        }
        cls.bet = Bet.objects.create(**cls.bet_data, game=cls.game)

        cls.bet_types_data = {
            "team": "Vagalumes",
        }
        cls.bet_types = BetType.objects.create(
            **cls.bet_types_data,
            bet=cls.bet,
        )

    def test_bet_types_fields(self):
        self.assertEqual(self.bet_types.team, self.bet_types_data["team"])
        self.assertEqual(self.bet_types.total_value, 0.0)
        self.assertIsNone(self.bet_types.winner)
