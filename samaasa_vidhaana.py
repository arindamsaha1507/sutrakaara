"""Module for samaasa vidhaana"""

from dataclasses import dataclass, field

from sutra import adhyaaya_two, sutra_list
from utils import KhandaType, Prakriya, SamaasaType

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

        pr1 = Praatipadika(moola=self.praatipadikas[0])
        pr2 = Praatipadika(moola=self.praatipadikas[1])

        pr1.typ.append(KhandaType.SAMAASA)
        pr2.typ.append(KhandaType.SAMAASA)

        print(f"pr1: {pr1}")
        print(f"pr2: {pr2}")

        if self.samaasa_type == SamaasaType.DWANDWA:
            pr1.typ.append(KhandaType.DWANDWA)
            pr2.typ.append(KhandaType.DWANDWA)
            sup1 = Sup(index=0, mukhya=pr1)
        elif self.samaasa_type == SamaasaType.KARMADHAARAYA:
            pr1.typ.append(KhandaType.KARMADHAARAYA)
            pr1.typ.append(KhandaType.TATPURUSHA)
            pr2.typ.append(KhandaType.KARMADHAARAYA)
            pr2.typ.append(KhandaType.TATPURUSHA)
            sup1 = Sup(index=0, mukhya=pr1)
        else:
            raise NotImplementedError("Only Dwandwa and Karmadhaaraya are supported")

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
