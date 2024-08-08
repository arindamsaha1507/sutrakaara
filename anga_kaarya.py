"""Module for the Anga Kaarya."""

from dataclasses import dataclass, field

from utils import Prakriya
import sutra_list


@dataclass
class AngaKaarya:
    """Class to define the Sutras for the Anga Kaarya"""

    prakriya: Prakriya
    sutra_list: list = field(default_factory=list, init=False)

    def __post_init__(self):

        self.sutra_list = [

            sutra_list.SutraSixOneSixtySeven(),

            sutra_list.SutraSevenTwoOneHundredFifteen(),
            sutra_list.SutraSixFourOneHundredFortyThree(),
            sutra_list.SutraSixOneFifteen(),
        ]

        self.execute()

    def execute(self):
        """Execute the Sutras"""

        for sutra in self.sutra_list:
            sutra(self.prakriya)