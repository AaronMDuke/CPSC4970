from module5.identified_object import IdentifiedObject


class Competition(IdentifiedObject):
    def __init__(self, oid, teams, location, date_time):
        super().__init__(oid)
        self._teams_competing = list(teams)
        self.location = location
        self.date_time = date_time

    @property
    def teams_competing(self):
        return self._teams_competing

    def send_email(self, emailer, subject, message):
        seen = set()
        recipients = []
        for team in self._teams_competing:
            for member in team.members:
                if member.email is not None and member not in seen:
                    seen.add(member)
                    recipients.append(member.email)
        emailer.send_plain_email(recipients, subject, message)

    def __str__(self):
        dt_str = f" on {self.date_time.strftime('%m/%d/%Y %H:%M')}" if self.date_time else ""
        teams_str = " vs. ".join(t.name for t in self._teams_competing)
        return f"Competition at {self.location}{dt_str} with {teams_str}"