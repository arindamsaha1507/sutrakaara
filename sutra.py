"""Module for Sutras."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import copy
import inspect

from varna import anunaasika_svara, vyanjana, sankhyaa
from vinyaasa import get_vinyaasa, get_shabda

from utils import Prakriya, Khanda, KhandaType, UtilFunctions


@dataclass
class Sutra(ABC):
    """Abstract base class for Sutras"""

    sutra: str = field(init=False)
    adhyaaya: int = field(init=False)
    paada: int = field(init=False)
    kramaanka: int = field(init=False)

    def define(self, line: str):
        """Define the Sutra"""

        def convert_sanskrit_to_int(sanskrit_numeral: str) -> int:
            num_str = "".join(str(sankhyaa.index(char)) for char in sanskrit_numeral)
            return int(num_str)

        parts = line.split(" ")
        self.sutra = " ".join(parts[:-1])

        numbers = parts[-1].split(".")

        if len(numbers) != 3:
            raise ValueError("Invalid Sutra number")

        self.adhyaaya = convert_sanskrit_to_int(numbers[0])
        self.paada = convert_sanskrit_to_int(numbers[1])
        self.kramaanka = convert_sanskrit_to_int(numbers[2])

        if self.adhyaaya < 1 or self.paada < 1 or self.kramaanka < 1:
            raise ValueError("Invalid Sutra number")

        if self.paada > 4:
            raise ValueError("Invalid Paada number")

        if self.adhyaaya > 8:
            raise ValueError("Invalid Adhyaaya number")

    def describe(self) -> str:
        """Return the Sutra number in the format 'Adhyaaya.Paada.Kramaanka'"""

        return f"{self.sutra} {self.adhyaaya}.{self.paada}.{self.kramaanka}"

    def __call__(self, praakriya: Prakriya):
        if self.check(praakriya):
            self.apply(praakriya)

    def push(self, praakriya: Prakriya, sthiti: list[Khanda], message: str):
        """Push the new state to the Prakriya"""

        praakriya.add_to_prakriya(sthiti, self.describe(), message)

    @staticmethod
    @abstractmethod
    def check(prakriya: Prakriya):
        """Check if the Sutra can be applied to the Prakriya"""

    @abstractmethod
    def apply(self, prakriya: Prakriya):
        """Apply the Sutra to the Prakriya"""


class DhaatuSanjna:
    """Class to define the Sutras for the Dhaatu Sanjna"""

    @staticmethod
    def sutra_1_3_1(prakriya: Prakriya, dhaatu):
        """भूवादयो धातवः १.३.१"""

        stack = inspect.stack()
        if stack[1].function == "add_dhaatu":
            prakriya.add_to_prakriya([dhaatu], "भूवादयो धातवः १.३.१", "धातु-संज्ञा")

        return prakriya

    @staticmethod
    def sutra_3_1_32():
        """धात्वादिभ्यः ३.१.३२"""

        raise NotImplementedError("This Sutra is not implemented yet")


class ItSanjna:
    """Class to define the Sutras for the It Sanjna"""

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

            ItLopa.sutra_1_3_9(prakriya, khanda, khanda_index, indices)

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

            ItLopa.sutra_1_3_9(prakriya, khanda, khanda_index, indices)

    @dataclass
    class SutraOneThreeThree(Sutra):
        """हलन्त्यम् १.३.३"""

        def __post_init__(self):
            print("SutraOneThreeThree")
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

            ItLopa.sutra_1_3_9(prakriya, khanda, khanda_index, indices)

    @dataclass
    class SutraOneThreeFour(Sutra):
        """आदिर्ञिटुडवः १.३.४"""

        def __post_init__(self):
            self.define("आदिर्ञिटुडवः १.३.४")

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

            ItLopa.sutra_1_3_9(prakriya, khanda, khanda_index, indices)

    # @staticmethod
    # def sutra_1_3_4(prakriya: Prakriya):
    #     """आदिर्ञिटुडवः १.३.४"""

    #     aupaadheshika_khanda = [
    #         khanda for khanda in prakriya.vartamaana_sthiti if khanda.aupadeshika
    #     ]

    #     aupaadheshika_khanda_index = [
    #         ii
    #         for ii, khanda in enumerate(prakriya.vartamaana_sthiti)
    #         if khanda.aupadeshika
    #     ]

    #     if not aupaadheshika_khanda:
    #         return

    #     aupaadheshika_khanda = aupaadheshika_khanda[0]

    #     vinyaasa = get_vinyaasa(aupaadheshika_khanda.roopa)

    #     if get_shabda(vinyaasa[:2]) in ["ञि", "टु", "डु"]:
    #         indices = [0, 1]
    #         aupaadheshika_khanda.it.extend([get_shabda(vinyaasa[:2])])

    #         if vinyaasa[2] not in vyanjana and vinyaasa[2] not in anunaasika_svara:
    #             indices.append(2)
    #             if vinyaasa[2] == "॒":
    #                 aupaadheshika_khanda.anudaatta_it = True
    #             else:
    #                 aupaadheshika_khanda.svarita_it = True

    #         prakriya.add_to_prakriya(
    #             prakriya.vartamaana_sthiti,
    #             "आदिर्ञिटुडवः १.३.४",
    #             f"{get_shabda(vinyaasa[:2])} इत्",
    #         )

    #         ItLopa.sutra_1_3_9(
    #             prakriya, aupaadheshika_khanda, aupaadheshika_khanda_index[0], indices
    #         )


class ItLopa:
    """Class to define the Sutras for the It Lopa"""

    @staticmethod
    def sutra_1_3_9(
        prakriya: Prakriya, khanda: Khanda, khanda_index: int, indices: list[int]
    ):
        """तस्य लोपः १.३.९"""

        print(indices)

        vinyaasa = get_vinyaasa(khanda.roopa)

        for index in sorted(indices, reverse=True):
            del vinyaasa[index]

        khanda.roopa = get_shabda(vinyaasa)

        sthiti = copy.deepcopy(prakriya.vartamaana_sthiti)
        sthiti[khanda_index] = khanda

        prakriya.add_to_prakriya(
            sthiti,
            "तस्य लोपः १.३.९",
            "इत्-लोपः",
        )
