"""All sutras"""

from dataclasses import dataclass
import copy

from utils import Prakriya, UtilFunctions, Sutra, KhandaType, Khanda
from varna import anunaasika_svara, vyanjana
from vinyaasa import get_vinyaasa, get_shabda

from aagama import Aagama
from dhaatu import Dhaatu


@dataclass
class SutraOneOneFortySix(Sutra):
    """आद्यन्तौ टकितौ १.१.४६"""

    def __post_init__(self):
        self.define("आद्यन्तौ टकितौ १.१.४६")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.AAGAMA in khanda.typ
        ]
        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        khanda = khanda[0]

        if "ट्" not in khanda.it and "क्" not in khanda.it:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.AAGAMA in khanda.typ
        ][0]

        khanda_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.AAGAMA in khanda.typ
        ][0]

        mukhya = khanda.mukhya
        varnas = get_vinyaasa(mukhya.roopa)

        mukhya_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if khanda.roopa == mukhya.roopa
        ][0]

        aagama = get_vinyaasa(khanda.roopa)[0]

        if "ट्" in khanda.it:
            varnas.insert(0, aagama)

        if "क्" in khanda.it:
            varnas.append(aagama)

        mukhya.roopa = get_shabda(varnas)

        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis[mukhya_index] = mukhya
        sthitis.pop(khanda_index)

        self.push(prakriya, sthitis, "आद्यन्तौ टकितौ")


@dataclass
class SutraOneOneFortySeven(Sutra):
    """मिदचोन्त्यात् परः १.१.४७"""

    def __post_init__(self):
        self.define("मिदचोन्त्यात् परः १.१.४७")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.AAGAMA in khanda.typ
        ]
        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        khanda = khanda[0]

        if "म्" not in khanda.it:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.AAGAMA in khanda.typ
        ][0]

        khanda_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.AAGAMA in khanda.typ
        ][0]

        mukhya = khanda.mukhya
        varnas = get_vinyaasa(mukhya.roopa)

        mukhya_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if khanda.roopa == mukhya.roopa
        ][0]

        aagama = get_vinyaasa(khanda.roopa)[0]

        count = len(varnas) - 1
        while count >= 0:
            if varnas[count] not in vyanjana:
                break
            count -= 1

        varnas.insert(count + 1, aagama)

        mukhya.roopa = get_shabda(varnas)

        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis[mukhya_index] = mukhya
        sthitis.pop(khanda_index)

        self.push(prakriya, sthitis, "आद्यन्तौ टकितौ")


@dataclass
class SutraOneThreeOne(Sutra):
    """भूवादयो धातवः १.३.१"""

    def __post_init__(self):
        self.define("भूवादयो धातवः १.३.१")

    @staticmethod
    def check(prakriya: Prakriya):
        # pylint: disable=arguments-differ
        if not prakriya.vartamaana_sthiti:
            return True
        return False

    def apply(self, prakriya: Prakriya, moola: str):
        # pylint: disable=arguments-differ

        dhaatu = Dhaatu(moola=moola)
        self.push(prakriya, [dhaatu], f"{dhaatu.gana}स्य धातुः")

    def call(self, praakriya: Prakriya, moola: str):
        """Call the Sutra"""
        if self.check(praakriya):
            self.apply(praakriya, moola)


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


@dataclass
class SutraSixOneSixtyFour(Sutra):
    """धात्वादेः षः सः ६.१.६४"""

    def __post_init__(self):
        self.define("धात्वादेः षः सः ६.१.६४")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.DHAATU in khanda.typ
        ]

        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        khanda = khanda[0]

        varnas = get_vinyaasa(khanda.roopa)
        if varnas[0] != "ष्":
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.DHAATU in khanda.typ
        ][0]

        khanda_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.DHAATU in khanda.typ
        ][0]

        varnas = get_vinyaasa(khanda.roopa)
        varnas[0] = "स्"

        replacement = {
            "ण्": "न्",
            "ट्": "त्",
            "ठ्": "थ्",
        }

        if varnas[1] in replacement:
            varnas[1] = replacement[varnas[1]]

        if varnas[2] in replacement:
            varnas[2] = replacement[varnas[2]]

        khanda.roopa = get_shabda(varnas)

        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis[khanda_index] = khanda

        self.push(prakriya, sthitis, "षकारस्य सकारः")


@dataclass
class SutraSixOneSixtyFive(Sutra):
    """णो नः ६.१.६५"""

    def __post_init__(self):
        self.define("णो नः ६.१.६५")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.DHAATU in khanda.typ
        ]

        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        khanda = khanda[0]

        varnas = get_vinyaasa(khanda.roopa)
        if varnas[0] != "ण्":
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.DHAATU in khanda.typ
        ][0]

        khanda_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.DHAATU in khanda.typ
        ][0]

        varnas = get_vinyaasa(khanda.roopa)
        varnas[0] = "न्"

        khanda.roopa = get_shabda(varnas)

        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis[khanda_index] = khanda

        self.push(prakriya, sthitis, "णकारस्य नकारः")


@dataclass
class SutraSevenOneFiftyEight(Sutra):
    """इदितो नुम् धातोः ७.१.५८"""

    def __post_init__(self):
        self.define("इदितो नुम् धातोः ७.१.५८")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.DHAATU in khanda.typ
        ]

        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        khanda = khanda[0]

        if "इ" not in khanda.it:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.DHAATU in khanda.typ
        ][0]

        khanda_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.DHAATU in khanda.typ
        ][0]

        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        aagama = Aagama(moola="नुम्", uchchaarana=[1], mukhya=khanda)
        sthitis.insert(khanda_index + 1, aagama)

        self.push(prakriya, sthitis, f"इदितस्य {khanda}-धातोः नुमागमः")

        aagama.remove_uchchaarana()

        ucchaarana = get_vinyaasa(aagama.moola)[aagama.uchchaarana[0]]

        prakriya.add_to_prakriya(sthitis, "-", f"{ucchaarana}कार उच्चारणार्थम्")
