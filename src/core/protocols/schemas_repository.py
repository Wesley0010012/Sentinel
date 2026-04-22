from abc import ABC, abstractmethod
from ..entities.schema import Schema

class SchemasRepository(ABC):
    @abstractmethod
    def findLatestBySignature(self, signature: str) -> Schema | None:
        pass