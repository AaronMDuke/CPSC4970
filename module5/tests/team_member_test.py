import unittest
from module5.team_member import TeamMember
from module5.team import Team

class TeamMemberTest(unittest.TestCase):
    def test_str(self):
        tm = TeamMember(1, "Bob", "bob@gmail.com")
        self.assertEqual("Bob<bob@gmail.com>", str(tm))

    def test_name(self):
       tm = TeamMember(1, "Bob", "bob@gmail.com")
       tm.name = "Bobby"
       self.assertEqual("Bobby", tm.name)

    def test_not_equal_types(self):
        tm = TeamMember(1, "Bob", "bob@gmail.com")
        t1 = Team(1, "Bob")
        self.assertNotEqual(tm, t1)

    if __name__ == "__main__":
        unittest.main()
