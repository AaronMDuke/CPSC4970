from module5.identified_object import IdentifiedObject
from module5.custom_exception import DuplicateOid


class League(IdentifiedObject):
    def __init__(self, oid, name):
        super().__init__(oid)
        self.name = name
        self._teams = []
        self._competitions = []

    @property
    def teams(self):
        return self._teams

    @property
    def competitions(self):
        return self._competitions

    def add_team(self, team):
        for existing in self._teams:
            if existing.oid == team.oid:
                raise DuplicateOid(team.oid)
        self._teams.append(team)

    def remove_team(self, team):
        for competition in self._competitions:
            if team in competition.teams_competing:
                raise ValueError("Team cannot be removed from competition")
        if team in self._teams:
            self._teams.remove(team)

    def team_named(self, team_name):
        return next((t for t in self._teams if t.name == team_name), None)

    def add_competition(self, competition):
        for team in competition.teams_competing:
            if team not in self._teams:
                raise ValueError("This team isn't in the league")
        self._competitions.append(competition)


    def teams_for_member(self, member):
        return [t for t in self._teams if member in t.members]

    def competitions_for_team(self, team):
        return [c for c in self._competitions if team in c.teams_competing]

    def competitions_for_member(self, member):
        teams = self.teams_for_member(member)
        return [c for c in self._competitions if any(t in c.teams_competing for t in teams)]

    def __str__(self):
        return f"{self.name}: {len(self._teams)} teams, {len(self._competitions)} competition"