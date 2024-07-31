"""Module to define the classes for the Prakriya and Khanda"""

from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from enum import Enum

class KhandaType(Enum):
    """Enum to represent the type of Khanda"""

    DHAATU = "धातु"
    PRATYAAYA = "प्रत्यय"


@dataclass
class Khanda(ABC):
    """Abstract base class for Khanda"""

    typ: list[KhandaType] = field(default_factory=list, init=False)
    roopa: str = field(default=None)
    it: list = field(default_factory=list)
    aupadeshika: bool = field(default=True)

    @abstractmethod
    def __post_init__(self):
        pass

    def __repr__(self) -> str:
        return self.roopa


@dataclass
class Prakriya:
    """Class to represent a Prakriya"""

    sthiti: list[str] = field(default_factory=list, init=False)
    sutra: list[str] = field(default_factory=list, init=False)
    tippani: list[str] = field(default_factory=list, init=False)
    vartamaana_sthiti: list[Khanda] = field(default=None, init=False)

    # @property
    # def roopa(self):
    #     """Return the Dhatus in the Prakriya"""

    #     tt = []
    #     for line in self.sthiti:
    #         ss = " ".join([str(khanda) for khanda in line])
    #         tt.append(ss)

    #     return tt

    # @property
    # def vartamaana_sthiti(self):
    #     """Return the current state of the Prakriya"""

    #     return self.sthiti[-1]

    @property
    def length(self):
        """Return the length of the Prakriya"""

        if len(self.sthiti) != len(self.sutra) or len(self.sthiti) != len(self.tippani):
            raise ValueError("The lengths of the Prakriya lists do not match")

        return len(self.sthiti)

    def __repr__(self) -> str:

        ss = "\n".join(
            [
                f"{ii} : {jj} : {kk}"
                for ii, jj, kk in zip(self.sthiti, self.sutra, self.tippani)
            ]
        )
        return ss

    def add_to_prakriya(self, sthiti: list[Khanda], sutra: str, tippani: str):
        """Add a Khanda to the Prakriya"""

        self.vartamaana_sthiti = sthiti

        string_sthiti = " ".join([str(khanda) for khanda in sthiti])
        self.sthiti.append(string_sthiti)
        self.sutra.append(sutra)
        self.tippani.append(tippani)

        # self.sthiti.append(copy.deepcopy(khanda))
        # self.sutra.append(sutra)
        # self.tippani.append(tippani)

        print(self)
