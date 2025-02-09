"""Module for Sutras."""

from dataclasses import dataclass, field

from utils import Prakriya, UtilFunctions
import sutra.sutra_list as sutra_list


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
            sutra_list.SutraOneThreeSeven(),
            sutra_list.SutraOneThreeEight(),
        ]

        self.execute()
        self.remove_aupadeshika_sanjna()

    def execute(self):
        """Execute the Sutras"""

        for sutra in self.sutra_list:
            sutra(self.prakriya)

    def remove_aupadeshika_sanjna(self):
        """Remove the Aupadeshika Sanjna"""

        aupadeshika = UtilFunctions.get_aupadeshika_khanda(self.prakriya, return_index=False)
        aupadeshika.aupadeshika = False