"""Praakrita Kaaryaa"""

from dataclasses import dataclass, field
from utils import Prakriya, KhandaType
import sutra.sutra_list as sutra_list
import sutra.adhyaaya_three as adhyaaya_three
from vinyaasa import get_vinyaasa

import it_prakarana
import anga_kaarya


def remove_svara_markers(prakriya: Prakriya):
    """Remove the Svara markers from the Moola"""

    for khanda in prakriya.vartamaana_sthiti:

        if "॒" not in get_vinyaasa(khanda.roopa) and "॑" not in get_vinyaasa(
            khanda.roopa
        ):
            continue

        khanda.roopa = khanda.roopa.replace("॒", "")
        khanda.roopa = khanda.roopa.replace("॑", "")

        khanda.typ.append(KhandaType.ANUDATTOPADESHA)

        prakriya.add_to_prakriya(prakriya.vartamaana_sthiti, "-", "स्वरमात्राः अपाकृताः")


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
            adhyaaya_three.SutraThreeOneTwentyFive(),
        ]

        self.execute()
        remove_svara_markers(self.prakriya)

        if len(self.prakriya.vartamaana_sthiti) > 1:
            it_prakarana.ItSanjna(self.prakriya)
            anga_kaarya.AngaKaarya(self.prakriya)
            dhaatu = self.prakriya.vartamaana_sthiti[0]
            self.prakriya.combine()
            dhaatu.roopa = self.prakriya.final
            dhaatu.typ.append(KhandaType.NIJANTA)
            self.prakriya.vartamaana_sthiti = [dhaatu]
            self.prakriya.add_to_prakriya(
                self.prakriya.vartamaana_sthiti, "-", "वर्णमेलनम्"
            )

    def execute(self):
        """Execute the Sutras"""

        for sutra in self.sutra_list:
            sutra(self.prakriya)
