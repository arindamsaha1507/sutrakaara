"""Module to represent a Taddhita Pratyaya"""

from dataclasses import dataclass, field

from utils import Khanda, KhandaType


@dataclass
class Taddhita(Khanda):
    """Class to represent a Taddhita Pratyaya"""

    moola: str = field(default=None)
    mukhya: Khanda = field(default=None)
    uchchaarana: list = field(default_factory=list)

    def __post_init__(self):
        self.typ.append(KhandaType.TADDHITA)
        self.typ.append(KhandaType.PRATYAAYA)
        self.roopa = self.moola
        self.upadesha = self.moola

    def __repr__(self) -> str:
        # pylint: disable=useless-super-delegation
        return super().__repr__()
