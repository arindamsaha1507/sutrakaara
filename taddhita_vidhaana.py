"""Module for the Taddhita Vidhaana."""

from dataclasses import dataclass, field

from utils import Prakriya, Taddhitaartha, KhandaType
import sutra.adhyaaya_four as adhyaaya_four

import it_prakarana


@dataclass
class TaddhitaVidhaana:
    """Class to define the Sutras for the Krt Vidhaana"""

    prakriya: Prakriya
    taddhita: str
    artha: Taddhitaartha
    sutra_list: list = field(default_factory=list, init=False)

    def __post_init__(self):

        self.sutra_list = [

            adhyaaya_four.SutraFourOneEightyThree(),

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
            sutra.call(self.prakriya, self.taddhita, self.artha)

        if KhandaType.TADDHITA not in self.prakriya.vartamaana_sthiti[-1].typ:
            raise ValueError("Krt not added to the Prakriya")