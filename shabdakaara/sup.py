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
        self.typ.append(KhandaType.VIBHAKTI)

        if self.vibhakti == 1:
            self.typ.append(KhandaType.PRATHAMAA)
        elif self.vibhakti == 2:
            self.typ.append(KhandaType.DVITIYAA)
        elif self.vibhakti == 3:
            self.typ.append(KhandaType.TRITIYAA)
        elif self.vibhakti == 4:
            self.typ.append(KhandaType.CHATURTHII)
        elif self.vibhakti == 5:
            self.typ.append(KhandaType.PANCHAMII)
        elif self.vibhakti == 6:
            self.typ.append(KhandaType.SHASHTHII)
        elif self.vibhakti == 7:
            self.typ.append(KhandaType.SAPTAMII)
        elif self.vibhakti == 8:
            self.typ.append(KhandaType.SAMBODHANAM)

        if self.vachana == 1:
            self.typ.append(KhandaType.EKAVACHANA)
        elif self.vachana == 2:
            self.typ.append(KhandaType.DVIVACHANA)
        elif self.vachana == 3:
            self.typ.append(KhandaType.BAHUVACHANA)



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
