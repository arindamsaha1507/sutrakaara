"""Module to define the classes for the Prakriya and Khanda"""

from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from enum import Enum

from varna import vyanjana, sankhyaa
from vinyaasa import get_shabda, get_vinyaasa


class KhandaType(Enum):
    """Enum to represent the type of Khanda"""

    DHAATU = "धातु"
    PRATYAAYA = "प्रत्यय"
    AAGAMA = "आगम"
    NIPAATA = "निपात"
    SVARAADI = "स्वरादि"
    AVYAYA = "अव्यय"
    GANAPAATHA = "गणपाठ"
    UPASARGA = "उपसर्ग"
    PRAADI = "प्रादि"
    PRAATIPADIKA = "प्रातिपदिक"
    PRATYAYA = "प्रत्यय"
    SUP = "सुप्"
    TIN = "तिङ्"
    PADA = "पद"
    SUBANTA = "सुबन्त"
    TINGANTA = "तिङन्त"
    KRT = "कृत्"
    TADDHITA = "तद्धित"
    KRIDANTA = "कृदन्त"
    TADDHITAANTA = "तद्धितान्त"


SUP = [
    "सुँ",
    "औ",
    "जस्",
    "अम्",
    "औट्",
    "शस्",
    "टा",
    "भ्याम्",
    "भिस्",
    "ङॆ",
    "भ्याम्",
    "भ्यस्",
    "ङसिँ",
    "भ्याम्",
    "भ्यस्",
    "ङस्",
    "ओस्",
    "आम्",
    "ङि",
    "ओस्",
    "सुप्",
]


class Krdartha(Enum):
    """Enum to represent the Krdartha"""

    KRTYA = "कृत्य"
    NVULAADI = "ण्वुलादि"
    ANAADI = "अणादि"
    BHOOTA = "भूत"
    VARTAMAANA = "वर्तमान"
    TAACHCHHILA = "ताच्छिल"
    BHAVISHYAT = "भविष्यत्"
    BHAAVA = "भाव"
    STRI = "स्त्री"
    KARANAADHIKARANA = "करणाधिकरण"
    KHALAADI = "खलादि"
    DHAATUSAMBANDHI = "धातुसम्बन्धी"


@dataclass
class Khanda(ABC):
    """Abstract base class for Khanda"""

    typ: list[KhandaType] = field(default_factory=list, init=False)
    roopa: str = field(default=None)
    it: list = field(default_factory=list)
    aupadeshika: bool = field(default=True)
    upadesha: str = field(init=False)
    uchchaarana: list[int] = field(default_factory=list)

    @abstractmethod
    def __post_init__(self):
        pass

    def __repr__(self) -> str:
        return self.roopa

    def remove_uchchaarana(self):
        """Remove the Uchchaarana from the Khanda"""

        varnas = get_vinyaasa(self.roopa)
        for inx in self.uchchaarana:
            varnas.pop(inx)
        self.roopa = get_shabda(varnas)


@dataclass
class Prakriya:
    """Class to represent a Prakriya"""

    sthiti: list[str] = field(default_factory=list, init=False)
    sutra: list[str] = field(default_factory=list, init=False)
    tippani: list[str] = field(default_factory=list, init=False)
    vartamaana_sthiti: list[Khanda] = field(default=None, init=False)
    final: str = field(default=None, init=False)

    @property
    def length(self):
        """Return the length of the Prakriya"""

        if len(self.sthiti) != len(self.sutra) or len(self.sthiti) != len(self.tippani):
            raise ValueError("The lengths of the Prakriya lists do not match")

        return len(self.sthiti)

    @property
    def string(self):
        """Return the vartamaana sthiti as a string"""

        ss = " ".join([str(khanda) for khanda in self.vartamaana_sthiti])
        return get_vinyaasa(ss)

    def replace_index(self, index: int, replacement: str):
        """Replace the letter at the given index with the replacement"""

        total_length = 0
        required_khanda = None

        for khanda in self.vartamaana_sthiti:
            vinyaasa = get_vinyaasa(khanda.roopa)
            if index < total_length + len(vinyaasa):
                reduced_index = index - total_length
                required_khanda = khanda
                break
            total_length += len(vinyaasa) + 1

        if reduced_index >= len(vinyaasa):
            raise ValueError("Invalid index")

        vinyaasa[reduced_index] = replacement
        required_khanda.roopa = get_shabda(vinyaasa)

    def insert_index(self, index: int, replacement: str):
        """Insert the letter at the given index with the replacement"""

        total_length = 0
        required_khanda = None

        for khanda in self.vartamaana_sthiti:
            vinyaasa = get_vinyaasa(khanda.roopa)
            if index < total_length + len(vinyaasa):
                reduced_index = index - total_length
                required_khanda = khanda
                break
            total_length += len(vinyaasa) + 1

        if reduced_index >= len(vinyaasa):
            raise ValueError("Invalid index")

        vinyaasa.insert(reduced_index, replacement)
        required_khanda.roopa = get_shabda(vinyaasa)

    def delete_index(self, index: int):
        """Delete the letter at the given index with the replacement"""

        total_length = 0
        required_khanda = None

        for khanda in self.vartamaana_sthiti:
            vinyaasa = get_vinyaasa(khanda.roopa)
            if index < total_length + len(vinyaasa):
                reduced_index = index - total_length
                required_khanda = khanda
                break
            total_length += len(vinyaasa) + 1

        if reduced_index >= len(vinyaasa):
            raise ValueError("Invalid index")

        vinyaasa.pop(reduced_index)
        required_khanda.roopa = get_shabda(vinyaasa)

    def combine(self):
        """Combine the Vartamaana Sthiti to form the final string"""

        vinyaasa = []

        for khanda in self.vartamaana_sthiti:
            vv = get_vinyaasa(khanda.roopa)
            while " " in vv:
                vv.remove(" ")
            vinyaasa.extend(vv)

        self.final = get_shabda(vinyaasa)

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


@dataclass
class Sutra(ABC):
    """Abstract base class for Sutras"""

    sutra: str = field(init=False)
    adhyaaya: int = field(init=False)
    paada: int = field(init=False)
    kramaanka: int = field(init=False)

    def define(self, line: str):
        """Define the Sutra"""

        def convert_sanskrit_to_int(sanskrit_numeral: str) -> int:
            num_str = "".join(str(sankhyaa.index(char)) for char in sanskrit_numeral)
            return int(num_str)

        parts = line.split(" ")
        self.sutra = " ".join(parts[:-1])

        numbers = parts[-1].split(".")

        if len(numbers) != 3:
            raise ValueError("Invalid Sutra number")

        self.adhyaaya = convert_sanskrit_to_int(numbers[0])
        self.paada = convert_sanskrit_to_int(numbers[1])
        self.kramaanka = convert_sanskrit_to_int(numbers[2])

        if self.adhyaaya < 1 or self.paada < 1 or self.kramaanka < 1:
            raise ValueError("Invalid Sutra number")

        if self.paada > 4:
            raise ValueError("Invalid Paada number")

        if self.adhyaaya > 8:
            raise ValueError("Invalid Adhyaaya number")

    def describe(self) -> str:
        """Return the Sutra number in the format 'Adhyaaya.Paada.Kramaanka'"""

        return f"{self.sutra} {self.adhyaaya}.{self.paada}.{self.kramaanka}"

    def __call__(self, praakriya: Prakriya):
        if self.check(praakriya):
            self.apply(praakriya)

    def push(self, praakriya: Prakriya, sthiti: list[Khanda], message: str):
        """Push the new state to the Prakriya"""

        praakriya.add_to_prakriya(sthiti, self.describe(), message)

    @staticmethod
    @abstractmethod
    def check(prakriya: Prakriya):
        """Check if the Sutra can be applied to the Prakriya"""

    @abstractmethod
    def apply(self, prakriya: Prakriya):
        """Apply the Sutra to the Prakriya"""

@dataclass
class Unaadi(ABC):
    """Abstract base class for Sutras"""

    sutra: str = field(init=False)
    paada: int = field(init=False)
    kramaanka: int = field(init=False)

    def define(self, line: str):
        """Define the Sutra"""

        def convert_sanskrit_to_int(sanskrit_numeral: str) -> int:
            num_str = "".join(str(sankhyaa.index(char)) for char in sanskrit_numeral)
            return int(num_str)

        parts = line.split(" ")
        self.sutra = " ".join(parts[:-1])

        numbers = parts[-1].split(".")

        if len(numbers) != 2:
            raise ValueError("Invalid Sutra number")

        self.paada = convert_sanskrit_to_int(numbers[0])
        self.kramaanka = convert_sanskrit_to_int(numbers[1])

        if self.paada < 1 or self.kramaanka < 1:
            raise ValueError("Invalid Sutra number")

        if self.paada > 5:
            raise ValueError("Invalid Paada number")

    def describe(self) -> str:
        """Return the Sutra number in the format 'Adhyaaya.Paada.Kramaanka'"""

        return f"{self.sutra} {self.paada}.{self.kramaanka}"

    def __call__(self, praakriya: Prakriya):
        if self.check(praakriya):
            self.apply(praakriya)

    def push(self, praakriya: Prakriya, sthiti: list[Khanda], message: str):
        """Push the new state to the Prakriya"""

        praakriya.add_to_prakriya(sthiti, self.describe(), message)

    @staticmethod
    @abstractmethod
    def check(prakriya: Prakriya):
        """Check if the Sutra can be applied to the Prakriya"""

    @abstractmethod
    def apply(self, prakriya: Prakriya):
        """Apply the Sutra to the Prakriya"""


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
