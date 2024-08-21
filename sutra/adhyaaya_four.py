"""Sutras for Adhyaaya 3"""

from dataclasses import dataclass

from utils import Prakriya, Sutra, KhandaType, Taddhitaartha
from sutra.sutra_list import SutraUtils
# from vinyaasa import get_vinyaasa

from taddhita import Taddhita


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

        return True

    def apply(self, prakriya: Prakriya, artha: Taddhitaartha, pratyaya: str):
        # pylint: disable=arguments-differ

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.PRAATIPADIKA)[-1][1]
        khanda_index = SutraUtils.get_khanda(prakriya, KhandaType.PRAATIPADIKA)[-1][0]

        taddhita = Taddhita(moola=pratyaya, mukhya=khanda)
        prakriya.vartamaana_sthiti.insert(khanda_index + 1, taddhita)

        self.push(
            prakriya,
            prakriya.vartamaana_sthiti,
            f"{artha.value} इत्यर्थे {pratyaya} प्रत्ययः",
        )

    def call(self, praakriya: Prakriya, pratyaya: str, artha: Taddhitaartha):
        """Call the Sutra"""
        if self.check(praakriya, artha, pratyaya):
            self.apply(praakriya, artha, pratyaya)
