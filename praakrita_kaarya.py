from dataclasses import dataclass, field
from utils import Prakriya
import sutra_list


@dataclass
class PraakritaKaaraya:
    """Class to define the Sutras for the It Sanjna"""

    prakriya: Prakriya
    sutra_list: list = field(default_factory=list, init=False)

    def __post_init__(self):
        self.sutra_list = [
            sutra_list.SutraSixOneSixtyFour(),
            sutra_list.SutraSevenOneFiftyEight(),
            sutra_list.SutraOneThreeThree(),
            sutra_list.SutraOneOneFortySix(),
            sutra_list.SutraOneOneFortySeven(),
        ]

        self.execute()

    def execute(self):
        """Execute the Sutras"""

        for sutra in self.sutra_list:
            sutra(self.prakriya)
