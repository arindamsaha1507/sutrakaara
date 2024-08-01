"""Module to define the classes for the Prakriya and Khanda"""

from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from enum import Enum

from varna import vyanjana


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


class UtilFunctions:
    """Class to define the utility functions"""

    @staticmethod
    def get_aupadeshika_khanda(prakriya: Prakriya, return_index: bool = True):
        """Get the Aupadeshika Khanda"""

        aupadeshika_khanda = [
            khanda for khanda in prakriya.vartamaana_sthiti if khanda.aupadeshika
        ]

        if len(aupadeshika_khanda) > 1:
            raise ValueError("Only one Aupadeshika Khanda is allowed")

        if not aupadeshika_khanda:
            return None

        if not return_index:
            return aupadeshika_khanda[0]

        aupadeshika_khanda_index = [
            ii
            for ii, khanda in enumerate(prakriya.vartamaana_sthiti)
            if khanda.aupadeshika
        ]

        return aupadeshika_khanda[0], aupadeshika_khanda_index[0]

    @staticmethod
    def add_dhaatu_it_svaras(dhaatu, indices, vinyaasa):
        """Add the It Svaras to the Dhaatu"""

        for idx in indices.copy():
            if idx + 1 < len(vinyaasa) and vinyaasa[idx + 1] not in vyanjana:
                if vinyaasa[idx + 1] == "॒":
                    dhaatu.anudaatta_it = True
                else:
                    dhaatu.svarita_it = True

                indices.append(idx + 1)

        return indices
