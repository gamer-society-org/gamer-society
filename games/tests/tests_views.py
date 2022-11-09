from rest_framework.test import APIClient
from django.test import TestCase
from users.models import User
from games.models import Game
from championships.models import Championship
from teams.models import Team
from rest_framework.authtoken.models import Token
from historys.models import History
import math

client = APIClient()


class GamesViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.staff_data = {
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
            "entry_amount": 0,
            "prize": 100000,
        }

        cls.players_data = [
            {
                "username": f"player{i}",
                "nickname": f"Player{i}",
                "password": "1234",
                "birthday": "1995-05-15",
                "email": f"kkk{i}@kkk.com",
                "is_player": True,
            }
            for i in range(40)
        ]

        cls.teams_data = [
            {
                "name": f"Team{i}",
                "initials": f"TM{i}",
                "wins": 0,
                "losses": 0,
                "e_sport": "Counter Strike",
            }
            for i in range(8)
        ]

        cls.user_staff = User.objects.create_user(**cls.staff_data)

        cls.teams = []
        for item in cls.teams_data:
            cls.teams.append(Team.objects.create(**item))

        cls.players = []
        for i, item in enumerate(cls.players_data):
            cls.players.append(
                User.objects.create_user(**item, team=cls.teams[math.floor(i / 5)])
            )
            History.objects.create(user=cls.players[i])

    def test_edit_game_staff(self):
        token_staff = Token.objects.create(user=self.user_staff)
        client.credentials(HTTP_AUTHORIZATION=f"Token {token_staff}")

        championship_data = client.post(
            "/api/championships/register/", self.championship_data
        ).data

        championship = Championship.objects.get(id=championship_data["id"])
        teams = Team.objects.all()

        for team in teams:
            owner_team = team.users.all()[0]
            owner_team.is_team_owner = True
            owner_team.save()

        token_owner1 = Token.objects.create(user=self.players[0])
        client.credentials(HTTP_AUTHORIZATION=f"Token {token_owner1}")
        client.patch(f"/api/championships/{championship.id}/add-teams/{teams[0].id}/")

        token_owner2 = Token.objects.create(user=self.players[5])
        client.credentials(HTTP_AUTHORIZATION=f"Token {token_owner2}")
        client.patch(f"/api/championships/{championship.id}/add-teams/{teams[1].id}/")

        token_owner3 = Token.objects.create(user=self.players[10])
        client.credentials(HTTP_AUTHORIZATION=f"Token {token_owner3}")
        client.patch(f"/api/championships/{championship.id}/add-teams/{teams[2].id}/")

        token_owner4 = Token.objects.create(user=self.players[15])
        client.credentials(HTTP_AUTHORIZATION=f"Token {token_owner4}")
        client.patch(f"/api/championships/{championship.id}/add-teams/{teams[3].id}/")

        token_owner5 = Token.objects.create(user=self.players[20])
        client.credentials(HTTP_AUTHORIZATION=f"Token {token_owner5}")
        client.patch(f"/api/championships/{championship.id}/add-teams/{teams[4].id}/")

        token_owner6 = Token.objects.create(user=self.players[25])
        client.credentials(HTTP_AUTHORIZATION=f"Token {token_owner6}")
        client.patch(f"/api/championships/{championship.id}/add-teams/{teams[5].id}/")

        token_owner7 = Token.objects.create(user=self.players[30])
        client.credentials(HTTP_AUTHORIZATION=f"Token {token_owner7}")
        client.patch(f"/api/championships/{championship.id}/add-teams/{teams[6].id}/")

        token_owner8 = Token.objects.create(user=self.players[35])
        client.credentials(HTTP_AUTHORIZATION=f"Token {token_owner8}")
        client.patch(f"/api/championships/{championship.id}/add-teams/{teams[7].id}/")

        games = Game.objects.filter(championship=championship)

        client.credentials(HTTP_AUTHORIZATION=f"Token {token_staff}")
        response = client.put(
            f"/api/games/{games[0].id}/",
            {
                "team_1": championship.teams.all()[0].id,
                "team_2": championship.teams.all()[1].id,
                "initial_date": "2023-01-02",
            },
        )

        game = Game.objects.get(id=games[0].id)
        
        team_1 = Team.objects.get(id=game.team_1)
        team_2 = Team.objects.get(id=game.team_2)

        client.credentials(HTTP_AUTHORIZATION=f"Token {token_owner8}")
        response_error = client.put(
            f"/api/games/{games[0].id}/",
            {
                "team_1": championship.teams.all()[0].id,
                "team_2": championship.teams.all()[1].id,
                "initial_date": "2023-01-02",
            },
        )

        self.assertIsInstance(team_1, Team)
        self.assertIsInstance(team_2, Team)
        self.assertEqual(403, response_error.status_code)

    # Teste comentando pois não deve ser possível deletar um ganme de forma isolada, eles são deletados junto com o championship inteiro.
    # def test_delete_game_staff(self):
    #     token_staff = Token.objects.create(user=self.user_staff)
    #     client.credentials(HTTP_AUTHORIZATION=f"Token {token_staff}")

    #     response = client.delete(
    #         f"/api/championships/{self.championship.id}/games/{self.game.id}"
    #     )

    #     self.assertEqual(204, response.status_code)

    # def test_delete_game_another_staff(self):
    #     token_staff2 = Token.objects.create(user=self.user_staff2)
    #     client.credentials(HTTP_AUTHORIZATION=f"Token {token_staff2}")

    #     response = client.delete(
    #         f"/api/championships/{self.championship.id}/games/{self.game.id}"
    #     )

    #     self.assertEqual(403, response.status_code)