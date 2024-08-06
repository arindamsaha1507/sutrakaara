"""Get Dhaatus from a file"""

import yaml

from utils import Prakriya

from dhaatu_prakarana import DhaatuSanjna
from it_prakarana import ItSanjna
from praakrita_kaarya import PraakritaKaaraya
from upasarga_kaarya import UpasargaKaarya


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
    def add_upasarga(pp: Prakriya, upasarga: str):
        """Add an Upasarga to the Prakriya"""

        with open("गणपाठ.yml", "r", encoding="utf-8") as ff:
            upasarga_list = yaml.safe_load(ff)["प्रादि"]

        if upasarga not in upasarga_list:
            raise ValueError(f"Upasarga {upasarga} not found in the file")

        UpasargaKaarya(pp, upasarga)


def main():
    """Main function"""

    pp = Prakriya()
    CreatePrakriya.add_dhaatu(pp, 1205)
    CreatePrakriya.add_upasarga(pp, "सु")
    CreatePrakriya.add_upasarga(pp, "आङ्")
    CreatePrakriya.add_upasarga(pp, "अधि")

    with open("prakriya.txt", "w", encoding="utf-8") as ff:
        ff.write(pp.__repr__())


if __name__ == "__main__":
    main()
