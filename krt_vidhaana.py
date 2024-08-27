"""Module for the Krt Vidhaana."""

from dataclasses import dataclass, field

from sutra import adhyaaya_four, adhyaaya_two, sutra_list
from utils import Prakriya, Krdartha, KhandaType
from praatipadika import Praatipadika
import sutra.adhyaaya_three as adhyaaya_three

import it_prakarana


@dataclass
class KrtVidhaana:
    """Class to define the Sutras for the Krt Vidhaana"""

    prakriya: Prakriya
    krt: str
    artha: Krdartha
    upapada: str = None
    vibhakti: int = None
    vachana: int = None
    sutra_list: list = field(default_factory=list, init=False)

    def __post_init__(self):

        self.sutra_list = [
            
            # Anaadyarthe
            adhyaaya_three.SutraThreeTwoOne(),
            adhyaaya_three.SutraThreeTwoThree(),

            # Bhootaarthe
            adhyaaya_three.SutraThreeTwoOneHundredTwo(),
            # Bhaavaarthe
            adhyaaya_three.SutraThreeThreeFiftySeven(),
            adhyaaya_three.SutraThreeThreeEighteen(),
        ]

        if self.artha == Krdartha.ANAADI:

            if self.upapada is None:
                raise ValueError("Upapada is required for Anaadi Krt")
            if self.vibhakti is None:
                raise ValueError("Vibhakti is required for Anaadi Krt")
            if self.vachana is None:
                raise ValueError("Vachana is required for Anaadi Krt")
            
            if self.vibhakti == 2:
                self.vibhakti = 6

            praatipadika = Praatipadika(moola=self.upapada)
            self.prakriya.vartamaana_sthiti.insert(0, praatipadika)
            sutra = adhyaaya_four.SutraFourOneTwo()
            sutra.call(self.prakriya, self.vibhakti, self.vachana)

            it_prakarana.ItSanjna(self.prakriya)
            aupadeshika = it_prakarana.UtilFunctions.get_aupadeshika_khanda(
                self.prakriya, return_index=False
            )
            if aupadeshika:
                aupadeshika.aupadeshika = False

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


    def execute(self):
        """Execute the Sutras"""

        for sutra in self.sutra_list:
            sutra.call(self.prakriya, self.krt, self.artha)

        if KhandaType.KRT not in self.prakriya.vartamaana_sthiti[-1].typ:
            raise ValueError("Krt not added to the Prakriya")
