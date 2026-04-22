from abc import ABC, abstractmethod
from ..entities.schema import Schema
from .schema_tester import SchemaTester

class SchemaTesterFactory(ABC):
    def build(self, schema: Schema) -> SchemaTester:
        pass