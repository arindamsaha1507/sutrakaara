"""Upasaraga Kaarya"""

from dataclasses import dataclass, field
from utils import Prakriya
import sutra_list

import it_prakarana


@dataclass
class UpasargaKaarya:
    """Class to define the Sutras for the Upasarga Sanjna"""

    prakriya: Prakriya
    upasarga: str
    sutra_list: list = field(default_factory=list, init=False)

    def __post_init__(self):

        self.sutra_list = [
            sutra_list.SutraOneFourFiftyEight(),
            sutra_list.SutraOneOneThirtySeven(),
            sutra_list.SutraOneTwoFortyFive(),
            sutra_list.SutraOneThreeThree(),
        ]

        sutra = sutra_list.SutraOneFourFiftyNine()
        sutra.call(self.prakriya, self.upasarga)

        self.execute()

        aupadeshika = it_prakarana.UtilFunctions.get_aupadeshika_khanda(
            self.prakriya, return_index=False
        )
        if aupadeshika:
            aupadeshika.aupadeshika = False

        sutra = sutra_list.SutraFiveOneTwo()
        sutra.call(self.prakriya, 1, 1)
        sutra = sutra_list.SutraOneThreeTwo()
        sutra(self.prakriya)

        aupadeshika = it_prakarana.UtilFunctions.get_aupadeshika_khanda(
            self.prakriya, return_index=False
        )
        if aupadeshika:
            aupadeshika.aupadeshika = False

        sutra = sutra_list.SutraTwoFourEightyTwo()
        sutra(self.prakriya)

        sutra = sutra_list.SutraOneFourFourteen()
        sutra(self.prakriya)


    def execute(self):
        """Execute the Sutras"""

        for sutra in self.sutra_list:
            sutra(self.prakriya)
