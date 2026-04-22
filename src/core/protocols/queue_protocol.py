from abc import ABC, abstractmethod

class QueueProtocol(ABC):
    @abstractmethod
    def consume(self) -> dict | None:
        pass