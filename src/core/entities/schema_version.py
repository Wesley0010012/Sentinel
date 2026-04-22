from datetime import datetime

class SchemaVersion:
    def __init__(self, signature: str, created_at: datetime):
        self._signature = signature
        self._createdAt = created_at

    @property
    def signature(self) -> str:
        return self._signature

    @property
    def created_at(self) -> datetime:
        return self._createdAt