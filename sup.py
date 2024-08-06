"""Sup Pratyaya"""

from dataclasses import dataclass, field

from utils import Khanda, KhandaType, SUP


@dataclass
class Sup(Khanda):
    """Class to represent a sup pratyaya"""

    index: int = field(default=None)
    mukhya: Khanda = field(default=None)
    moola: str = field(default=None, init=False)

    def __post_init__(self):

        self.moola = SUP[self.index]
        self.roopa = self.moola

        self.typ.append(KhandaType.PRATYAYA)
        self.typ.append(KhandaType.SUP)

    @property
    def vibhakti(self):
        """Return the vibhakti of the Sup Pratyaya"""
        return self.index // 3 + 1

    @property
    def vachana(self):
        """Return the vachana of the Sup Pratyaya"""
        return self.index % 3 + 1

    def __repr__(self) -> str:
        # pylint: disable=useless-super-delegation
        return super().__repr__()
