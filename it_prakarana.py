"""Module for Sutras."""

from dataclasses import dataclass, field
import inspect

from utils import Prakriya
import sutra_list


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


@dataclass
class ItSanjna:
    """Class to define the Sutras for the It Sanjna"""

    prakriya: Prakriya
    sutra_list: list = field(default_factory=list, init=False)

    def __post_init__(self):
        self.sutra_list = [
            sutra_list.VartikaOneThreeTwo(),
            sutra_list.SutraOneThreeThree(),
            sutra_list.SutraOneThreeTwo(),
            sutra_list.SutraOneThreeFive(),
        ]

        self.execute()

    def execute(self):
        """Execute the Sutras"""

        for sutra in self.sutra_list:
            sutra(self.prakriya)
