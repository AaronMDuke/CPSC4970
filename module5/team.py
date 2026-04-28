from module5.identified_object import IdentifiedObject
from module5.custom_exception import DuplicateOid, DuplicateEmail


class Team(IdentifiedObject):
    def __init__(self, oid, name):
        super().__init__(oid)
        self.name = name
        self._members = []

    @property
    def members(self):
        return self._members

    def add_member(self, member):
        for existing in self._members:
            if existing.oid == member.oid:
                raise DuplicateOid(member.oid)
            if existing.email is not None and member.email is not None:
                if existing.email.lower() == member.email.lower():
                    raise DuplicateEmail(member.email)
        self._members.append(member)

    def member_named(self, s):
        for member in self._members:
            if member.name == s:
                return member
        return None

    def remove_member(self, member):
        if member in self._members:
            self._members.remove(member)

    def send_email(self, emailer, subject, message):
        recipients = [m.email for m in self._members if m.email is not None]
        emailer.send_plain_email(recipients, subject, message)

    def __str__(self):
        return f"{self.name}: {len(self._members)} members"