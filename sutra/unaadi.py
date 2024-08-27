"""Module for Unaadi Sutras"""

from dataclasses import dataclass
import copy

from utils import Prakriya, KhandaType, Unaadi, get_shabda, get_vinyaasa

from aagama import Aagama
from varna import svara
from krt import Krt
from sutra.sutra_list import SutraUtils, SutraOneOneFortySix
from it_prakarana import ItSanjna


@dataclass
class UnaadiTwoFiftyEight(Unaadi):
    """क्विब्वचिप्रच्छिश्रिस्रुद्रुप्रुज्वां दीर्घोऽसंप्रसारणं च २.५८"""

    def __post_init__(self):
        self.define("क्विब्वचिप्रच्छिश्रिस्रुद्रुप्रुज्वां दीर्घोऽसंप्रसारणं च २.५८")

    @staticmethod
    def check(prakriya: Prakriya, pratyaya: str):
        # pylint: disable=arguments-differ

        if pratyaya != "क्विप्":
            return False

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

        if khanda.upadesha not in ["व॒चँ", "प्र॒छँ", "श्रिञ्", "स्रु॒", "द्रु॒", "प्रु॒ङ्", "जुडँ"]:
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

        pratyaya = Krt(moola="क्विप्", mukhya=khanda)
        vv = get_vinyaasa(pratyaya.mukhya.roopa)
        for i, v in enumerate(vv):
            if v in svara:
                if v == "अ":
                    vv[i] = "आ"
                elif v == "इ":
                    vv[i] = "ई"
                elif v == "उ":
                    vv[i] = "ऊ"

        pratyaya.mukhya.roopa = get_shabda(vv)

        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis.insert(khanda_index + 1, pratyaya)

        self.push(prakriya, sthitis, "क्विप्प्रत्ययादेशः दीर्घः असंप्रसारणं च")

        # pratyaya.remove_uchchaarana()

        # ucchaarana = get_vinyaasa(pratyaya.moola)[pratyaya.uchchaarana[0]]

        # prakriya.add_to_prakriya(sthitis, "-", f"{ucchaarana}कार उच्चारणार्थम्")

    def call(self, prakriya: Prakriya, pratyaya: str):
        """Call the Sutra"""
        if self.check(prakriya, pratyaya):
            self.apply(prakriya)


@dataclass
class UnaadiTwoSixtySeven(Unaadi):
    """गमेर्डोः २.२७"""

    def __post_init__(self):
        self.define("गमेर्डोः २.२७")

    @staticmethod
    def check(prakriya: Prakriya, pratyaya: str):
        # pylint: disable=arguments-differ

        if pratyaya != "डो":
            return False

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

        if khanda.upadesha != "ग॒मॢँ":
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

        pratyaya = Krt(moola="डो", mukhya=khanda)

        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis.insert(khanda_index + 1, pratyaya)

        self.push(prakriya, sthitis, "डोप्रत्ययादेशः")

    def call(self, prakriya: Prakriya, pratyaya: str):
        """Call the Sutra"""
        if self.check(prakriya, pratyaya):
            self.apply(prakriya)


@dataclass
class UnaadiFourTwentyFive(Unaadi):
    """अलीकादयश्च ४.२५"""

    def __post_init__(self):
        self.define("अलीकादयश्च ४.२५")

    @staticmethod
    def check(prakriya: Prakriya, pratyaya: str):
        # pylint: disable=arguments-differ

        if pratyaya != "कीकच्":
            return False

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)

        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][1]
        khanda_index = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][0]

        pratyaya = Krt(moola="कीकच्", mukhya=khanda)
        prakriya.vartamaana_sthiti.insert(khanda_index + 1, pratyaya)

        self.push(prakriya, prakriya.vartamaana_sthiti, "कीकच्प्रत्ययादेशः")

        ItSanjna(prakriya)

        if khanda.roopa == "वल्":

            aagama = Aagama(moola="मुट्", mukhya=pratyaya, uchchaarana=[1])
            prakriya.vartamaana_sthiti.insert(khanda_index + 2, aagama)

            prakriya.add_to_prakriya(
                prakriya.vartamaana_sthiti, "-", "बाहुलकात् प्रत्ययस्य मुट् आगमः"
            )

            aagama.remove_uchchaarana()

            ucchaarana = get_vinyaasa(aagama.moola)[aagama.uchchaarana[0]]

            prakriya.add_to_prakriya(
                prakriya.vartamaana_sthiti, "-", f"{ucchaarana}कार उच्चारणार्थम्"
            )

            ItSanjna(prakriya)
            SutraOneOneFortySix()(prakriya)


    def call(self, prakriya: Prakriya, pratyaya: str):
        """Call the Sutra"""
        if self.check(prakriya, pratyaya):
            self.apply(prakriya)


@dataclass
class UnaadiFourOneHundredTwentyTwo(Unaadi):
    """मनेरुच्च ४.१२२"""

    def __post_init__(self):
        self.define("मनेरुच्च ४.१२२")

    @staticmethod
    def check(prakriya: Prakriya, pratyaya: str):
        # pylint: disable=arguments-differ

        if pratyaya != "इन्":
            return False

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)

        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        khanda = khanda[0][1]

        if khanda.roopa != "मन्":
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][1]
        khanda_index = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][0]

        pratyaya = Krt(moola="इन्", mukhya=khanda)
        prakriya.vartamaana_sthiti.insert(khanda_index + 1, pratyaya)
        khanda.roopa = "मुन्"

        self.push(prakriya, prakriya.vartamaana_sthiti, "इन्-प्रत्ययादेशः अकारस्य उकारश्च")

    def call(self, prakriya: Prakriya, pratyaya: str):
        """Call the Sutra"""
        if self.check(prakriya, pratyaya):
            self.apply(prakriya)


@dataclass
class UnaadiFourOneHundredSeventySeven(Unaadi):
    """पातेर्डुम्सुन् ४.१७७"""

    def __post_init__(self):
        self.define("पातेर्डुम्सुन् ४.१७७")

    @staticmethod
    def check(prakriya: Prakriya, pratyaya: str):
        # pylint: disable=arguments-differ

        if pratyaya != "डुम्सुँन्":
            return False

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)

        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        khanda = khanda[0][1]

        if khanda.upadesha != "पा॒":
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][1]
        khanda_index = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][0]

        pratyaya = Krt(moola="डुम्सुँन्", mukhya=khanda)

        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis.insert(khanda_index + 1, pratyaya)

        self.push(prakriya, sthitis, "डुम्सुँन्प्रत्ययादेशः")

    def call(self, prakriya: Prakriya, pratyaya: str):
        """Call the Sutra"""
        if self.check(prakriya, pratyaya):
            self.apply(prakriya)


@dataclass
class UnaadiFourOneHundredEightyEight(Unaadi):
    """सर्वधातुभ्योऽसुन् ४.१८८"""

    def __post_init__(self):
        self.define("सर्वधातुभ्योऽसुन् ४.१८८")

    @staticmethod
    def check(prakriya: Prakriya, pratyaya: str):
        # pylint: disable=arguments-differ

        if pratyaya != "असुन्":
            return False

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.DHAATU in khanda.typ
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
            if KhandaType.DHAATU in khanda.typ
        ][0]

        khanda_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.DHAATU in khanda.typ
        ][0]

        pratyaya = Krt(moola="असुन्", mukhya=khanda, uchchaarana=[2])

        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis.insert(khanda_index + 1, pratyaya)

        self.push(prakriya, sthitis, "असुन्प्रत्ययादेशः")

        pratyaya.remove_uchchaarana()

        ucchaarana = get_vinyaasa(pratyaya.moola)[pratyaya.uchchaarana[0]]

        prakriya.add_to_prakriya(sthitis, "-", f"{ucchaarana}कार उच्चारणार्थम्")

    def call(self, prakriya: Prakriya, pratyaya: str):
        """Call the Sutra"""
        if self.check(prakriya, pratyaya):
            self.apply(prakriya)
