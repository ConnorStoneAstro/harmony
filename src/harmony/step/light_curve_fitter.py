from abc import abstractmethod
from harmony import DataPacket, ResultPacket, Step


class LightCurveFitter(Step):
    @abstractmethod
    def run(
        self, data_packet: DataPacket
    ) -> ResultPacket:  # Add model specific settings as args here
        pass
