"""Sutras for Adhyaaya 8"""

from dataclasses import dataclass

from utils import KhandaType, Prakriya, Sutra

from sutra.sutra_list import SutraUtils

from taddhita import Taddhita


@dataclass
class SutraFiveFourNinetyTwo(Sutra):
    """गोरतद्धितलुकि ५.४.९२"""

    def __post_init__(self):
        self.define("गोरतद्धितलुकि ५.४.९२")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = SutraUtils.get_khanda(prakriya, KhandaType.PRAATIPADIKA)
        if not khanda:
            return False
        if len(khanda) != 2:
            return False
        khanda = khanda[1][1]

        if khanda.roopa != "गो":
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.PRAATIPADIKA)
        khanda_index = khanda[1][0]
        khanda = khanda[1][1]

        pratyaya = Taddhita(moola="ट्च्", mukhya=khanda)

        prakriya.vartamaana_sthiti.append((khanda_index + 1, pratyaya))

        self.push(prakriya, prakriya.vartamaana_sthiti, "समासान्ते टच्")
