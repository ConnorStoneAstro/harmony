from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Packet:

    packet_key: str

    def save(self, filepath: Path):
        # FIXME
        pass

    @classmethod
    def load(cls, filepath: Path) -> "Packet":
        # FIXME
        pass
