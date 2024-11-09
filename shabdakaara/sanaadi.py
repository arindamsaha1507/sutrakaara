"""Module to represent a Sanaadi Pratyaya"""

from dataclasses import dataclass, field

from utils import Khanda, KhandaType


@dataclass
class Sanaadi(Khanda):
    """Class to represent a Krt Pratyaya"""

    moola: str = field(default=None)
    mukhya: Khanda = field(default=None)
    uchchaarana: list = field(default_factory=list)

    def __post_init__(self):
        self.typ.append(KhandaType.SANAADI)
        self.typ.append(KhandaType.PRATYAAYA)
        self.roopa = self.moola

    def __repr__(self) -> str:
        # pylint: disable=useless-super-delegation
        return super().__repr__()
