"""Sutras for Adhyaaya 8"""

from dataclasses import dataclass

from utils import Prakriya, Sutra
from pratyaahaara import expand_pratyahaara


@dataclass
class SutraEightThreeTwentyFour(Sutra):
    """नश्चापदान्तस्य झलि ८.३.२४"""

    def __post_init__(self):
        self.define("नश्चापदान्तस्य झलि ८.३.२४")

    @staticmethod
    def check(prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        ss = prakriya.string
        aa = ss[indices[0]]
        bb = ss[indices[1]]

        if aa not in ["म्", "न्"]:
            return False

        if bb not in expand_pratyahaara("झल्"):
            return False

        return True

    def apply(self, prakriya: Prakriya, indices: tuple[int, int]):
        # pylint: disable=arguments-differ

        prakriya.replace_index(indices[0], "ं")
        self.push(prakriya, prakriya.vartamaana_sthiti, "अनुस्वार अदेशः")


    def call(self, prakriya: Prakriya, indices: tuple[int, int]):
        """Call the Sutra"""
        if self.check(prakriya, indices):
            self.apply(prakriya, indices)
