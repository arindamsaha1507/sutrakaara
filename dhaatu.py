"""Module to create Dhaatu objects from a list of Dhatus"""

# pylint: disable=non-ascii-module-import

from dataclasses import dataclass, field
from enum import Enum

from utils import Khanda, KhandaType


GANAS = {
    "१": "भ्वादि",
    "२": "अदादि",
    "३": "जुहोत्यादि",
    "४": "दिवादि",
    "५": "स्वादि",
    "६": "तुदादि",
    "७": "रुधादि",
    "८": "तनादि",
    "९": "क्र्यादि",
    "१०": "चुरादि",
}


class Gana(Enum):
    """Enum to represent the Ganas"""

    BHVAADI = "भ्वादि"
    ADAADI = "अदादि"
    JUHOTYAADI = "जुहोत्यादि"
    DIVAADI = "दिवादि"
    SWAADI = "स्वादि"
    TUDAADI = "तुदादि"
    RUDHAADI = "रुधादि"
    TANAADI = "तनादि"
    KRYAADI = "क्र्यादि"
    CHURAADI = "चुरादि"

    YAJAADI = "यजादि"


def devanagari_to_integers(devanagari_str):
    """Convert a Devanagari string to integers"""

    # Dictionary to map Devanagari digits to Arabic digits
    devanagari_to_arabic = {
        "०": "0",
        "१": "1",
        "२": "2",
        "३": "3",
        "४": "4",
        "५": "5",
        "६": "6",
        "७": "7",
        "८": "8",
        "९": "9",
    }

    # Convert Devanagari string to Arabic numerals
    arabic_str = "".join(
        devanagari_to_arabic[char] if char in devanagari_to_arabic else char
        for char in devanagari_str
    )

    return int(arabic_str)


@dataclass(kw_only=True)
class Dhaatu(Khanda):
    """Class to represent a Dhaatu"""

    # pylint: disable=too-many-instance-attributes

    moola: str = field(default=None)
    kramaanka: str = field(init=False)
    gana: str = field(init=False)
    artha: str = field(init=False)
    dhaatu: str = field(init=False)
    pada: str = field(init=False)
    idaagama: str = field(init=False)
    anudaatta_it: bool = field(default=False)
    svarita_it: bool = field(default=False)
    anudaatta_svara: bool = field(init=False, default=False)
    num: int = field(init=False)

    def __post_init__(self):
        self.typ.append(KhandaType.DHAATU)
        self.kramaanka = self.moola.split(" ", maxsplit=1)[0]
        self.upadesha = self.moola.split(" ")[1]
        self.artha = " ".join(self.moola.split(" ")[2:])
        self.gana = Gana(GANAS[self.kramaanka.split(".")[0]])

        self.roopa = self.upadesha
        self.num = devanagari_to_integers(self.kramaanka.split(".")[1])

        self.typ.append(self.gana)

        if self.gana == Gana.BHVAADI:
            if self.num >= 1157 and self.num <= 1165:
                self.typ.append(Gana.YAJAADI)

    def __repr__(self) -> str:
        # pylint: disable=useless-super-delegation
        return super().__repr__()
