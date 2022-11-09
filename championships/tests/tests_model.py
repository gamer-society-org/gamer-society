from django.test import TestCase
from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from championships.models import Championship
from games.models import Game

client = APIClient()


class ChampionshipModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_staff = {
            "username": "Gustavo",
            "nickname": "Buiu",
            "password": "1234",
            "birthday": "2000-05-22",
            "email": "gustavo@email.com",
            "is_player": False,
            "is_staff": True,
        }
        cls.championship = {
            "name": "VALORANT $75 PRIZE",
            "initial_date": "2022-11-22",
            "e_sport": "Valorant",
            "entry_amount": 10.0,
            "prize": 75.0,
        }

    def test_create_champ_model(self):
        # testar se cria 11 jogos
        # testar se jogos estão vazios
        # testar relacionamento com user, se retorna staff_owner_id
        user = User.objects.create_user(**self.user_staff)

        champ = Championship.objects.create(**self.championship, staff_owner=user)

        self.assertEqual(self.championship["name"], champ.name)
        self.assertEqual(self.championship["initial_date"], champ.initial_date)
        self.assertEqual(self.championship["e_sport"], champ.e_sport)
        self.assertEqual(self.championship["entry_amount"], champ.entry_amount)
        self.assertEqual(self.championship["prize"], champ.prize)
        self.assertIsInstance(champ.staff_owner, User)

