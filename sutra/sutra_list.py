"""All sutras"""

from dataclasses import dataclass
import copy

from utils import Prakriya, UtilFunctions, Sutra, KhandaType, Khanda, Krdartha
from varna import anunaasika_svara, vyanjana, svara
from vinyaasa import get_vinyaasa, get_shabda
from pratyaahaara import expand_pratyahaara

from aagama import Aagama
from dhaatu import Dhaatu, Gana
from upasarga import Upasarga


class SutraUtils:
    """Utility functions for Sutras"""

    @staticmethod
    def get_khanda(
        prakriya: Prakriya,
        include: list[KhandaType] = None,
        exclude: list[KhandaType] = None,
    ):
        """Get khanda of a specific type"""

        if isinstance(include, KhandaType):
            include = [include]

        if isinstance(exclude, KhandaType):
            exclude = [exclude]

        if not include:
            include = []

        if not exclude:
            exclude = []

        khanda = [
            (idx, khanda)
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if any(typ in khanda.typ for typ in include)
            and not any(typ in khanda.typ for typ in exclude)
        ]

        if not khanda:
            return None

        return khanda

    @staticmethod
    def check_pratyaya_and_artha(
        pratyaya: str, artha: Krdartha, expected_pratyaya: str, expected_artha: Krdartha
    ):
        """Check if the pratyaya and artha are compatible"""

        if artha != expected_artha:
            return False

        if pratyaya != expected_pratyaya:
            return False

        return True


@dataclass
class SutraOneOneFive(Sutra):
    """क्ङिति च १.१.५"""

    def __post_init__(self):
        self.define("क्ङिति च १.१.५")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if (
                KhandaType.AARDHADHAATUKA in khanda.typ
                or KhandaType.SAARVADHAATUKA in khanda.typ
            )
            and KhandaType.KRTITAGUNA not in khanda.typ
        ]

        if not khanda:
            return False

        khanda = khanda[0]

        if "क्" not in khanda.it and "ङ्" not in khanda.it and "ग्" not in khanda.it:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        self.push(prakriya, prakriya.vartamaana_sthiti, "गुणवृद्धिनिषेधः")


@dataclass
class SutraOneOneThirtySeven(Sutra):
    """स्वरादिनिपातमव्ययम् १.१.३७"""

    def __post_init__(self):
        self.define("स्वरादिनिपातमव्ययम् १.१.३७")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.NIPAATA in khanda.typ and KhandaType.AVYAYA not in khanda.typ
        ]
        if len(khanda) == 1:
            return True

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.SVARAADI in khanda.typ and KhandaType.AVYAYA not in khanda.typ
        ]

        if len(khanda) == 1:
            return True

        return False

    def apply(self, prakriya: Prakriya):
        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if (KhandaType.NIPAATA in khanda.typ or KhandaType.SVARAADI in khanda.typ)
            and KhandaType.AVYAYA not in khanda.typ
        ]

        khanda = khanda[0]

        khanda.typ.append(KhandaType.AVYAYA)

        self.push(
            prakriya, prakriya.vartamaana_sthiti, f"{khanda.roopa} इत्यस्य अव्ययसंज्ञा"
        )


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
class SutraOneTwoFortyFive(Sutra):
    """अर्थवदधातुरप्रत्ययः प्रातिपदिकम् १.२.४५"""

    def __post_init__(self):
        self.define("अर्थवदधातुरप्रत्ययः प्रातिपदिकम् १.२.४५")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.GANAPAATHA in khanda.typ
            and KhandaType.PRAATIPADIKA not in khanda.typ
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
            if KhandaType.GANAPAATHA in khanda.typ
            and KhandaType.PRAATIPADIKA not in khanda.typ
        ][0]

        khanda.typ.append(KhandaType.PRAATIPADIKA)

        self.push(
            prakriya, prakriya.vartamaana_sthiti, f"{khanda.roopa} इत्यस्य प्रातिपदिकसंज्ञा"
        )


@dataclass
class SutraOneTwoFortySix(Sutra):
    """कृत्तद्धितसमासाश्च १.२.४६"""

    def __post_init__(self):
        self.define("कृत्तद्धितसमासाश्च १.२.४६")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = prakriya.vartamaana_sthiti[-1]

        if KhandaType.KRT in khanda.typ:
            return True

        if KhandaType.TADDHITA in khanda.typ:
            return True

        count = len(
            list(
                [
                    khanda
                    for khanda in prakriya.vartamaana_sthiti
                    if KhandaType.SUP in khanda.typ
                ]
            )
        )

        if count > 1 and KhandaType.SUP in khanda.typ:
            return True

        return False

    def apply(self, prakriya: Prakriya):

        for khanda in prakriya.vartamaana_sthiti:
            if KhandaType.PRAATIPADIKA not in khanda.typ:
                khanda.typ.append(KhandaType.PRAATIPADIKA)

        self.push(prakriya, prakriya.vartamaana_sthiti, "प्रातिपदिकसंज्ञा")


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

        if not any(
            khanda.typ == KhandaType.DHAATU for khanda in prakriya.vartamaana_sthiti
        ):
            return True

        return False

    def apply(self, prakriya: Prakriya, moola: str):
        # pylint: disable=arguments-differ

        dhaatu = Dhaatu(moola=moola)
        self.push(prakriya, [dhaatu], f"{dhaatu.gana.value}गणस्य धातुः")

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

        sutra = SutraOneThreeFour()
        sutra(prakriya)
        if sutra.check(prakriya):
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
class SutraOneThreeFour(Sutra):
    """न विभक्तौ तुस्माः १.३.४"""

    def __post_init__(self):
        self.define("न विभक्तौ तुस्माः १.३.४")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = UtilFunctions.get_aupadeshika_khanda(prakriya, return_index=False)
        if not khanda:
            return False

        if KhandaType.VIBHAKTI not in khanda.typ:
            return False

        vinyaasa = get_vinyaasa(khanda.roopa)

        if vinyaasa[-1] not in ["स्", "म्", "त्", "थ्", "द्", "ध्", "न्"]:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = UtilFunctions.get_aupadeshika_khanda(prakriya, return_index=False)
        vinyaasa = get_vinyaasa(khanda.roopa)
        varna = vinyaasa[-1]
        self.push(prakriya, prakriya.vartamaana_sthiti, f"{varna[0]}कारो न इट्")


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

        if KhandaType.DHAATU not in khanda.typ:
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
class SutraOneThreeSeven(Sutra):
    """चुटू १.३.७"""

    def __post_init__(self):
        self.define("चुटू १.३.७")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = UtilFunctions.get_aupadeshika_khanda(prakriya, return_index=False)
        if not khanda:
            return False

        vinyaasa = get_vinyaasa(khanda.roopa)

        if vinyaasa[0] not in ["च्", "छ्", "ज्", "झ्", "ञ्", "ट्", "ठ्", "ड्", "ढ्", "ण्"]:
            return False

        return True

    def apply(self, prakriya: Prakriya):
        khanda, khanda_index = UtilFunctions.get_aupadeshika_khanda(prakriya)
        vinyaasa = get_vinyaasa(khanda.roopa)

        indices = [0]
        khanda.it.extend([vinyaasa[0]])

        self.push(prakriya, prakriya.vartamaana_sthiti, f"{vinyaasa[0][0]}कार इत्")

        SutraOneThreeNine()(prakriya, khanda, khanda_index, indices)


@dataclass
class SutraOneThreeEight(Sutra):
    """लशक्वतद्धिते १.३.८"""

    def __post_init__(self):
        self.define("लशक्वतद्धिते १.३.८")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = UtilFunctions.get_aupadeshika_khanda(prakriya, return_index=False)
        if not khanda:
            return False

        if KhandaType.PRATYAAYA not in khanda.typ:
            return False

        if KhandaType.TADDHITA in khanda.typ:
            return False

        vinyaasa = get_vinyaasa(khanda.roopa)

        if vinyaasa[0] not in ["ल्", "श्", "क्", "ख्", "ग्", "घ्", "ङ्"]:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda, khanda_index = UtilFunctions.get_aupadeshika_khanda(prakriya)
        vinyaasa = get_vinyaasa(khanda.roopa)

        indices = [0]
        khanda.it.extend([vinyaasa[0]])

        self.push(prakriya, prakriya.vartamaana_sthiti, f"{vinyaasa[0][0]}कार इत्")

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
class SutraOneFourFourteen(Sutra):
    """सुप्तिङन्तं पदम् १.४.१४"""

    def __post_init__(self):
        self.define("सुप्तिङन्तं पदम् १.४.१४")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.SUP in khanda.typ or KhandaType.TIN in khanda.typ
        ]

        if not khanda:
            return False

        return True

    def apply(self, prakriya: Prakriya):
        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.SUP in khanda.typ or KhandaType.TIN in khanda.typ
        ][0]

        khanda_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.SUP in khanda.typ or KhandaType.TIN in khanda.typ
        ][0]

        padaadi = khanda.mukhya

        while khanda_index >= 0:

            prakriya.vartamaana_sthiti[khanda_index].typ.append(KhandaType.PADA)

            if padaadi.roopa == prakriya.vartamaana_sthiti[khanda_index].roopa:
                break

            khanda_index -= 1

        self.push(prakriya, prakriya.vartamaana_sthiti, f"{padaadi.roopa} इत्यस्य पदसंज्ञा")


@dataclass
class SutraOneFourEighteen(Sutra):
    """यचि भम् १.४.१८"""

    def __post_init__(self):
        self.define("यचि भम् १.४.१८")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = [
            khanda
            for index, khanda in enumerate(prakriya.vartamaana_sthiti)
            if (
                KhandaType.SUP in khanda.typ
                or KhandaType.TADDHITA in khanda.typ
                or KhandaType.STRI in khanda.typ
            )
            and KhandaType.BHA not in prakriya.vartamaana_sthiti[index - 1].typ
        ]

        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        khanda = khanda[0]
        vinyaasa = get_vinyaasa(khanda.roopa)

        if vinyaasa[0] not in svara and vinyaasa[0] != "य्":
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda_index = [
            index
            for index, khanda in enumerate(prakriya.vartamaana_sthiti)
            if (
                KhandaType.SUP in khanda.typ
                or KhandaType.TADDHITA in khanda.typ
                or KhandaType.STRI in khanda.typ
            )
            and KhandaType.BHA not in prakriya.vartamaana_sthiti[index - 1].typ
        ][0]

        prakriti = prakriya.vartamaana_sthiti[khanda_index - 1]

        prakriti.typ.append(KhandaType.BHA)

        self.push(prakriya, prakriya.vartamaana_sthiti, f"{prakriti.roopa} इत्यस्य भसंज्ञा")


@dataclass
class SutraOneFourFiftyEight(Sutra):
    """प्रादयः १.४.५८"""

    def __post_init__(self):
        self.define("प्रादयः १.४.५८")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.PRAADI in khanda.typ and KhandaType.NIPAATA not in khanda.typ
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
            if KhandaType.PRAADI in khanda.typ and KhandaType.NIPAATA not in khanda.typ
        ][0]

        khanda.typ.append(KhandaType.NIPAATA)

        self.push(
            prakriya, prakriya.vartamaana_sthiti, f"{khanda.roopa} इत्यस्य निपातसंज्ञा"
        )


@dataclass
class SutraOneFourFiftyNine(Sutra):
    """उपसर्गाः क्रियायोगे १.४.५९"""

    def __post_init__(self):
        self.define("उपसर्गाः क्रियायोगे १.४.५९")

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

        return True

    def apply(self, prakriya: Prakriya, upasarga: str):
        # pylint: disable=arguments-differ

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

        upa = Upasarga(moola=upasarga, mukhya=khanda)
        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis.insert(khanda_index, upa)

        self.push(prakriya, sthitis, f"{upasarga} इत्यस्य उपसर्गसंज्ञा")

    def call(self, praakriya: Prakriya, upasarga: str):
        """Call the Sutra"""
        if self.check(praakriya):
            self.apply(praakriya, upasarga)


@dataclass
class SutraSixOneFifteen(Sutra):
    """वचिस्वपियजादीनां किति ६.१.१५"""

    def __post_init__(self):
        self.define("वचिस्वपियजादीनां किति ६.१.१५")

    @staticmethod
    def check(prakriya: Prakriya):

        dhaatu = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.DHAATU in khanda.typ
        ]

        if not dhaatu:
            return False

        if len(dhaatu) != 1:
            return False

        dhaatu = dhaatu[0]

        if not (Gana.YAJAADI in dhaatu.typ or dhaatu.upadesha in ["व॒चँ", "ञिष्व॒पँ"]):
            return False

        dhaatu_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.DHAATU in khanda.typ
        ][0]

        nexts = prakriya.vartamaana_sthiti[dhaatu_index + 1]

        if "क्" not in nexts.it:
            return False

        if dhaatu.upadesha == "व॒चँ" and nexts.moola == "क्विप्":
            return False

        return True

    def apply(self, prakriya: Prakriya):

        dhaatu = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.DHAATU in khanda.typ
        ][0]

        vv = get_vinyaasa(dhaatu.roopa)

        for idx, varna in enumerate(vv):
            if varna == "य्":
                vv[idx] = "इ"
            elif varna == "व्":
                vv[idx] = "उ"

        dhaatu.roopa = get_shabda(vv)

        self.push(prakriya, prakriya.vartamaana_sthiti, "सम्प्रसारणम्")

        SutraSixOneOneHundredEight().call(prakriya, dhaatu)


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
class SutraSixOneSixtySeven(Sutra):
    """वेरपृक्तस्य ६.१.६७"""

    def __post_init__(self):
        self.define("वेरपृक्तस्य ६.१.६७")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.PRATYAYA in khanda.typ
        ]

        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        khanda = khanda[0]

        if khanda.roopa != "वि":
            return False


        return True

    def apply(self, prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.PRATYAYA in khanda.typ
        ][0]

        khanda.roopa = " "

        self.push(prakriya, prakriya.vartamaana_sthiti, "अपृक्तविशब्दस्य लोपः")


@dataclass
class SutraSixOneSeventySeven(Sutra):
    """इको यणचि ६.१.७७"""

    def __post_init__(self):
        self.define("इको यणचि ६.१.७७")

    @staticmethod
    def check(prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        ss = prakriya.string
        aa = ss[indices[0]]
        bb = ss[indices[1]]

        if aa in expand_pratyahaara("इक्") and bb in expand_pratyahaara("अच्"):
            return True

        return False

    def apply(self, prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        ss = prakriya.string
        aa = ss[indices[0]]

        if aa in ["इ", "ई"]:
            replacement = "य्"
        elif aa in ["उ", "ऊ"]:
            replacement = "व्"
        elif aa in ["ऋ", "ॠ"]:
            replacement = "र्"
        elif aa == "ऌ":
            replacement = "ल्"

        prakriya.replace_index(indices[0], replacement)

        self.push(prakriya, prakriya.vartamaana_sthiti, "यणादेशः")

    def call(self, prakriya: Prakriya, indices: tuple[int, int]):
        """Call the Sutra"""
        if self.check(prakriya, indices):
            self.apply(prakriya, indices)


@dataclass
class SutraSixOneSeventyEight(Sutra):
    """एचोऽयवायावः ६.१.७८"""

    def __post_init__(self):
        self.define("एचोऽयवायावः ६.१.७८")

    @staticmethod
    def check(prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        ss = prakriya.string
        aa = ss[indices[0]]
        bb = ss[indices[1]]

        if aa in expand_pratyahaara("एच्") and bb in expand_pratyahaara("अच्"):
            return True

        return False

    def apply(self, prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        ss = prakriya.string
        aa = ss[indices[0]]

        if aa == "ए":
            replacement = "अ"
            insertion = "य्"
        elif aa == "ऐ":
            replacement = "आ"
            insertion = "य्"
        elif aa == "ओ":
            replacement = "अ"
            insertion = "व्"
        elif aa == "औ":
            replacement = "आ"
            insertion = "व्"

        prakriya.replace_index(indices[0], replacement)
        prakriya.insert_index(indices[0] + 1, insertion)

        self.push(prakriya, prakriya.vartamaana_sthiti, "यान्तवान्तादेशः")

    def call(self, prakriya: Prakriya, indices: tuple[int, int]):
        """Call the Sutra"""
        if self.check(prakriya, indices):
            self.apply(prakriya, indices)


@dataclass
class SutraSixOneOneHundredOne(Sutra):
    """अकः सवर्णे दीर्घः ६.१.१०१"""

    def __post_init__(self):
        self.define("अकः सवर्णे दीर्घः ६.१.१०१")

    @staticmethod
    def check(prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        ss = prakriya.string
        aa = ss[indices[0]]
        bb = ss[indices[1]]

        if not (aa in expand_pratyahaara("अक्") and bb in expand_pratyahaara("अक्")):
            return False

        if aa in ["अ", "आ"] and bb not in ["अ", "आ"]:
            return False

        if aa in ["इ", "ई"] and bb not in ["इ", "ई"]:
            return False

        if aa in ["उ", "ऊ"] and bb not in ["उ", "ऊ"]:
            return False

        if aa in ["ऋ", "ॠ"] and bb not in ["ऋ", "ॠ"]:
            return False

        return True

    def apply(self, prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        ss = prakriya.string
        aa = ss[indices[0]]

        if aa in ["अ", "आ"]:
            replacement = "आ"
        elif aa in ["इ", "ई"]:
            replacement = "ई"
        elif aa in ["उ", "ऊ"]:
            replacement = "ऊ"
        elif aa in ["ऋ", "ॠ"]:
            replacement = "ॠ"

        prakriya.replace_index(indices[0], replacement)
        prakriya.replace_index(indices[1], " ")

        self.push(prakriya, prakriya.vartamaana_sthiti, "सवर्णदीर्घः")

    def call(self, prakriya: Prakriya, indices: tuple[int, int]):
        """Call the Sutra"""
        if self.check(prakriya, indices):
            self.apply(prakriya, indices)


@dataclass
class SutraSixOneOneHundredEight(Sutra):
    """सम्रसारणाच्च ६.१.१०८"""

    def __post_init__(self):
        self.define("सम्रसारणाच्च ६.१.१०८")

    @staticmethod
    def check(prakriya: Prakriya, khanda: Khanda):
        # pylint: disable=arguments-differ

        flag = False

        for idx, varna in enumerate(get_vinyaasa(khanda.roopa)[:-1]):
            if varna in svara and get_vinyaasa(khanda.roopa)[idx + 1] in svara:
                flag = True
                break

        return flag

    def apply(self, prakriya: Prakriya, khanda: Khanda):
        # pylint: disable=arguments-differ

        vinyaasa = get_vinyaasa(khanda.roopa)
        for idx, varna in enumerate(vinyaasa[:-1]):
            if varna in svara and vinyaasa[idx + 1] in svara:
                index = idx
                break

        vinyaasa.pop(index + 1)
        khanda.roopa = get_shabda(vinyaasa)

        self.push(prakriya, prakriya.vartamaana_sthiti, "सम्रसारणात् पूर्वपरयोरेकादेशः")

    def call(self, prakriya: Prakriya, khanda: Khanda):
        """Call the Sutra"""
        if self.check(prakriya, khanda):
            self.apply(prakriya, khanda)


@dataclass
class SutraSixFourThirtySeven(Sutra):
    """अनुदात्तोपदेशवनतितनोत्यादीनामनुनासिक लोपो झलि क्ङिति ६.४.३७"""

    def __post_init__(self):
        self.define("अनुदात्तोपदेशवनतितनोत्यादीनामनुनासिक लोपो झलि क्ङिति ६.४.३७")

    @staticmethod
    def check(prakriya: Prakriya):

        pratyaya = SutraUtils.get_khanda(
            prakriya, [KhandaType.PRATYAAYA, KhandaType.KRT]
        )

        if not pratyaya:
            return False

        if len(pratyaya) != 1:
            return False

        pratyaya = pratyaya[0][1]

        if "क्" not in pratyaya.it and "ङ्" not in pratyaya.it:
            return False

        anga = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)

        if not anga:
            return False

        if len(anga) != 1:
            return False

        anga = anga[0][1]
        anta = get_vinyaasa(anga.roopa)[-1]

        if anta not in ["ङ्", "ञ्", "ण्", "न्", "म्"]:
            return False

        if (
            KhandaType.ANUDATTOPADESHA not in anga.typ
            and Gana.TANAADI not in anga.typ
            and anga.upadesha != "वनँ"
        ):
            return False

        return True

    def apply(self, prakriya: Prakriya):

        anga = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][1]

        vinyaasa = get_vinyaasa(anga.roopa)
        anga.roopa = get_shabda(vinyaasa[:-1])

        self.push(prakriya, prakriya.vartamaana_sthiti, "अनुनासिक लोपः")


@dataclass
class SutraSixFourFortyEight(Sutra):
    """अतो लोपः ६.४.४८"""

    def __post_init__(self):
        self.define("अतो लोपः ६.४.४८")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)

        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        khanda = khanda[0][1]

        if get_vinyaasa(khanda.roopa)[-1] != "अ":
            return False

        pratyaya = SutraUtils.get_khanda(prakriya, KhandaType.PRATYAAYA)

        if not pratyaya:
            return False

        if KhandaType.AARDHADHAATUKA not in pratyaya[0][1].typ:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][1]

        vinyaasa = get_vinyaasa(khanda.roopa)
        khanda.roopa = get_shabda(vinyaasa[:-1])

        self.push(prakriya, prakriya.vartamaana_sthiti, "अकारलोपः")


@dataclass
class SutraSixFourFiftyOne(Sutra):
    """णेरनिटि ६.४.५१"""

    def __post_init__(self):
        self.define("णेरनिटि ६.४.५१")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.NIJANTA)

        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        khanda = khanda[0][1]

        pratyaya = SutraUtils.get_khanda(prakriya, KhandaType.AARDHADHAATUKA)

        if not pratyaya:
            return False

        pratyaya = pratyaya[0][1]

        if pratyaya.upadesha in ["तृच्", "तृन्", "क्त्वा", "तुमुन्", "क्त", "क्तवतुँ"]:
            return False

        return True

    def apply(self, prakriya):

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.NIJANTA)[0][1]

        vinyaasa = get_vinyaasa(khanda.roopa)
        khanda.roopa = get_shabda(vinyaasa[:-1])

        self.push(prakriya, prakriya.vartamaana_sthiti, "णिच्-प्रत्ययस्य लोपः")


@dataclass
class SutraSixFourSixtyFour(Sutra):
    """आतो लोप इटि च ६.४.६४"""

    def __post_init__(self):
        self.define("आतो लोप इटि च ६.४.६४")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)

        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        khanda = khanda[0][1]

        if get_vinyaasa(khanda.roopa)[-1] != "आ":
            return False

        pratyaya = SutraUtils.get_khanda(prakriya, KhandaType.PRATYAAYA)

        if not pratyaya:
            return False

        if KhandaType.AARDHADHAATUKA not in pratyaya[0][1].typ:
            return False

        if (
            "क्" not in pratyaya[0][1].it
            and "ङ्" not in pratyaya[0][1].it
            and KhandaType.IDAAGAMA not in pratyaya[0][1].typ
        ):
            return False
        
        vinyaasa = get_vinyaasa(pratyaya[0][1].roopa)
        if vinyaasa[0] not in svara:
            return False

        return True
    
    def apply(self, prakriya: Prakriya):

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.DHAATU)[0][1]

        vinyaasa = get_vinyaasa(khanda.roopa)
        khanda.roopa = get_shabda(vinyaasa[:-1])

        self.push(prakriya, prakriya.vartamaana_sthiti, "आकारलोपः")


@dataclass
class SutraSixFourOneHundredFortyThree(Sutra):
    """टेः ६.४.१४३"""

    def __post_init__(self):
        self.define("टेः ६.४.१४३")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.PRATYAAYA in khanda.typ
        ]

        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        khanda = khanda[0]

        if "ड्" not in khanda.it:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.PRATYAAYA in khanda.typ
        ][0]

        khanda_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.PRATYAAYA in khanda.typ
        ][0]

        new_anga = prakriya.vartamaana_sthiti[khanda_index - 1]
        vinyaasa = get_vinyaasa(new_anga.roopa)

        vv = vinyaasa.pop(-1)
        while vv not in svara:
            vv = vinyaasa.pop(-1)

        new_anga.roopa = get_shabda(vinyaasa)

        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis[khanda_index - 1] = new_anga

        self.push(prakriya, sthitis, "टकारस्य टेः प्रत्ययः")


@dataclass
class SutraSixFourOneHundredFortyEight(Sutra):
    """यस्येति च ६.४.१४८"""

    def __post_init__(self):
        self.define("यस्येति च ६.४.१४८")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.BHA)

        if not khanda:
            return False

        if len(khanda) != 1:
            return False

        khanda_index = khanda[0][0]
        khanda = khanda[0][1]

        pratyaya = prakriya.vartamaana_sthiti[khanda_index + 1]

        if (
            KhandaType.TADDHITA not in pratyaya.typ
            and get_vinyaasa(pratyaya.roopa)[0] != "ई"
        ):
            return False

        if get_vinyaasa(khanda.roopa)[-1] not in ["अ", "आ", "इ", "ई"]:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = SutraUtils.get_khanda(prakriya, KhandaType.BHA)[0][1]

        vinyaasa = get_vinyaasa(khanda.roopa)
        khanda.roopa = get_shabda(vinyaasa[:-1])

        self.push(
            prakriya, prakriya.vartamaana_sthiti, f"भसंज्ञकस्य {vinyaasa[-1]}कारलोपः"
        )


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


@dataclass
class SutraSevenTwoOneHundredFifteen(Sutra):
    """अचो ञ्णिति ७.२.११५"""

    def __post_init__(self):
        self.define("अचो ञ्णिति ७.२.११५")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.PRATYAAYA in khanda.typ
            and ("ञ्" in khanda.it or "ण्" in khanda.it)
        ]

        if not khanda:
            return False

        aa = [
            (idx - 1, prakriya.vartamaana_sthiti[idx - 1])
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.PRATYAAYA in khanda.typ
            and ("ञ्" in khanda.it or "ण्" in khanda.it)
            and get_vinyaasa(prakriya.vartamaana_sthiti[idx - 1].roopa)[-1]
            in expand_pratyahaara("अच्")
        ]

        if not aa:
            return False

        aa = aa[0][1]

        if get_vinyaasa(aa.upadesha)[-1] == "अ":
            return False

        return True

    def apply(self, prakriya: Prakriya):

        aa = [
            (idx - 1, prakriya.vartamaana_sthiti[idx - 1])
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.PRATYAAYA in khanda.typ
            and ("ञ्" in khanda.it or "ण्" in khanda.it)
            and get_vinyaasa(prakriya.vartamaana_sthiti[idx - 1].roopa)[-1]
            in expand_pratyahaara("अच्")
        ][0]

        idx, anga = aa

        new_anga = copy.deepcopy(anga)
        vinyaasa = get_vinyaasa(anga.roopa)
        if vinyaasa[-1] in ["इ", "ई"]:
            vinyaasa[-1] = "ऐ"
        elif vinyaasa[-1] in ["उ", "ऊ"]:
            vinyaasa[-1] = "औ"
        elif vinyaasa[-1] in ["ऋ", "ॠ"]:
            vinyaasa[-1] = "आ"
            vinyaasa.append("र्")
        elif vinyaasa[-1] == "ऌ":
            vinyaasa[-1] = "आ"
            vinyaasa.append("ल्")
        elif vinyaasa[-1] == "अ":
            vinyaasa[-1] = "आ"
        elif vinyaasa[-1] == "ए":
            vinyaasa[-1] = "ऐ"
        elif vinyaasa[-1] == "ओ":
            vinyaasa[-1] = "औ"

        new_anga.roopa = get_shabda(vinyaasa)

        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis[idx] = new_anga

        self.push(prakriya, sthitis, "अङ्गवृद्धिः")


@dataclass
class SutraSevenTwoOneHundredSixteen(Sutra):
    """अत उपधायाः ७.२.११६"""

    def __post_init__(self):
        self.define("अत उपधायाः ७.२.११६")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.PRATYAAYA in khanda.typ
            and ("ञ्" in khanda.it or "ण्" in khanda.it)
        ]

        if not khanda:
            return False

        aa = [
            (idx - 1, prakriya.vartamaana_sthiti[idx - 1])
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.PRATYAAYA in khanda.typ
            and ("ञ्" in khanda.it or "ण्" in khanda.it)
            and len(get_vinyaasa(prakriya.vartamaana_sthiti[idx - 1].roopa)) > 1
            and get_vinyaasa(prakriya.vartamaana_sthiti[idx - 1].roopa)[-2] == "अ"
        ]

        if not aa:
            return False

        aa = aa[0][1]

        if get_vinyaasa(aa.upadesha)[-1] == "अ":
            return False

        return True

    def apply(self, prakriya: Prakriya):

        aa = [
            (idx - 1, prakriya.vartamaana_sthiti[idx - 1])
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.PRATYAAYA in khanda.typ
            and ("ञ्" in khanda.it or "ण्" in khanda.it)
            and get_vinyaasa(prakriya.vartamaana_sthiti[idx - 1].roopa)[-2] == "अ"
        ][0]

        idx, anga = aa

        vinyaasa = get_vinyaasa(anga.roopa)
        vinyaasa[-2] = "आ"
        anga.roopa = get_shabda(vinyaasa)

        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis[idx] = anga
        self.push(prakriya, sthitis, "उपधावृद्धिः")


@dataclass
class SutraSevenTwoOneHundredSeventeen(Sutra):
    """तद्धितेष्वचामादेः ७.२.११७"""

    def __post_init__(self):
        self.define("तद्धितेष्वचामादेः ७.२.११७")

    @staticmethod
    def check(prakriya: Prakriya):

        pratyaya = SutraUtils.get_khanda(prakriya, KhandaType.TADDHITA)

        if not pratyaya:
            return False

        if len(pratyaya) != 1:
            return False

        pratyaya_index = pratyaya[0][0]
        pratyaya = pratyaya[0][1]

        anga = prakriya.vartamaana_sthiti[pratyaya_index - 1]

        vinyaasa = get_vinyaasa(anga.roopa)

        for index, varna in enumerate(vinyaasa):
            if varna in svara:
                required_index = index
                break

        if (
            vinyaasa[required_index] in expand_pratyahaara("ऐच्")
            or vinyaasa[required_index] == "आ"
        ):
            return False

        if "ञ्" not in pratyaya.it and "ण्" not in pratyaya.it:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        pratyaya_index = SutraUtils.get_khanda(prakriya, KhandaType.TADDHITA)[0][0]

        anga = prakriya.vartamaana_sthiti[pratyaya_index - 1]

        vinyaasa = get_vinyaasa(anga.roopa)

        for index, varna in enumerate(vinyaasa):
            if varna in svara:
                required_index = index
                break

        if vinyaasa[required_index] == "अ":
            vinyaasa[required_index] = "आ"
        elif vinyaasa[required_index] in ["इ", "ई", "ए"]:
            vinyaasa[required_index] = "ऐ"
        elif vinyaasa[required_index] in ["उ", "ऊ", "ओ"]:
            vinyaasa[required_index] = "औ"
        elif vinyaasa[required_index] in ["ऋ", "ॠ"]:
            vinyaasa[required_index] = "आ"
            vinyaasa.insert(required_index + 1, "र्")
        elif vinyaasa[required_index] == "ऌ":
            vinyaasa[required_index] = "आ"
            vinyaasa.insert(required_index + 1, "ल्")

        anga.roopa = get_shabda(vinyaasa)

        self.push(prakriya, prakriya.vartamaana_sthiti, "आदिस्वरवृद्धिः")


@dataclass
class SutraSevenThreeEightyFour(Sutra):
    """सार्वधातुकार्धधातुकयोः ७.३.८४"""

    def __post_init__(self):
        self.define("सार्वधातुकार्धधातुकयोः ७.३.८४")

    @staticmethod
    def check(prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if (
                KhandaType.AARDHADHAATUKA in khanda.typ
                or KhandaType.SAARVADHAATUKA in khanda.typ
            )
            and KhandaType.KRTITAGUNA not in khanda.typ
        ]

        if not khanda:
            return False

        khanda = khanda[0]

        khanda_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if (
                KhandaType.AARDHADHAATUKA in khanda.typ
                or KhandaType.SAARVADHAATUKA in khanda.typ
            )
            and KhandaType.KRTITAGUNA not in khanda.typ
        ][0]

        anga = prakriya.vartamaana_sthiti[khanda_index - 1]

        if get_vinyaasa(anga.roopa)[-1] not in ["इ", "ई", "उ", "ऊ", "ऋ", "ॠ", "ऌ"]:
            return False

        if get_vinyaasa(anga.upadesha)[-1] == "अ":
            return False

        sutra = SutraOneOneFive()
        sutra(prakriya)
        if sutra.check(prakriya):
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.AARDHADHAATUKA in khanda.typ
            or KhandaType.SAARVADHAATUKA in khanda.typ
        ][0]

        khanda_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.AARDHADHAATUKA in khanda.typ
            or KhandaType.SAARVADHAATUKA in khanda.typ
        ][0]

        anga = prakriya.vartamaana_sthiti[khanda_index - 1]
        vv = get_vinyaasa(anga.roopa)
        if vv[-1] in ["इ", "ई"]:
            vv[-1] = "ए"
        elif vv[-1] in ["उ", "ऊ"]:
            vv[-1] = "ओ"
        elif vv[-1] in ["ऋ", "ॠ"]:
            vv[-1] = "अ"
            vv.append("र्")
        elif vv[-1] == "ऌ":
            vv[-1] = "अ"
            vv.append("ल्")
        anga.roopa = get_shabda(vv)
        khanda.typ.append(KhandaType.KRTITAGUNA)

        self.push(prakriya, prakriya.vartamaana_sthiti, "सार्वधातुकार्धधातुकयोः वृद्धिः")
