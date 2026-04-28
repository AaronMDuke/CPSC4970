import unittest
from module5.team import Team
from module5.team_member import TeamMember
from module5.custom_exception import DuplicateOid, DuplicateEmail


class TeamTest(unittest.TestCase):
    def test_str(self):
        t = Team(1, "Blue Team")
        t.add_member(TeamMember(1, "Bob", "bob@gmail.com"))
        t.add_member(TeamMember(2, "Cole", "cole@gmail.com"))
        self.assertEqual("Blue Team: 2 members", str(t) )

    def duplicate_members_test(self):
        t = Team(1, "Blue Team")
        tm = TeamMember(1, "Bob", "bob@gmail.com")
        t.add_member(tm)
        t.add_member(tm)
        self.assertEqual(1, len(t.members))

    def test_add_member(self):
        t = Team(1, "Ballers")
        tm = TeamMember(1, "Bob", "bob@gmail.com")
        t.add_member(tm)
        self.assertIn(tm, t.members)

    def test_duplicate_oid(self):
        t = Team(1, "Ballers")
        t.add_member(TeamMember(1, "Jack", "jack@gmail.com"))
        with self.assertRaises(DuplicateOid):
            t.add_member(TeamMember(1, "Jackie", "jackie@gmail.com"))

    def test_duplicate_email(self):
        t = Team(1, "Ballers")
        t.add_member(TeamMember(1, "Gary", "gary@gmail.com"))
        with self.assertRaises(DuplicateEmail):
            t.add_member(TeamMember(2, "Jeff", "gary@gmail.com"))

    def test_case_insensitive_email(self):
        t = Team(1, "Ballers")
        t.add_member(TeamMember(1, "John", "john@gmail.com"))
        with self.assertRaises(DuplicateEmail):
            t.add_member(TeamMember(2, "John", "JOHN@GMAIL.COM"))



    if __name__ == "__main__":
        unittest.main()