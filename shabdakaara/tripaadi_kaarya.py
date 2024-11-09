"""Module to define the Sandhi Kaarya"""

from dataclasses import dataclass, field
from utils import Prakriya
import sutra.adhyaaya_eight as sutra_list


@dataclass
class TripaadiKaarya:
    """Class to define the Sutras for the Tripaadi Kaarya"""

    prakriya: Prakriya
    sutra_list: list = field(default_factory=list, init=False)

    def __post_init__(self):

        self.sutra_list = [
            sutra_list.SutraEightTwoThirty(),
            sutra_list.SutraEightTwoTwentyThree(),
            sutra_list.SutraEightTwoSixtySix(),
            sutra_list.SutraEightTwoThirtyNine(),
            sutra_list.SutraEightThreeFifteen(),
            sutra_list.SutraEightThreeTwentyThree(),
            sutra_list.SutraEightThreeTwentyFour(),
            sutra_list.SutraEightFourFiftyEight(),
        ]

        self.execute()

    def execute(self):
        """Execute the Sutras"""

        for sutra in self.sutra_list:

            ss = self.prakriya.string

            print(f"Executing {sutra} with {ss}")

            for ii, varna in enumerate(ss):

                if varna == " ":
                    continue

                if ii == len(ss) - 1:
                    continue

                jj = ii + 1

                while ss[jj] == " " and jj < len(ss) - 1:
                    jj += 1

                sutra.call(self.prakriya, (ii, jj))
