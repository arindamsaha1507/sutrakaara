"""Praakrita Kaaryaa"""

from dataclasses import dataclass, field
from utils import Prakriya
import sutra_list
from vinyaasa import get_vinyaasa


def remove_svara_markers(prakriya: Prakriya):
    """Remove the Svara markers from the Moola"""

    for khanda in prakriya.vartamaana_sthiti:

        if "॒" not in get_vinyaasa(khanda.roopa) and "॑" not in get_vinyaasa(
            khanda.roopa
        ):
            continue

        khanda.roopa = khanda.roopa.replace("॒", "")
        khanda.roopa = khanda.roopa.replace("॑", "")

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
        ]

        self.execute()
        remove_svara_markers(self.prakriya)

    def execute(self):
        """Execute the Sutras"""

        for sutra in self.sutra_list:
            sutra(self.prakriya)
