"""Module to create Dhaatu objects from a list of Dhatus"""

# pylint: disable=non-ascii-module-import

from dataclasses import dataclass, field

from utils import Khanda, Prakriya, KhandaType
from it_prakarana import ItSanjna, DhaatuSanjna
from praakrita_kaarya import PraatritaKaaraya


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


@dataclass(kw_only=True)
class Dhaatu(Khanda):
    """Class to represent a Dhaatu"""

    # pylint: disable=too-many-instance-attributes

    moola: str = field(default=None)
    kramaanka: str = field(init=False)
    gana: str = field(init=False)
    upadesha: str = field(init=False)
    artha: str = field(init=False)
    dhaatu: str = field(init=False)
    pada: str = field(init=False)
    idaagama: str = field(init=False)
    anudaatta_it: bool = field(default=False)
    svarita_it: bool = field(default=False)
    anudaatta_svara: bool = field(init=False, default=False)

    def __post_init__(self):
        self.typ.append(KhandaType.DHAATU)
        self.kramaanka = self.moola.split(" ", maxsplit=1)[0]
        self.upadesha = self.moola.split(" ")[1]
        self.artha = " ".join(self.moola.split(" ")[2:])
        self.gana = GANAS[self.kramaanka.split(".")[0]]

        self.roopa = self.upadesha

    def __repr__(self) -> str:
        # pylint: disable=useless-super-delegation
        return super().__repr__()

    def add_dhaatu(self, prakriya: Prakriya):
        """Add the Dhaatu to the Prakriya"""

        if prakriya.length > 0:
            raise ValueError("The Prakriya is not empty")

        DhaatuSanjna(prakriya, self)

    def identify_it(self, prakriya: Prakriya):
        """Identify the It of the Dhaatu"""

        ItSanjna(prakriya=prakriya)
        PraatritaKaaraya(prakriya)