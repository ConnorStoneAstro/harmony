from abc import ABC, abstractmethod
from harmony import Packet


class Step(ABC):
    @abstractmethod
    def run(self) -> Packet:
        pass
