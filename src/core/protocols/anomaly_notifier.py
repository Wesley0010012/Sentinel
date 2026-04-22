from abc import ABC, abstractmethod
from ..entities.schema import Schema

class AnomalyNotifier(ABC):
    @abstractmethod
    def notify_schema_not_found(self, schema_signature: str) -> None:
        pass

    @abstractmethod
    def notify_schema_anomaly(self, schema: Schema) -> None:
        pass