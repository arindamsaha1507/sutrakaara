"""Sutras for Adhyaaya 3"""

from dataclasses import dataclass

from utils import Prakriya, Sutra, KhandaType, Taddhitaartha
from sutra.sutra_list import SutraUtils

# from vinyaasa import get_vinyaasa

from sup import Sup
from taddhita import Taddhita
from vinyaasa import get_vinyaasa


@dataclass
class SutraFourOneTwo(Sutra):
    """स्वौजसमौट्छष्टाभ्याम्भिस्ङेभ्याम्भ्यस्ङसिभ्याम्भ्यस्ङसोसाङ्ङ्योस्सुप् ४.१.२"""

    def __post_init__(self):
        self.define("स्वौजसमौट्छष्टाभ्याम्भिस्ङेभ्याम्भ्यस्ङसिभ्याम्भ्यस्ङसोसाङ्ङ्योस्सुप् ४.१.२")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = [
            khanda
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.PRAATIPADIKA in khanda.typ
            and KhandaType.PADA not in khanda.typ
        ]

        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        return True

    def apply(self, prakriya: Prakriya, vibhakti: int, vachana: int):
        # pylint: disable=arguments-differ

        vibhakti -= 1
        vachana -= 1

        number = vibhakti * 3 + vachana

        khanda = [
            khanda
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.PRAATIPADIKA in khanda.typ
            and KhandaType.PADA not in khanda.typ
        ][0]

        khanda_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.PRAATIPADIKA in khanda.typ
            and KhandaType.PADA not in khanda.typ
        ][0]

        sup = Sup(index=number, mukhya=khanda)

        prakriya.vartamaana_sthiti.insert(khanda_index + 1, sup)
        khanda.typ.append(KhandaType.PADA)

        self.push(prakriya, prakriya.vartamaana_sthiti, "सुब्विधानम्")

    def call(self, praakriya: Prakriya, vibhakti: int, vachana: int):
        """Call the Sutra"""
        if self.check(praakriya):
            self.apply(praakriya, vibhakti, vachana)


@dataclass
class SutraFourOneEightyThree(Sutra):
    """प्राग्दीव्यतोऽण् ४.१.८३"""

    def __post_init__(self):
        self.define("प्राग्दीव्यतोऽण् ४.१.८३")

    @staticmethod
    def check(prakriya: Prakriya, artha: Taddhitaartha, pratyaya: str):
        # pylint: disable=arguments-differ

        if pratyaya != "अण्":
            return False

        allowed_arthas = [
            Taddhitaartha.TASYA_APATYAM,
            Taddhitaartha.TASYA_IDAM,
        ]

        if artha not in allowed_arthas:
            return False

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.PRAATIPADIKA)
        if not khanda:
            return False

        khanda = khanda[-1][1]
        vinyaasa = get_vinyaasa(khanda.roopa)

        if vinyaasa[-1] == "अ" and artha == Taddhitaartha.TASYA_APATYAM:
            return False

        return True

    def apply(self, prakriya: Prakriya, artha: Taddhitaartha, pratyaya: str):
        # pylint: disable=arguments-differ

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.PRAATIPADIKA)[-1][1]
        khanda_index = SutraUtils.get_khanda(prakriya, KhandaType.PRAATIPADIKA)[-1][0]

        taddhita = Taddhita(moola=pratyaya, mukhya=khanda)
        prakriya.vartamaana_sthiti.insert(khanda_index + 2, taddhita)

        artha = " ".join(artha.value.split(" ")[:-2])

        self.push(
            prakriya,
            prakriya.vartamaana_sthiti,
            f"{artha} इत्यर्थे {pratyaya} प्रत्ययः",
        )

    def call(self, praakriya: Prakriya, pratyaya: str, artha: Taddhitaartha):
        """Call the Sutra"""
        if self.check(praakriya, artha, pratyaya):
            self.apply(praakriya, artha, pratyaya)


@dataclass
class SutraFourOneNinetyFive(Sutra):
    """अत इञ् ४.१.९५"""

    def __post_init__(self):
        self.define("अत इञ् ४.१.९५")

    @staticmethod
    def check(prakriya: Prakriya, artha: Taddhitaartha, pratyaya: str):
        # pylint: disable=arguments-differ

        if pratyaya != "इञ्":
            return False

        if artha != Taddhitaartha.TASYA_APATYAM:
            return False

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.PRAATIPADIKA)
        if not khanda:
            print("No Khanda")
            return False

        khanda = khanda[-1][1]
        vinyaasa = get_vinyaasa(khanda.roopa)

        if vinyaasa[-1] != "अ":
            return False

        return True

    def apply(self, prakriya: Prakriya, artha: Taddhitaartha, pratyaya: str):
        # pylint: disable=arguments-differ

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.PRAATIPADIKA)[-1][1]
        khanda_index = SutraUtils.get_khanda(prakriya, KhandaType.PRAATIPADIKA)[-1][0]

        taddhita = Taddhita(moola=pratyaya, mukhya=khanda)
        prakriya.vartamaana_sthiti.insert(khanda_index + 2, taddhita)

        artha = " ".join(artha.value.split(" ")[:-2])

        self.push(
            prakriya,
            prakriya.vartamaana_sthiti,
            f"{artha} इत्यर्थे {pratyaya} प्रत्ययः",
        )

    def call(self, praakriya: Prakriya, pratyaya: str, artha: Taddhitaartha):
        """Call the Sutra"""
        if self.check(praakriya, artha, pratyaya):
            self.apply(praakriya, artha, pratyaya)
