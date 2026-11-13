from harmony import Step, ResultPacket
from pathlib import Path


class SaveResult(Step):
    def run(self, save_path: Path, result_packet: ResultPacket):
        pass
