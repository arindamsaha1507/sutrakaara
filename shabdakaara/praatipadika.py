"""Module to represent a Praatipadika"""

from dataclasses import dataclass, field

from utils import Khanda, KhandaType


@dataclass
class Praatipadika(Khanda):
    """Class to represent a Praatipadika"""

    moola: str = field(default=None)

    def __post_init__(self):
        self.typ.append(KhandaType.PRAATIPADIKA)
        self.roopa = self.moola
        self.upadesha = self.moola
        self.aupadeshika = False

    def __repr__(self) -> str:
        # pylint: disable=useless-super-delegation
        return super().__repr__()
 