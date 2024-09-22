"""Sutras for Adhyaaya 8"""

from dataclasses import dataclass

from utils import KhandaType, Prakriya, Sutra
from pratyaahaara import expand_pratyahaara
from vinyaasa import get_vinyaasa


@dataclass
class SutraEightTwoThirty(Sutra):
    """चोः कुः ८.२.३०"""

    def __post_init__(self):
        self.define("चोः कुः ८.२.३०")

    @staticmethod
    def check(prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        ss = prakriya.string
        aa = ss[indices[0]]
        bb = ss[indices[1]]

        if aa not in ["च्", "छ्", "ज्", "झ्", "ञ्"]:
            return False

        if bb in expand_pratyahaara("झल्"):
            return True

        khanda = prakriya.get_khanda_for_index(indices[0])

        if KhandaType.PADA not in khanda.typ:
            return False

        vinyaasa = get_vinyaasa(khanda.roopa)
        if vinyaasa[-1] != aa:
            return False

        return True

    def apply(self, prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        aa = prakriya.string[indices[0]]

        if aa == "च्":
            replacement = "क्"
        elif aa == "छ्":
            replacement = "ख्"
        elif aa == "ज्":
            replacement = "ग्"
        elif aa == "झ्":
            replacement = "घ्"
        elif aa == "ञ्":
            replacement = "ङ्"

        prakriya.replace_index(indices[0], replacement)
        self.push(prakriya, prakriya.vartamaana_sthiti, "कुत्वम्")

    def call(self, prakriya: Prakriya, indices: tuple[int, int]):
        """Call the Sutra"""
        if self.check(prakriya, indices):
            self.apply(prakriya, indices)


@dataclass
class SutraEightTwoTwentyThree(Sutra):
    """संयोगान्तस्य लोपः ८.२.२३"""

    def __post_init__(self):
        self.define("संयोगान्तस्य लोपः ८.२.२३")

    @staticmethod
    def check(prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        ss = prakriya.string

        aa = ss[indices[0]]

        if indices[0] == 0:
            return False

        bb = ss[indices[0] - 1]

        if aa not in expand_pratyahaara("हल्"):
            return False

        if bb not in expand_pratyahaara("हल्"):
            return False

        khanda = prakriya.get_khanda_for_index(indices[0])

        if KhandaType.PADA not in khanda.typ:
            return False

        vinyaasa = get_vinyaasa(khanda.roopa)
        if vinyaasa[-1] != aa:
            return False

        return True

    def apply(self, prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        prakriya.replace_index(indices[0], " ")
        self.push(prakriya, prakriya.vartamaana_sthiti, "लोपः")

    def call(self, prakriya: Prakriya, indices: tuple[int, int]):
        """Call the Sutra"""
        if self.check(prakriya, indices):
            self.apply(prakriya, indices)


@dataclass
class SutraEightTwoThirtyNine(Sutra):
    """झलां जशोऽन्ते ८.२.३९"""

    def __post_init__(self):
        self.define("झलां जशोऽन्ते ८.२.३९")

    @staticmethod
    def check(prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        ss = prakriya.string
        aa = ss[indices[0]]

        if aa not in expand_pratyahaara("झल्"):
            return False

        khanda = prakriya.get_khanda_for_index(indices[0])

        if KhandaType.PADA not in khanda.typ:
            return False

        vinyaasa = get_vinyaasa(khanda.roopa)
        if vinyaasa[-1] != aa:
            return False

        return True

    def apply(self, prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        aa = prakriya.string[indices[0]]

        if aa in ["क्", "ख्", "ग्", "घ्", "ह्"]:
            replacement = "ग्"
        elif aa in ["च्", "छ्", "ज्", "झ्", "श्"]:
            replacement = "ज्"
        elif aa in ["ट्", "ठ्", "ड्", "ढ्", "ष्"]:
            replacement = "ड्"
        elif aa in ["त्", "थ्", "द्", "ध्", "स्"]:
            replacement = "द्"
        elif aa in ["प्", "फ्", "ब्", "भ्"]:
            replacement = "ब्"

        prakriya.replace_index(indices[0], replacement)
        self.push(prakriya, prakriya.vartamaana_sthiti, "जश्त्वम्")

    def call(self, prakriya: Prakriya, indices: tuple[int, int]):
        """Call the Sutra"""
        if self.check(prakriya, indices):
            self.apply(prakriya, indices)


@dataclass
class SutraEightTwoSixtySix(Sutra):
    """ससजुषो रुः ८.२.६६"""

    def __post_init__(self):
        self.define("ससजुषो रुः ८.२.६६")

    @staticmethod
    def check(prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        ss = prakriya.string
        aa = ss[indices[0]]

        khanda = prakriya.get_khanda_for_index(indices[0])

        if KhandaType.PADA not in khanda.typ:
            return False

        if khanda.roopa != "सजुष्" and aa != "स्":
            return False

        vinyaasa = get_vinyaasa(khanda.roopa)
        if vinyaasa[-1] != aa:
            return False

        return True

    def apply(self, prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        khanda = prakriya.get_khanda_for_index(indices[0])
        khanda.typ.append(KhandaType.RUTVA)

        prakriya.replace_index(indices[0], "र्")
        self.push(prakriya, prakriya.vartamaana_sthiti, "रुत्वम्")

    def call(self, prakriya: Prakriya, indices: tuple[int, int]):
        """Call the Sutra"""
        if self.check(prakriya, indices):
            self.apply(prakriya, indices)


@dataclass
class SutraEightThreeFifteen(Sutra):
    """खरवसानयोर्विसर्जनीयः ८.३.१५"""

    def __post_init__(self):
        self.define("खरवसानयोर्विसर्जनीयः ८.३.१५")

    @staticmethod
    def check(prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        ss = prakriya.string
        aa = ss[indices[0]]
        bb = ss[indices[1]]

        if aa != "र्":
            return False

        khanda = prakriya.get_khanda_for_index(indices[0])

        if bb not in expand_pratyahaara("खर्") and KhandaType.PADA not in khanda.typ:
            return False

        return True

    def apply(self, prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        prakriya.replace_index(indices[0], "ः")
        self.push(prakriya, prakriya.vartamaana_sthiti, "विसर्गविधानम्")

    def call(self, prakriya: Prakriya, indices: tuple[int, int]):
        """Call the Sutra"""
        if self.check(prakriya, indices):
            self.apply(prakriya, indices)


@dataclass
class SutraEightThreeTwentyThree(Sutra):
    """मोऽनुस्वारः ८.३.२३"""

    def __post_init__(self):
        self.define("मोऽनुस्वारः ८.३.२३")

    @staticmethod
    def check(prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        ss = prakriya.string
        aa = ss[indices[0]]
        bb = ss[indices[1]]

        if aa != "म्":
            return False

        if bb not in expand_pratyahaara("हल्"):
            return False

        khanda = prakriya.get_khanda_for_index(indices[0])

        if KhandaType.PADA not in khanda.typ:
            return False

        vinyaasa = get_vinyaasa(khanda.roopa.strip())
        if aa != vinyaasa[-1]:
            return False

        return True

    def apply(self, prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        prakriya.replace_index(indices[0], "ं")
        self.push(prakriya, prakriya.vartamaana_sthiti, "अनुस्वार अदेशः")

    def call(self, prakriya: Prakriya, indices: tuple[int, int]):
        """Call the Sutra"""
        if self.check(prakriya, indices):
            self.apply(prakriya, indices)


@dataclass
class SutraEightThreeTwentyFour(Sutra):
    """नश्चापदान्तस्य झलि ८.३.२४"""

    def __post_init__(self):
        self.define("नश्चापदान्तस्य झलि ८.३.२४")

    @staticmethod
    def check(prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        ss = prakriya.string
        aa = ss[indices[0]]
        bb = ss[indices[1]]

        if aa not in ["म्", "न्"]:
            return False

        if bb not in expand_pratyahaara("झल्"):
            return False

        khanda = prakriya.get_khanda_for_index(indices[0])
        print(f"khanda: {khanda}")

        vinyaasa = get_vinyaasa(khanda.roopa.strip())
        print(f"vinyaasa: {vinyaasa}")
        if KhandaType.PADA in khanda.typ and aa == vinyaasa[-1]:
            return False

        return True

    def apply(self, prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        prakriya.replace_index(indices[0], "ं")
        self.push(prakriya, prakriya.vartamaana_sthiti, "अनुस्वार अदेशः")

    def call(self, prakriya: Prakriya, indices: tuple[int, int]):
        """Call the Sutra"""
        if self.check(prakriya, indices):
            self.apply(prakriya, indices)


@dataclass
class SutraEightFourFiftyEight(Sutra):
    """अनुस्वारस्य ययि परसवर्णः ८.४.५८"""

    def __post_init__(self):
        self.define("अनुस्वारस्य ययि परसवर्णः ८.४.५८")

    @staticmethod
    def check(prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        ss = prakriya.string
        aa = ss[indices[0]]
        bb = ss[indices[1]]

        if aa != "ं":
            return False

        if bb not in expand_pratyahaara("यय्"):
            return False

        return True

    def apply(self, prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        ss = prakriya.string
        bb = ss[indices[1]]

        if bb in ["क्", "ख्", "ग्", "घ्", "ङ्"]:
            replacement = "ङ्"
        elif bb in ["च्", "छ्", "ज्", "झ्", "ञ्"]:
            replacement = "ञ्"
        elif bb in ["ट्", "ठ्", "ड्", "ढ्", "ण्"]:
            replacement = "ण्"
        elif bb in ["त्", "थ्", "द्", "ध्", "न्"]:
            replacement = "न्"
        elif bb in ["प्", "फ्", "ब्", "भ्", "म्"]:
            replacement = "म्"
        elif bb in ["य्", "र्", "ल्", "व्"]:
            replacement = "ं"

        prakriya.replace_index(indices[0], replacement)
        self.push(prakriya, prakriya.vartamaana_sthiti, "परसवर्णः")

    def call(self, prakriya: Prakriya, indices: tuple[int, int]):
        """Call the Sutra"""
        if self.check(prakriya, indices):
            self.apply(prakriya, indices)
