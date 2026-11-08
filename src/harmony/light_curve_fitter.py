from abc import ABC, abstractmethod
from harmony import DataPacket, ResultPacket


class LightCurveFitter(ABC):

    @abstractmethod
    def __init__(self, data_packet: DataPacket):  # Add model specific settings as args here
        pass

    @abstractmethod
    def fit(self) -> ResultPacket:
        pass
