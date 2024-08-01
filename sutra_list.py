"""All sutras"""

from dataclasses import dataclass
import copy

from utils import Prakriya, UtilFunctions, Sutra, KhandaType, Khanda
from varna import anunaasika_svara, vyanjana
from vinyaasa import get_vinyaasa, get_shabda


@dataclass
class SutraOneThreeOne(Sutra):
    """भूवादयो धातवः १.३.१"""

    def __post_init__(self):
        self.define("भूवादयो धातवः १.३.१")

    @staticmethod
    def check():
        # pylint: disable=arguments-differ
        pass

    def apply(self, prakriya: Prakriya, dhaatu: Khanda):
        # pylint: disable=arguments-differ

        self.push(prakriya, [dhaatu], "धातु-संज्ञा")


@dataclass
class SutraOneThreeTwo(Sutra):
    """उपदेशे अजनुनासिकः इत् १.३.२"""

    def __post_init__(self):
        self.define("उपदेशे अजनुनासिकः इत् १.३.२")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = UtilFunctions.get_aupadeshika_khanda(prakriya, return_index=False)
        if not khanda:
            return False

        vinyaasa = get_vinyaasa(khanda.roopa)

        check = [varna in anunaasika_svara for varna in vinyaasa]

        if not any(check):
            return False

        return True

    def apply(self, prakriya: Prakriya):
        varnas = []
        indices = []

        khanda, khanda_index = UtilFunctions.get_aupadeshika_khanda(prakriya)
        vinyaasa = get_vinyaasa(khanda.roopa)
        temp = [
            (idx, varna)
            for idx, varna in enumerate(vinyaasa)
            if varna in anunaasika_svara
        ]
        indices, varnas = map(list, zip(*temp))
        varnas = [varna[0] for varna in varnas]
        indices = UtilFunctions.add_dhaatu_it_svaras(khanda, indices, vinyaasa)
        khanda.it.extend(varnas)

        tippani = f"{'कार-'.join(varnas)}कार-इत्"
        self.push(prakriya, prakriya.vartamaana_sthiti, tippani)

        SutraOneThreeNine()(prakriya, khanda, khanda_index, indices)


@dataclass
class VartikaOneThreeTwo(Sutra):
    """इर इत्संज्ञा वाच्या (वार्तिक)"""

    def __post_init__(self):
        self.define("इर इत्संज्ञा वाच्या (वार्तिक) १.३.२")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = UtilFunctions.get_aupadeshika_khanda(prakriya, return_index=False)
        if not khanda:
            return False

        if KhandaType.DHAATU not in khanda.typ:
            return False

        vinyaasa = get_vinyaasa(khanda.roopa)

        if vinyaasa[-1] != "र्":
            return False

        return True

    def apply(self, prakriya: Prakriya):
        khanda, khanda_index = UtilFunctions.get_aupadeshika_khanda(prakriya)
        vinyaasa = get_vinyaasa(khanda.roopa)

        indices = [len(vinyaasa) - 1]
        indices.append(len(vinyaasa) - 2)

        if vinyaasa[-2] != "इँ":
            indices.append(len(vinyaasa) - 3)
            if vinyaasa[-2] == "॒":
                khanda.anudaatta_it = True
            else:
                khanda.svarita_it = True

        khanda.it.extend(["इर्"])

        self.push(prakriya, prakriya.vartamaana_sthiti, "इर्-इत्")

        SutraOneThreeNine()(prakriya, khanda, khanda_index, indices)


@dataclass
class SutraOneThreeThree(Sutra):
    """हलन्त्यम् १.३.३"""

    def __post_init__(self):
        self.define("हलन्त्यम् १.३.३")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = UtilFunctions.get_aupadeshika_khanda(prakriya, return_index=False)
        if not khanda:
            return False

        if "इर्" in khanda.it:
            return False

        vinyaasa = get_vinyaasa(khanda.roopa)

        if vinyaasa[-1] not in vyanjana:
            return False

        return True

    def apply(self, prakriya: Prakriya):
        khanda, khanda_index = UtilFunctions.get_aupadeshika_khanda(prakriya)
        vinyaasa = get_vinyaasa(khanda.roopa)

        indices = [len(vinyaasa) - 1]
        khanda.it.extend([vinyaasa[-1]])

        self.push(prakriya, prakriya.vartamaana_sthiti, f"{vinyaasa[-1][0]}कार इत्")

        SutraOneThreeNine()(prakriya, khanda, khanda_index, indices)


@dataclass
class SutraOneThreeFive(Sutra):
    """आदिर्ञिटुडवः १.३.५"""

    def __post_init__(self):
        self.define("आदिर्ञिटुडवः १.३.५")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = UtilFunctions.get_aupadeshika_khanda(prakriya, return_index=False)
        if not khanda:
            return False

        vinyaasa = get_vinyaasa(khanda.roopa)

        if get_shabda(vinyaasa[:2]) not in ["ञि", "टु", "डु"]:
            return False

        return True

    def apply(self, prakriya: Prakriya):
        khanda, khanda_index = UtilFunctions.get_aupadeshika_khanda(prakriya)
        vinyaasa = get_vinyaasa(khanda.roopa)

        indices = [0, 1]
        khanda.it.extend([get_shabda(vinyaasa[:2])])

        if vinyaasa[2] not in vyanjana and vinyaasa[2] not in anunaasika_svara:
            indices.append(2)
            if vinyaasa[2] == "॒":
                khanda.anudaatta_it = True
            else:
                khanda.svarita_it = True

        self.push(
            prakriya, prakriya.vartamaana_sthiti, f"{get_shabda(vinyaasa[:2])} इत्"
        )

        SutraOneThreeNine()(prakriya, khanda, khanda_index, indices)


@dataclass
class SutraOneThreeNine(Sutra):
    """तस्य लोपः १.३.९"""

    def __post_init__(self):
        self.define("तस्य लोपः १.३.९")

    @staticmethod
    def check():
        # pylint: disable=arguments-differ
        pass

    def apply(
        self, prakriya: Prakriya, khanda: Khanda, khanda_index: int, indices: list[int]
    ):
        # pylint: disable=arguments-differ

        vinyaasa = get_vinyaasa(khanda.roopa)

        for index in sorted(indices, reverse=True):
            del vinyaasa[index]

        khanda.roopa = get_shabda(vinyaasa)

        sthiti = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthiti[khanda_index] = khanda

        self.push(prakriya, sthiti, "इत्-लोपः")

    def __call__(
        self, prakriya: Prakriya, khanda: Khanda, khanda_index: int, indices: list[int]
    ):
        self.apply(prakriya, khanda, khanda_index, indices)
