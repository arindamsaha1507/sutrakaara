"""Module to represent an Upasarga"""

from dataclasses import dataclass, field

from utils import Khanda, KhandaType


@dataclass
class Upasarga(Khanda):
    """Class to represent an Upasarga"""

    moola: str = field(default=None)
    mukhya: Khanda = field(default=None)

    def __post_init__(self):
        self.typ.append(KhandaType.UPASARGA)
        self.typ.append(KhandaType.PRAADI)
        self.typ.append(KhandaType.GANAPAATHA)
        self.roopa = self.moola

        if self.roopa != "आङ्":
            self.aupadeshika = False

    def __repr__(self) -> str:
        # pylint: disable=useless-super-delegation
        return super().__repr__()
