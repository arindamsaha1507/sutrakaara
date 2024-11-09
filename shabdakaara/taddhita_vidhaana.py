"""Module for the Taddhita Vidhaana."""

from dataclasses import dataclass, field

from utils import Prakriya, Taddhitaartha, KhandaType
import sutra.adhyaaya_two as adhyaaya_two
import sutra.adhyaaya_four as adhyaaya_four
import sutra.sutra_list as sutra_list

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
            adhyaaya_four.SutraFourOneNinetyFive(),
        ]

        vibhakti = int(self.artha.value.split(" ")[-2])
        vachana = int(self.artha.value.split(" ")[-1])

        sutra = adhyaaya_four.SutraFourOneTwo()
        sutra.call(self.prakriya, vibhakti, vachana)

        it_prakarana.ItSanjna(self.prakriya)

        sutra = sutra_list.SutraOneFourFourteen()
        sutra(self.prakriya)

        self.execute()

        it_prakarana.ItSanjna(self.prakriya)

        aupadeshika = it_prakarana.UtilFunctions.get_aupadeshika_khanda(
            self.prakriya, return_index=False
        )
        if aupadeshika:
            aupadeshika.aupadeshika = False

        sutra = sutra_list.SutraOneTwoFortySix()
        sutra(self.prakriya)

        sutra = adhyaaya_two.SutraTwoFourSeventyOne()
        sutra(self.prakriya)

        # print(self.prakriya)

    def execute(self):
        """Execute the Sutras"""

        for sutra in self.sutra_list:
            sutra.call(self.prakriya, self.taddhita, self.artha)

        if KhandaType.TADDHITA not in self.prakriya.vartamaana_sthiti[-1].typ:
            print(self.prakriya)
            raise ValueError("Taddhita not added to the Prakriya")
