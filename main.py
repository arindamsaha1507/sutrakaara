"""Get Dhaatus from a file"""

import yaml

from utils import Prakriya

from dhaatu_prakarana import DhaatuSanjna
from it_prakarana import ItSanjna
from praakrita_kaarya import PraakritaKaaraya


class CreatePrakriya:
    """Class to load Dhaatus from a file"""

    @staticmethod
    def add_dhaatu(pp: Prakriya, number: int):
        """Create all Dhaatus from the file"""

        with open("धातुपाठ_मूल.txt", "r", encoding="utf-8") as ff:
            paatha = ff.read()

        paatha = paatha.split("\n")
        moola = paatha[number]

        DhaatuSanjna(pp, moola)
        ItSanjna(pp)
        PraakritaKaaraya(pp)

    @staticmethod
    def add_upasarga(pp: Prakriya, gana: str, upasarga: str):
        """Add an Upasarga to the Prakriya"""

        pass


def main():
    """Main function"""

    pp = Prakriya()
    CreatePrakriya.add_dhaatu(pp, 1205)

    with open("prakriya.txt", "w", encoding="utf-8") as ff:
        ff.write(pp.__repr__())


if __name__ == "__main__":
    main()
