import unittest
from module5.league import League
from module5.team import Team
from module5.team_member import TeamMember
from module5.competition import Competition
from module5.custom_exception import DuplicateOid


class LeagueTest(unittest.TestCase):
    def test_str(self):
        league = League(1, "SE Region Curling League")
        league.add_team(Team(1, "Team 1"))
        league.add_team(Team(2, "Team 2"))
        league.add_competition(Competition(1, [], "Here", None))
        self.assertEqual("SE Region Curling League: 2 teams, 1 competition", str(league))

    def test_duplicate_teams(self):
        league = League(1, "SE Region Curling League")
        t = Team(1, "Team 1")
        league.add_team(t)
        with self.assertRaises(DuplicateOid):
            league.add_team(t)

    def test_remove_team(self):
        league = League(1, "SE Region Curling League")
        t = Team(1, "Team 1")
        league.add_team(t)
        league.remove_team(t)
        self.assertNotIn(t, league.teams)

    def test_add_team(self):
        league = League(1, "SE Region Curling League")
        t = Team(1, "Blue Team")
        league.add_team(t)
        self.assertIn(t, league.teams)

    def test_add_competition(self):
        league = League(1, "SE Region Curling League")
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        league.add_team(t1)
        league.add_team(t2)
        comp = Competition(1, [t1, t2], "vs", None)
        league.add_competition(comp)
        self.assertIn(comp, league.competitions)

    def test_duplicate_oid(self):
        league = League(1, "SE Region Curling League")
        league.add_team(Team(1, "Team 1"))
        with self.assertRaises(DuplicateOid):
            league.add_team(Team(1, "Team One"))



    if __name__ == "__main__":
        unittest.main()
