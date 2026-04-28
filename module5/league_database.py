import csv
import os
import pickle

from module5.team import Team
from module5.team_member import TeamMember

class LeagueDatabase:
    _sole_instance = None

    def __init__(self):
        self._leagues = []
        self._last_oid = 0


    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance


    @classmethod
    def load(cls, file_name):
        try:
            with open(file_name, 'rb') as f:
                cls._sole_instance = pickle.load(f)
            return
        except Exception as e:
            print(f"Could not load {file_name}: {e}")

        backup = file_name + ".backup"
        if os.path.exists(backup):
            try:
                with open(backup, 'rb') as f:
                    cls._sole_instance = pickle.load(f)
            except Exception as e:
                print(f"Could not load {backup}: {e}")


    @property
    def leagues(self):
        return self._leagues


    def add_league(self, league):
        self._leagues.append(league)


    def remove_league(self, league):
        if league in self._leagues:
            self._leagues.remove(league)


    def league_named(self, name):
        for league in self._leagues:
            if league.name == name:
                return league
        return None


    def next_oid(self):
        self._last_oid += 1
        return self._last_oid


    def save(self, file_name):
        if os.path.exists(file_name):
            os.replace(file_name, file_name + ".backup")
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)


    def import_league_teams(self, league, file_name):
        try:
            with open(file_name, "r", encoding="utf-8", newline="") as f:
                reader = csv.reader(f)
                next(reader)
                for team_name, member_name, email in reader:
                    team = league.team_named(team_name)
                    if team is None:
                        team = Team(self.next_oid(), team_name)
                        league.add_team(team)
                    team.add_member(TeamMember(self.next_oid(), member_name, email))
        except Exception as e:
            print(f"Could not import {file_name}: {e}")


    def export_league_teams(self, league, file_name):
        try:
            with open(file_name, "w", encoding ="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Team name", "Member name", "Member email"])
                for team in league.teams:
                    for member in team.members:
                        writer.writerow([team.name, member.name, member.email])
        except Exception as e:
            print(f"Could not export {file_name}: {e}")





