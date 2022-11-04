from rest_framework import permissions
from rest_framework.views import Request, View, status
from championships.models import Championship
from teams.models import Team


class IsChampionshipOwner(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: View, champs: Championship
    ) -> bool:
        self.message = "You're not the championship owner to perform this action"
        return request.user.is_authenticated and request.user == champs.staff_owner


class IsATeamOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, team: Team) -> bool:
        self.message = "You're not a team owner to perform this action"
        check_owner = False

        for user in team.users.all():
            if user.id == request.user.id and user.is_team_owner:
                check_owner = True

        return check_owner


class HaveFivePlayers(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, team: Team) -> bool:
        self.message = "Your must have at least 5 players"

        team_players_length = team.users.count()

        return team_players_length >= 5


class IsTeamEsportCorrectly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, team: Team) -> bool:
        message = "Your team do not have same e-sport"
        code = status.HTTP_400_BAD_REQUEST

        cs_id = view.kwargs["cs_id"]
        champ = Championship.objects.get(id=cs_id)

        return team.e_sports == champ.e_sport


class IsChampionshipFull(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, team: Team) -> bool:
        message = "The championship is full"
        code = status.HTTP_400_BAD_REQUEST

        cs_id = view.kwargs["cs_id"]
        champ = Championship.objects.get(id=cs_id)

        number_teams = champ.teams.count()

        return number_teams < 8


class HasAnotherChampAroundSevenDays(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, team: Team) -> bool:
        if team.championship.count() == 0:
            return True
        self.message = "You've other championship around this championship date"


class IsChampOwnerTryngToEnterInIt(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, team: Team) -> bool:
        self.message = "Championship owner can't play it"
        cs_id = view.kwargs["cs_id"]
        champ = Championship.objects.get(id=cs_id)
        champ_owner_id = champ.staff_owner.id
        
        for user in team.users.all():
            if user.id == champ_owner_id:
                return False
        
        return True