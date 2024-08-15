"""Module for the Krt Vidhaana."""

from dataclasses import dataclass, field

from utils import Prakriya
import sutra.sutra_list as sutra_list

import it_prakarana


@dataclass
class UnaadiVidhaana:
    """Class to define the Sutras for the Krt Vidhaana"""

    prakriya: Prakriya
    unaadi: str
    sutra_list: list = field(default_factory=list, init=False)

    def __post_init__(self):

        self.sutra_list = [
            sutra_list.UnaadiTwoFiftyEight(),
            sutra_list.UnaadiTwoSixtySeven(),
            sutra_list.UnaadiFourOneHundredSeventySeven(),
            sutra_list.UnaadiFourOneHundredEightyEight(),
        ]

        self.execute()

        it_prakarana.ItSanjna(self.prakriya)

        aupadeshika = it_prakarana.UtilFunctions.get_aupadeshika_khanda(
            self.prakriya, return_index=False
        )
        if aupadeshika:
            aupadeshika.aupadeshika = False

    def execute(self):
        """Execute the Sutras"""

        for sutra in self.sutra_list:
            sutra.call(self.prakriya, self.unaadi)
