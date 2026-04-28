class IdentifiedObject:
    def __init__(self, oid):
        self._oid = oid

    @property
    def oid(self):
        return self._oid

    def __eq__(self, other):
        return type(self) == type(other) and self._oid == other._oid

    def __hash__(self):
        return hash(self._oid)