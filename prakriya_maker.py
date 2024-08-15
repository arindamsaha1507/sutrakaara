"""Get Dhaatus from a file"""

import yaml

from utils import Prakriya, Krdartha

from anga_kaarya import AngaKaarya
from dhaatu_prakarana import DhaatuSanjna
from it_prakarana import ItSanjna
from krt_vidhaana import KrtVidhaana
from praakrita_kaarya import PraakritaKaaraya
from sandhi_kaarya import SandhiKaarya
from tripaadi_kaarya import TripaadiKaarya
from upasarga_kaarya import UpasargaKaarya
from unaadi_vidhaana import UnaadiVidhaana


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

    @staticmethod
    def add_krt(pp: Prakriya, krt: str, artha: Krdartha):
        """Add a Krt to the Prakriya"""

        KrtVidhaana(pp, krt, artha)
        AngaKaarya(pp)
        SandhiKaarya(pp)
        TripaadiKaarya(pp)

    @staticmethod
    def add_unaadi(pp: Prakriya, krt: str):
        """Add a Krt to the Prakriya"""

        UnaadiVidhaana(pp, krt)
        AngaKaarya(pp)
        SandhiKaarya(pp)
        TripaadiKaarya(pp)


def main():
    """Main function"""

    pp = Prakriya()

    CreatePrakriya.add_dhaatu(pp, 1215)
    CreatePrakriya.add_unaadi(pp, "डुम्सुँन्")

    # CreatePrakriya.add_dhaatu(pp, 988)
    # CreatePrakriya.add_upasarga(pp, "नि")
    # CreatePrakriya.add_krt(pp, "क्त", Krdartha.BHOOTA)

    # CreatePrakriya.add_dhaatu(pp, 0)
    # CreatePrakriya.add_krt(pp, "घञ्", Krdartha.BHAAVA)

    # CreatePrakriya.add_dhaatu(pp, 1704)
    # CreatePrakriya.add_krt(pp, "अप्", Krdartha.BHAAVA)

    # CreatePrakriya.add_dhaatu(pp, 1435)
    # CreatePrakriya.add_krt(pp, "अप्", Krdartha.BHAAVA)

    # CreatePrakriya.add_dhaatu(pp, 1222)
    # CreatePrakriya.add_unaadi(pp, "क्विप्")

    # CreatePrakriya.add_dhaatu(pp, 2095)
    # CreatePrakriya.add_unaadi(pp, "असुन्")


    # CreatePrakriya.add_dhaatu(pp, 1136)
    # CreatePrakriya.add_unaadi(pp, "डो")

    # CreatePrakriya.add_dhaatu(pp, 1205)
    # CreatePrakriya.add_upasarga(pp, "सु")
    # CreatePrakriya.add_upasarga(pp, "आङ्")
    # CreatePrakriya.add_upasarga(pp, "अधि")
    # CreatePrakriya.add_krt(pp, "घञ्", Krdartha.BHAAVA)

    pp.combine()

    with open("prakriya.txt", "w", encoding="utf-8") as ff:
        ff.write(str(pp))
        ff.write("\n")
        ff.write(pp.final)


if __name__ == "__main__":
    main()
