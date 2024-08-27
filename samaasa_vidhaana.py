"""Module for samaasa vidhaana"""

from dataclasses import dataclass, field

from sutra import adhyaaya_two, sutra_list
from utils import Prakriya, SamaasaType

from praatipadika import Praatipadika
from sup import Sup

import it_prakarana


@dataclass
class SamaasaVidhaana:
    """Class to define the Sutras for the Samaasa Vidhaana"""

    prakriya: Prakriya
    praatipadikas: tuple[str, str]
    samaasa_type: SamaasaType
    sutra_list: list = field(default_factory=list, init=False)

    def __post_init__(self):

        if self.samaasa_type == SamaasaType.DWANDWA:

            pr1 = Praatipadika(moola=self.praatipadikas[0])
            pr2 = Praatipadika(moola=self.praatipadikas[1])
            sup1 = Sup(index=0, mukhya=pr1)
            sup2 = Sup(index=0, mukhya=pr2)

            self.prakriya.add_to_prakriya([pr1, sup1], "-", "प्रातिपदिकम्")

            it_prakarana.ItSanjna(self.prakriya)

            self.prakriya.vartamaana_sthiti.append(pr2)
            self.prakriya.vartamaana_sthiti.append(sup2)

            self.prakriya.add_to_prakriya(
                self.prakriya.vartamaana_sthiti, "-", "प्रातिपदिकम्"
            )

            it_prakarana.ItSanjna(self.prakriya)

            sutra = sutra_list.SutraOneFourFourteen()
            sutra(self.prakriya)
            sutra(self.prakriya)

            sutra = sutra_list.SutraOneTwoFortySix()
            sutra(self.prakriya)

            sutra = adhyaaya_two.SutraTwoFourSeventyOne()
            sutra(self.prakriya)

