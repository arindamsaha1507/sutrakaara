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
            sutra_list.SutraEightTwoSixtySix(),
            sutra_list.SutraEightTwoThirtyNine(),
            sutra_list.SutraEightThreeFifteen(),
            sutra_list.SutraEightThreeTwentyFour(),
        ]

        self.execute()

    def execute(self):
        """Execute the Sutras"""

        ss = self.prakriya.string

        for ii, varna in enumerate(ss):

            if varna == " ":
                continue

            if ii == len(ss) - 1:
                continue

            jj = ii + 1

            if ss[jj] == " ":
                jj += 1

            for sutra in self.sutra_list:
                sutra.call(self.prakriya, (ii, jj))
