"""Sutras for Adhyaaya 3"""

from dataclasses import dataclass
import copy

from dhaatu import Gana
from utils import Prakriya, Sutra, KhandaType, Krdartha
from sanaadi import Sanaadi
from sutra.sutra_list import SutraUtils
from vinyaasa import get_vinyaasa

from krt import Krt


@dataclass
class SutraThreeOneTwentyFive(Sutra):
    """सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो णिच् ३.१.२५"""

    def __post_init__(self):
        self.define("सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो णिच् ३.१.२५")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = SutraUtils.get_khanda(
            prakriya, [KhandaType.DHAATU, KhandaType.PRAATIPADIKA]
        )
        if not khanda:
            return False
        if len(khanda) != 1:
            return False
        khanda = khanda[0][1]

        if KhandaType.PRAATIPADIKA in khanda.typ:
            raise NotImplementedError("Praatipadika not implemented")

        if Gana.CHURAADI not in khanda.typ:
            return False

        return True

    def apply(self, prakriya: Prakriya):
        khanda = SutraUtils.get_khanda(
            prakriya, [KhandaType.DHAATU, KhandaType.PRAATIPADIKA]
        )[0][1]

        pratyaya = Sanaadi(moola="णिच्", mukhya=khanda)

        prakriya.vartamaana_sthiti.append(pratyaya)

        self.push(
            prakriya, prakriya.vartamaana_sthiti, f"{khanda.roopa} इत्यस्य अनुदात्तोपदेशः"
        )


@dataclass
class SutraThreeTwoOneHundredTwo(Sutra):
    """निष्ठा ३.२.१०२"""

    def __post_init__(self):
        self.define("निष्ठा ३.२.१०२")

    @staticmethod
    def check(prakriya: Prakriya, artha: Krdartha, pratyaya: str):
        # pylint: disable=arguments-differ

        if not (pratyaya in ["क्त", "क्तवतुँ"] and artha == Krdartha.BHOOTA):
            return False

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)
        if not khanda:
            return False
        if len(khanda) != 1:
            return False

        return True

    def apply(self, prakriya: Prakriya, artha: Krdartha, pratyaya: str):
        # pylint: disable=arguments-differ

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][1]
        khanda_index = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][0]

        krt = Krt(moola=pratyaya, mukhya=khanda)
        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis.insert(khanda_index + 1, krt)

        self.push(prakriya, sthitis, f"{artha.value}-अर्थे {pratyaya} प्रत्ययः")

    def call(self, praakriya: Prakriya, pratyaya: str, artha: Krdartha):
        """Call the Sutra"""
        if self.check(praakriya, artha, pratyaya):
            self.apply(praakriya, artha, pratyaya)


@dataclass
class SutraThreeTwoOne(Sutra):
    """कर्मण्यण् ३.२.१"""

    def __post_init__(self):
        self.define("कर्मण्यण् ३.२.१")

    @staticmethod
    def check(prakriya: Prakriya, artha: Krdartha, pratyaya: str):
        # pylint: disable=arguments-differ

        if not (pratyaya == "अण्" and artha == Krdartha.ANAADI):
            return False

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)
        if not khanda:
            return False

        upapada = SutraUtils.get_khanda(prakriya, KhandaType.PRAATIPADIKA)
        if not upapada:
            return False

        sup = SutraUtils.get_khanda(prakriya, KhandaType.SUP)
        if not sup:
            return False

        if sup[0][1].moola not in ["ङस्", "ओस्", "आम्"]:
            return False

        if len(khanda) != 1:
            return False

        return True

    def apply(self, prakriya: Prakriya, artha: Krdartha, pratyaya: str):
        # pylint: disable=arguments-differ

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][1]
        khanda_index = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][0]

        krt = Krt(moola=pratyaya, mukhya=khanda)
        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis.insert(khanda_index + 1, krt)

        self.push(prakriya, sthitis, f"{artha.value}-अर्थे {pratyaya} प्रत्ययः")

    def call(self, praakriya: Prakriya, pratyaya: str, artha: Krdartha):
        """Call the Sutra"""
        if self.check(praakriya, artha, pratyaya):
            self.apply(praakriya, artha, pratyaya)


@dataclass
class SutraThreeTwoThree(Sutra):
    """आतोऽनुपसर्गे कः ३.२.३"""

    def __post_init__(self):
        self.define("आतोऽनुपसर्गे कः ३.२.३")

    @staticmethod
    def check(prakriya: Prakriya, artha: Krdartha, pratyaya: str):
        # pylint: disable=arguments-differ

        if not (pratyaya == "क" and artha == Krdartha.ANAADI):
            return False

        upapada = SutraUtils.get_khanda(prakriya, KhandaType.PRAATIPADIKA)
        if not upapada:
            return False

        sup = SutraUtils.get_khanda(prakriya, KhandaType.SUP)
        if not sup:
            return False

        if sup[0][1].moola not in ["ङस्", "ओस्", "आम्"]:
            return False

        upasarga = SutraUtils.get_khanda(prakriya, KhandaType.UPASARGA)
        if upasarga:
            return False

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)
        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        vinyaasa = get_vinyaasa(khanda[0][1].roopa)

        if vinyaasa[-1] != "आ":
            return False

        return True
    
    def apply(self, prakriya: Prakriya, artha: Krdartha, pratyaya: str):
        # pylint: disable=arguments-differ

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][1]
        khanda_index = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][0]

        krt = Krt(moola=pratyaya, mukhya=khanda)
        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis.insert(khanda_index + 1, krt)

        self.push(prakriya, sthitis, f"{artha.value}-अर्थे {pratyaya} प्रत्ययः")

    def call(self, praakriya: Prakriya, pratyaya: str, artha: Krdartha):
        """Call the Sutra"""
        if self.check(praakriya, artha, pratyaya):
            self.apply(praakriya, artha, pratyaya)


@dataclass
class SutraThreeThreeEighteen(Sutra):
    """भावे ३.३.१८"""

    def __post_init__(self):
        self.define("भावे ३.३.१८")

    @staticmethod
    def check(prakriya: Prakriya, artha: Krdartha, pratyaya: str):
        # pylint: disable=arguments-differ

        if not (pratyaya == "घञ्" and artha == Krdartha.BHAAVA):
            return False
        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)
        if not khanda:
            return False
        if len(khanda) != 1:
            return False

        sutra = SutraThreeThreeTwentyOne()
        sutra.call(prakriya, pratyaya, artha)
        if sutra.check(prakriya, artha, pratyaya):
            return False

        return True

    def apply(self, prakriya: Prakriya, artha: Krdartha, pratyaya: str):
        # pylint: disable=arguments-differ

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][1]
        khanda_index = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][0]

        krt = Krt(moola=pratyaya, mukhya=khanda)
        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis.insert(khanda_index + 1, krt)

        self.push(prakriya, sthitis, f"{artha.value}-अर्थे {pratyaya} प्रत्ययः")

    def call(self, praakriya: Prakriya, pratyaya: str, artha: Krdartha):
        """Call the Sutra"""
        if self.check(praakriya, artha, pratyaya):
            self.apply(praakriya, artha, pratyaya)


@dataclass
class SutraThreeThreeTwentyOne(Sutra):
    """इङश्च ३.३.२१"""

    def __post_init__(self):
        self.define("इङश्च ३.३.२१")

    @staticmethod
    def check(prakriya: Prakriya, artha: Krdartha, pratyaya: str):
        # pylint: disable=arguments-differ

        if not (pratyaya == "घञ्" and artha == Krdartha.BHAAVA):
            return False
        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)
        if not khanda:
            return False
        if len(khanda) != 1:
            return False
        khanda = khanda[0][1]

        if khanda.upadesha != "इ॒ङ्":
            return False

        return True

    def apply(self, prakriya: Prakriya, artha: Krdartha, pratyaya: str):
        # pylint: disable=arguments-differ

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][1]
        khanda_index = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][0]

        krt = Krt(moola=pratyaya, mukhya=khanda)
        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis.insert(khanda_index + 1, krt)

        self.push(prakriya, sthitis, f"{artha.value}-अर्थे {pratyaya} प्रत्ययः")

    def call(self, praakriya: Prakriya, pratyaya: str, artha: Krdartha):
        """Call the Sutra"""
        if self.check(praakriya, artha, pratyaya):
            self.apply(praakriya, artha, pratyaya)


@dataclass
class SutraThreeThreeFiftySeven(Sutra):
    """ॠदोरप् ३.३.५७"""

    def __post_init__(self):
        self.define("ॠदोरप् ३.३.५७")

    @staticmethod
    def check(prakriya: Prakriya, artha: Krdartha, pratyaya: str):
        # pylint: disable=arguments-differ

        if not (pratyaya == "अप्" and artha == Krdartha.BHAAVA):
            return False
        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)
        if not khanda:
            return False
        if len(khanda) != 1:
            return False
        khanda = khanda[0][1]

        sutra = SutraThreeThreeFiftyEight()
        sutra.call(prakriya, pratyaya, artha)

        if get_vinyaasa(khanda.roopa)[-1] not in ["ॠ", "उ", "ऊ"]:
            return False

        return True

    def apply(self, prakriya: Prakriya, artha: Krdartha, pratyaya: str):
        # pylint: disable=arguments-differ

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][1]
        khanda_index = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][0]

        krt = Krt(moola=pratyaya, mukhya=khanda)
        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis.insert(khanda_index + 1, krt)

        self.push(prakriya, sthitis, f"{artha.value}-अर्थे {pratyaya} प्रत्ययः")

    def call(self, praakriya: Prakriya, pratyaya: str, artha: Krdartha):
        """Call the Sutra"""
        if self.check(praakriya, artha, pratyaya):
            self.apply(praakriya, artha, pratyaya)


@dataclass
class SutraThreeThreeFiftyEight(Sutra):
    """ग्रहवृदृनिश्चिगमश्च ३.३.५८"""

    def __post_init__(self):
        self.define("ग्रहवृदृनिश्चिगमश्च ३.३.५८")

    @staticmethod
    def check(prakriya: Prakriya, artha: Krdartha, pratyaya: str):
        # pylint: disable=arguments-differ

        if not (pratyaya == "अप्" and artha == Krdartha.BHAAVA):
            return False
        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)
        if not khanda:
            return False
        if len(khanda) != 1:
            return False
        khanda = khanda[0][1]

        if khanda.upadesha not in ["ग्रहँ॑", "वृञ्", "दृ॒ङ्", "चि॒ञ्", "ग॒मॢँ"]:
            return False

        return True

    def apply(self, prakriya: Prakriya, artha: Krdartha, pratyaya: str):
        # pylint: disable=arguments-differ

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][1]
        khanda_index = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][0]

        krt = Krt(moola=pratyaya, mukhya=khanda)
        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis.insert(khanda_index + 1, krt)

        self.push(prakriya, sthitis, f"{artha.value}-अर्थे {pratyaya} प्रत्ययः")

    def call(self, praakriya: Prakriya, pratyaya: str, artha: Krdartha):
        """Call the Sutra"""
        if self.check(praakriya, artha, pratyaya):
            self.apply(praakriya, artha, pratyaya)


@dataclass
class SutraThreeFourOneHundredThirteen(Sutra):
    """तिङ्शित्सार्वधातुकम् ३.४.११३"""

    def __post_init__(self):
        self.define("तिङ्शित्सार्वधातुकम् ३.४.११३")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.PRATYAAYA in khanda.typ
            and (KhandaType.TIN in khanda.typ or "श्" in khanda.it)
            and KhandaType.DHAATU in khanda.mukhya.typ
            and KhandaType.AARDHADHAATUKA not in khanda.typ
            and KhandaType.SAARVADHAATUKA not in khanda.typ
        ]

        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.PRATYAAYA in khanda.typ
            and (KhandaType.TIN in khanda.typ or "श्" in khanda.it)
            and KhandaType.DHAATU in khanda.mukhya.typ
            and KhandaType.AARDHADHAATUKA not in khanda.typ
            and KhandaType.SAARVADHAATUKA not in khanda.typ
        ][0]

        khanda.typ.append(KhandaType.SAARVADHAATUKA)

        self.push(
            prakriya, prakriya.vartamaana_sthiti, f"{khanda.roopa} इत्यस्य सार्वधातुकसंज्ञा"
        )


@dataclass
class SutraThreeFourOneHundredFourteen(Sutra):
    """आर्धधातुकं शेषः ३.४.११४"""

    def __post_init__(self):
        self.define("आर्धधातुकं शेषः ३.४.११४")

    @staticmethod
    def check(prakriya: Prakriya):

        if SutraThreeFourOneHundredThirteen.check(prakriya):
            return False

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)

        if not khanda:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.PRATYAAYA in khanda.typ
            and KhandaType.DHAATU in khanda.mukhya.typ
            and KhandaType.AARDHADHAATUKA not in khanda.typ
            and KhandaType.SAARVADHAATUKA not in khanda.typ
        ][0]

        khanda.typ.append(KhandaType.AARDHADHAATUKA)

        self.push(
            prakriya, prakriya.vartamaana_sthiti, f"{khanda.roopa} इत्यस्य आर्धधातुकसंज्ञा"
        )
