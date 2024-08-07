"""Module to define the Sandhi Kaarya"""

from dataclasses import dataclass, field
from utils import Prakriya
import sutra_list


@dataclass
class SandhiKaarya:
    """Class to define the Sutras for the Sandhi Kaarya"""

    prakriya: Prakriya
    sutra_list: list = field(default_factory=list, init=False)

    def __post_init__(self):

        self.sutra_list = [
            sutra_list.SutraSixOneOneHundredOne(),
            sutra_list.SutraSixOneSeventySeven(),
            sutra_list.SutraSixOneSeventyEight(),
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
