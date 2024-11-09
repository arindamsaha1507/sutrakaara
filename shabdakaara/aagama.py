"""Module to represent an Aagama"""

from dataclasses import dataclass, field

from utils import Khanda, KhandaType

@dataclass
class Aagama(Khanda):
    """Class to represent an Aagama"""

    moola: str = field(default=None)
    uchchaarana: list = field(default_factory=list)
    mukhya: Khanda = field(default=None)

    def __post_init__(self):
        self.typ.append(KhandaType.AAGAMA)
        self.roopa = self.moola

    def __repr__(self) -> str:
        # pylint: disable=useless-super-delegation
        return super().__repr__()
