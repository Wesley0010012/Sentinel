from abc import ABC, abstractmethod
from ..entities.schema import Schema

class SchemaTester(ABC):
    def test(schema: Schema) -> bool:
        pass