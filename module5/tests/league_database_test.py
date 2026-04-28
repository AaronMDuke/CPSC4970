import os
import tempfile
import unittest

from module5.league import League
from module5.league_database import LeagueDatabase


class LeagueDatabaseTest(unittest.TestCase):
    def setUp(self):
        LeagueDatabase._sole_instance = None
        self.db = LeagueDatabase.instance()
        self.temp = tempfile.mkdtemp()


    def test_singleton_instance(self):
        self.assertIs(LeagueDatabase.instance(), self.db)


    def test_next_oid(self):
        self.assertEqual(self.db.next_oid(), 1)
        self.assertEqual(self.db.next_oid(), 2)


    def test_add_league(self):
        league = League(1, "League 1")
        self.db.add_league(league)
        self.assertIn(league, self.db.leagues)


    def test_remove_league(self):
        league = League(1, "League 1")
        self.db.add_league(league)
        self.assertIn(league, self.db.leagues)
        self.db.remove_league(league)
        self.assertNotIn(league, self.db.leagues)


    def test_league_named(self):
        league = League(1, "League 1")
        self.db.add_league(league)
        self.assertIs(self.db.league_named("League 1"), league)
        self.assertIsNone(self.db.league_named("missing"))


    def test_save_and_load(self):
        self.db.add_league(League(1, "League 1"))
        file_path = os.path.join(self.temp, "db.pkl")
        self.db.save(file_path)
        LeagueDatabase._sole_instance = None
        LeagueDatabase.load(file_path)
        names = []
        for league in LeagueDatabase.instance().leagues:
            names.append(league.name)
        self.assertIn("League 1", names)


    def test_import_league_teams(self):
        file_path = os.path.join(self.temp, "teams.csv")
        with open(file_path, "w", encoding="utf-8", newline="") as f:
            f.write("Team name,Member name,Member email\n")
            f.write("Team 1,Jay,jay@gmail.com\n")
            f.write("Team 1,Gary,gary@gmail.com\n")
            f.write("Team 2,Emily,emily@gmail.com\n")
        league = League(self.db.next_oid(), "League 1")
        self.db.add_league(league)
        self.db.import_league_teams(league, file_path)
        self.assertEqual(len(league.teams), 2)
        total_members = 0
        for team in league.teams:
            total_members += len(team.members)
        self.assertEqual(total_members, 3)


    def test_export_league_teams(self):
        league = League(self.db.next_oid(), "League 1")
        self.db.add_league(league)
        file_in = os.path.join(self.temp, "in.csv")
        with open(file_in, "w", encoding="utf-8", newline="") as f:
            f.write("Team name,Member name,Member email\n")
            f.write("Team 1,Jay,jay@gmail.com\n")
        self.db.import_league_teams(league, file_in)
        file_out = os.path.join(self.temp, "out.csv")
        self.db.export_league_teams(league, file_out)

        lines = []
        with open(file_out, "r", encoding="utf-8", newline="") as f:
            for line in f:
                lines.append(line.rstrip())
        self.assertEqual(lines[0], "Team name,Member name,Member email")
        self.assertEqual(lines[1], "Team 1,Jay,jay@gmail.com")



if __name__ == "__main__":
    unittest.main()