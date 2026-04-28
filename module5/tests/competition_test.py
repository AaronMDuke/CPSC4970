import datetime
import unittest
from module5.competition import Competition
from module5.team import Team
from module5.team_member import TeamMember

class CompetitionTest(unittest.TestCase):
    def test_str_no_date(self):
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        c = Competition(1,[t1, t2], "Here", None)
        self.assertEqual("Competition at Here with Team 1 vs. Team 2", str(c))

    def test_str_with_date(self):
        dt = datetime.datetime(2015, 5, 15, 10, 30)
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        c = Competition(1, [t1, t2], "Here", dt)
        self.assertEqual("Competition at Here on 05/15/2015 10:30 with Team 1 vs. Team 2", str(c))


    if __name__ == "__main__":
        unittest.main()