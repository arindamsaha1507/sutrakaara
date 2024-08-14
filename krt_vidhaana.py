"""Module for the Krt Vidhaana."""

from dataclasses import dataclass, field

from utils import Prakriya, Krdartha, KhandaType
import sutra.adhyaaya_three as adhyaaya_three

import it_prakarana


@dataclass
class KrtVidhaana:
    """Class to define the Sutras for the Krt Vidhaana"""

    prakriya: Prakriya
    krt: str
    artha: Krdartha
    sutra_list: list = field(default_factory=list, init=False)

    def __post_init__(self):

        self.sutra_list = [

            # Bhootaarthe
            adhyaaya_three.SutraThreeTwoOneHundredTwo(),

            # Bhaavaarthe
            adhyaaya_three.SutraThreeThreeFiftySeven(),
            adhyaaya_three.SutraThreeThreeEighteen(),
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
            sutra.call(self.prakriya, self.krt, self.artha)

        if KhandaType.KRT not in self.prakriya.vartamaana_sthiti[-1].typ:
            raise ValueError("Krt not added to the Prakriya")