"""Sutras for Adhyaaya 2"""

from dataclasses import dataclass

from utils import Prakriya, Sutra, KhandaType
from sutra.sutra_list import SutraUtils


@dataclass
class SutraTwoFourSeventyOne(Sutra):
    """सुपो धातुप्रातिपदिकयोः २.४.७१"""

    def __post_init__(self):
        self.define("सुपो धातुप्रातिपदिकयोः २.४.७१")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.SUP)

        if not khanda:
            return False

        khanda_index = khanda[-1][0]

        if khanda_index == len(prakriya.vartamaana_sthiti) - 1:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        remove_list = [False for _ in prakriya.vartamaana_sthiti]

        for idx, khanda in enumerate(prakriya.vartamaana_sthiti):
            if KhandaType.SUP in khanda.typ:
                remove_list[idx] = True

        prakriya.vartamaana_sthiti = [
            khanda
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if not remove_list[idx]
        ]

        self.push(prakriya, prakriya.vartamaana_sthiti, "सुपो धातुप्रातिपदिकयोः")


@dataclass
class SutraTwoFourEightyTwo(Sutra):
    """अव्ययादाप्सुपः २.४.८२"""

    def __post_init__(self):
        self.define("अव्ययादाप्सुपः २.४.८२")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.AVYAYA in khanda.typ
        ]

        if not khanda:
            return False

        khanda = khanda[-1]

        khanda_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.AVYAYA in khanda.typ
        ][-1]

        if KhandaType.SUP not in prakriya.vartamaana_sthiti[khanda_index + 1].typ:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.AVYAYA in khanda.typ
        ][-1]

        prakriya.vartamaana_sthiti.pop(khanda_index + 1)

        self.push(prakriya, prakriya.vartamaana_sthiti, "अव्ययादाप्सुपः")

        # sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        # sthitis[khanda_index + 1].roopa = ""

        # self.push(prakriya, sthitis, "सुब्लुक्")
