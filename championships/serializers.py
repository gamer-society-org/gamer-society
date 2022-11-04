from rest_framework import serializers
from games.models import Game
from teams.serializers import TeamSerializer, TeamSerializerReturn
from .models import Championship
from utils.game_name_phase import Names, Phase, games_list
from teams.models import Team
from games.serializers import GamesSerializer, GamesLowKeysSerializer


class CreateChampionshipsSerializer(serializers.ModelSerializer):

    games = GamesLowKeysSerializer(read_only=True, many=True)

    class Meta:
        model = Championship
        fields = [
            "id",
            "name",
            "initial_date",
            "e_sport",
            "winner",
            "staff_owner",
            "entry_amount",
            "prize",
            "teams",
            "games",
        ]

        read_only_fields = [
            "id",
            "staff_owner",
            "teams",
        ]

    def create(self, validated_data):
        champ_created = Championship.objects.create(**validated_data)

        for game in games_list:
            Game.objects.create(**game, championship=champ_created)

        return champ_created


class ListChampionshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Championship
        fields = [
            "id",
            "name",
            "initial_date",
            "e_sport",
            "winner",
            "staff_owner",
            "teams",
            "games",
            "teams",
        ]
        read_only_fields = [
            "id",
            "name",
            "initial_date",
            "e_sport",
            "winner",
            "staff_owner",
            "teams",
        ]

        read_only_fields = [
            "id",
            "name",
            "initial_date",
            "e_sport",
            "winner",
            "staff_owner",
            "teams",
        ]

    def update(self, instance, validated_data):
        cs_id = self.context["view"].kwargs["cs_id"]
        championship = Championship.objects.get(id=cs_id)
        instance.championship.add(championship)
        instance.save()
        champ_updated = Championship.objects.get(id=cs_id)

        return champ_updated


class ChampionshipDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Championship
        fields = "__all__"
        read_only_fields = ["id"]


class RetrieveChampionShipWithGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Championship
        fields = "__all__"
        read_only_fields = ["id"]

    games = GamesSerializer(many=True)
    teams = TeamSerializer(many=True)


class RetrieveChampionAddingGamesSerializer(RetrieveChampionShipWithGamesSerializer):

    # games = GamesSerializer(many=True)
    teams = TeamSerializerReturn(many=True)
