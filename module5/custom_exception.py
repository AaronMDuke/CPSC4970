class DuplicateOid(Exception):
    def __init__(self, oid):
        self.oid = oid
        super().__init__("Duplicate oid: " + str(oid))



class DuplicateEmail(Exception):
    def __init__(self, email):
        self.email = email
        super().__init__("Duplicate email: " + str(email))