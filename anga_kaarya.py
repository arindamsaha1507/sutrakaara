"""Module for the Anga Kaarya."""

from dataclasses import dataclass, field

from utils import Prakriya
import sutra.sutra_list as sutra_list
import sutra.adhyaaya_three as adhyaaya_three


@dataclass
class AngaKaarya:
    """Class to define the Sutras for the Anga Kaarya"""

    prakriya: Prakriya
    sutra_list: list = field(default_factory=list, init=False)

    def __post_init__(self):

        self.sutra_list = [

            adhyaaya_three.SutraThreeFourOneHundredFourteen(),
            sutra_list.SutraOneFourEighteen(),

            sutra_list.SutraSixFourFortyEight(),
            sutra_list.SutraSixFourFiftyOne(),

            sutra_list.SutraSevenTwoOneHundredFifteen(),
            sutra_list.SutraSevenTwoOneHundredSixteen(),
            sutra_list.SutraSevenTwoOneHundredSeventeen(),

            sutra_list.SutraSixFourOneHundredFortyThree(),
            sutra_list.SutraSixFourOneHundredFortyEight(),

            sutra_list.SutraSixFourThirtySeven(),

            sutra_list.SutraSixOneFifteen(),

            sutra_list.SutraSevenThreeEightyFour(),

            sutra_list.SutraSixOneSixtySeven(),

        ]

        self.execute()

    def execute(self):
        """Execute the Sutras"""

        for sutra in self.sutra_list:
            sutra(self.prakriya)