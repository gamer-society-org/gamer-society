from games.models import Game, Phase, Names
from django.test import TestCase
from championships.models import Championship
from users.models import User


class GameModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_staff_data = {
            "username": "Shiryu",
            "nickname": "vshiryu",
            "password": "1234",
            "birthday": "1995-05-15",
            "email": "kkk@kkk.com",
            "is_player": False,
            "is_staff": True,
        }

        cls.championship_data = {
            "name": "CS:GO Major",
            "initial_date": "2023-01-01",
            "e_sport": "Counter Strike",
            "entry_amount": 10,
            "prize": 100000,
        }

        cls.game_data = {
            "name": "Game 1",
            "phase": "Quartas Upper",
        }
        cls.user_staff = User.objects.create_user(**cls.user_staff_data)
        cls.championship = Championship.objects.create(
            **cls.championship_data, staff_owner=cls.user_staff
        )
        cls.game = Game.objects.get_or_create(
            **cls.game_data, championship=cls.championship
        )[0]

    def test_game_fields(self):
        self.assertEqual(self.game.name, self.game_data["name"])
        self.assertEqual(self.game.phase, self.game_data["phase"])
        self.assertIsNone(self.game.winner)
        self.assertIsNone(self.game.result_team_1)
        self.assertIsNone(self.game.result_team_2)
        self.assertIsNone(self.game.team_1)
        self.assertIsNone(self.game.team_2)

    def test_game_name_choices(self):
        choices = [obj.value for obj in (Names)]
        self.assertIn(self.game.name, choices)

    def test_game_phase_choices(self):
        choices = [obj.value for obj in (Phase)]
        self.assertIn(self.game.phase, choices)
