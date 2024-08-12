"""All sutras"""

from dataclasses import dataclass
import copy

from utils import Prakriya, UtilFunctions, Sutra, KhandaType, Khanda, Krdartha, Unaadi
from varna import anunaasika_svara, vyanjana, svara
from vinyaasa import get_vinyaasa, get_shabda
from pratyaahaara import expand_pratyahaara

from aagama import Aagama
from dhaatu import Dhaatu, Gana
from krt import Krt
from pada import Pada
from sup import Sup
from upasarga import Upasarga


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

        anta_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.SUP in khanda.typ or KhandaType.TIN in khanda.typ
        ][0]

        aadi_index = anta_index - 1

        while aadi_index >= 0:
            if (
                KhandaType.PRAATIPADIKA in prakriya.vartamaana_sthiti[aadi_index].typ
                or KhandaType.DHAATU in prakriya.vartamaana_sthiti[aadi_index].typ
            ):
                break
            aadi_index -= 1

        if aadi_index < 0:
            raise ValueError("No Aadi found")

        vinyaasa = []
        typs = [KhandaType.PADA]
        for idx in range(aadi_index, anta_index):
            vinyaasa.extend(get_vinyaasa(prakriya.vartamaana_sthiti[idx].roopa))
            if KhandaType.KRT in prakriya.vartamaana_sthiti[idx].typ:
                typs.append(KhandaType.KRIDANTA)
            if KhandaType.TADDHITA in prakriya.vartamaana_sthiti[idx].typ:
                typs.append(KhandaType.TADDHITAANTA)

        if KhandaType.SUP in prakriya.vartamaana_sthiti[anta_index].typ:
            typs.append(KhandaType.SUBANTA)
        else:
            typs.append(KhandaType.TINGANTA)

        shabda = get_shabda(vinyaasa)
        padam = Pada(moola=shabda, names=typs)

        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis.insert(aadi_index, padam)

        for idx in range(aadi_index + 1, anta_index + 2):
            sthitis.pop(aadi_index + 1)

        self.push(prakriya, sthitis, f"{padam.roopa} इत्यस्य पदसंज्ञा")


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

        if len(khanda) != 1:
            khanda = khanda[-1]
        else:
            khanda = khanda[0]

        khanda_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.AVYAYA in khanda.typ
        ][0]

        if KhandaType.SUP not in prakriya.vartamaana_sthiti[khanda_index + 1].typ:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.AVYAYA in khanda.typ
        ][-1]

        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis[khanda_index + 1].roopa = ""

        self.push(prakriya, sthitis, "सुब्लुक्")


@dataclass
class SutraThreeThreeEighteen(Sutra):
    """भावे ३.३.१८"""

    def __post_init__(self):
        self.define("भावे ३.३.१८")

    @staticmethod
    def check(prakriya: Prakriya, artha: Krdartha, pratyaya: str):
        # pylint: disable=arguments-differ

        if artha != Krdartha.BHAAVA:
            return False

        if pratyaya != "घञ्":
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

        sutra = SutraThreeThreeTwentyOne()
        sutra.call(prakriya, pratyaya, artha)
        if sutra.check(prakriya, artha, pratyaya):
            return False

        return True

    def apply(self, prakriya: Prakriya, artha: Krdartha, pratyaya: str):
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

        if artha != Krdartha.BHAAVA:
            return False

        if pratyaya != "घञ्":
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

        if khanda.upadesha != "इ॒ङ्":
            return False

        return True

    def apply(self, prakriya: Prakriya, artha: Krdartha, pratyaya: str):
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

        if artha != Krdartha.BHAAVA:
            return False

        if pratyaya != "अप्":
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

        if get_vinyaasa(khanda[0].roopa)[-1] not in ["ॠ", "उ", "ऊ"]:
            return False

        return True

    def apply(self, prakriya: Prakriya, artha: Krdartha, pratyaya: str):
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


@dataclass
class SutraFiveOneTwo(Sutra):
    """स्वौजसमौट्छष्टाभ्याम्भिस्ङेभ्याम्भ्यस्ङसिभ्याम्भ्यस्ङसोसाङ्ङ्योस्सुप् ५.१.२"""

    def __post_init__(self):
        self.define("स्वौजसमौट्छष्टाभ्याम्भिस्ङेभ्याम्भ्यस्ङसिभ्याम्भ्यस्ङसोसाङ्ङ्योस्सुप् ५.१.२")

    @staticmethod
    def check(prakriya: Prakriya):
        khanda = [
            khanda
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.PRAATIPADIKA in khanda.typ
            and KhandaType.SUP not in prakriya.vartamaana_sthiti[idx + 1].typ
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
            and KhandaType.SUP not in prakriya.vartamaana_sthiti[idx + 1].typ
        ][0]

        khanda_index = [
            idx
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.PRAATIPADIKA in khanda.typ
            and KhandaType.SUP not in prakriya.vartamaana_sthiti[idx + 1].typ
        ][0]

        sup = Sup(index=number, mukhya=khanda)

        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis.insert(khanda_index + 1, sup)

        self.push(prakriya, sthitis, "सुब्विधानम्")

    def call(self, praakriya: Prakriya, vibhakti: int, vachana: int):
        """Call the Sutra"""
        if self.check(praakriya):
            self.apply(praakriya, vibhakti, vachana)


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

        varnas = get_vinyaasa(khanda.roopa)
        if varnas[0] != "व्":
            return False

        if len(varnas) != 1:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        khanda = [
            khanda
            for khanda in prakriya.vartamaana_sthiti
            if KhandaType.PRATYAYA in khanda.typ
        ][0]

        khanda.roopa = " "

        # sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        # sthitis[khanda_index] = khanda

        self.push(prakriya, prakriya.vartamaana_sthiti, "अपृक्तवकारस्य लोपः")
        # self.push(prakriya, sthitis, "अपृक्तवकारस्य लोपः")


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
            in ["इ", "उ", "ऋ", "ऌ"]
        ]

        if not aa:
            return False

        return True

    def apply(self, prakriya: Prakriya):

        aa = [
            (idx - 1, prakriya.vartamaana_sthiti[idx - 1])
            for idx, khanda in enumerate(prakriya.vartamaana_sthiti)
            if KhandaType.PRATYAAYA in khanda.typ
            and ("ञ्" in khanda.it or "ण्" in khanda.it)
            and get_vinyaasa(prakriya.vartamaana_sthiti[idx - 1].roopa)[-1]
            in ["इ", "उ", "ऋ", "ऌ"]
        ][0]

        idx, anga = aa

        new_anga = copy.deepcopy(anga)
        vinyaasa = get_vinyaasa(anga.roopa)
        if vinyaasa[-1] == "इ":
            vinyaasa[-1] = "ऐ"
        elif vinyaasa[-1] == "उ":
            vinyaasa[-1] = "औ"
        elif vinyaasa[-1] == "ऋ":
            vinyaasa[-1] = "आ"
            vinyaasa.append("र्")
        elif vinyaasa[-1] == "ऌ":
            vinyaasa[-1] = "आ"
            vinyaasa.append("ल्")

        new_anga.roopa = get_shabda(vinyaasa)

        sthitis = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthitis[idx] = new_anga

        self.push(prakriya, sthitis, "अङ्गवृद्धिः")


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

        pratyaya = Krt(moola="क्विप्", mukhya=khanda, uchchaarana=[2])
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

        pratyaya.remove_uchchaarana()

        ucchaarana = get_vinyaasa(pratyaya.moola)[pratyaya.uchchaarana[0]]

        prakriya.add_to_prakriya(sthitis, "-", f"{ucchaarana}कार उच्चारणार्थम्")

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
