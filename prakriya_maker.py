"""Get Dhaatus from a file"""

import yaml

from utils import Prakriya, Krdartha, Taddhitaartha, SamaasaType

from anga_kaarya import AngaKaarya
from dhaatu_prakarana import DhaatuSanjna
from it_prakarana import ItSanjna
from krt_vidhaana import KrtVidhaana
from praakrita_kaarya import PraakritaKaaraya
from praatipadika import Praatipadika
from sandhi_kaarya import SandhiKaarya
from samaasa_vidhaana import SamaasaVidhaana
from taddhita_vidhaana import TaddhitaVidhaana
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
    def add_krt(
        pp: Prakriya,
        krt: str,
        artha: Krdartha,
        upapada: str = None,
        vibhakti: int = None,
        vachana: int = None,
    ):
        """Add a Krt to the Prakriya"""

        if artha == Krdartha.ANAADI:
            KrtVidhaana(pp, krt, artha, upapada, vibhakti, vachana)
        else:
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

    @staticmethod
    def add_praatipadika(pp: Prakriya, praatipadika: str):
        """Add a Krt to the Prakriya"""

        sthiti = [Praatipadika(moola=praatipadika)]
        pp.add_to_prakriya(sthiti, "-", "प्रातिपदिकम्")

    @staticmethod
    def add_taddhita(pp: Prakriya, taddhita: str, artha: Taddhitaartha):
        """Add a Taddhita to the Prakriya"""

        TaddhitaVidhaana(pp, taddhita, artha)
        AngaKaarya(pp)
        SandhiKaarya(pp)
        TripaadiKaarya(pp)

    @staticmethod
    def add_samasa(pp: Prakriya, praatipadikas: tuple[str, str], samaasa_type: SamaasaType):
        """Add a Samasa to the Prakriya"""

        SamaasaVidhaana(pp, praatipadikas, samaasa_type)
        TripaadiKaarya(pp)


def main():
    """Main function"""

    pp = Prakriya()

    CreatePrakriya.add_samasa(pp, ("तपस्", "स्वाध्याय"), SamaasaType.DWANDWA)

    # CreatePrakriya.add_dhaatu(pp, 1223)
    # CreatePrakriya.add_krt(pp, "क्विप्", Krdartha.ANAADI, "वाच्", 2, 1)

    # CreatePrakriya.add_dhaatu(pp, 1250)
    # CreatePrakriya.add_krt(pp, "क", Krdartha.ANAADI, "नार", 2, 1)

    # CreatePrakriya.add_dhaatu(pp, 0)
    # CreatePrakriya.add_krt(pp, "अण्", Krdartha.ANAADI, "अग्नि", 2, 1)

    # CreatePrakriya.add_dhaatu(pp, 563)
    # CreatePrakriya.add_unaadi(pp, "कीकच्")

    # CreatePrakriya.add_praatipadika(pp, "वल्मीक")
    # CreatePrakriya.add_taddhita(pp, "इञ्", Taddhitaartha.TASYA_APATYAM)

    # CreatePrakriya.add_dhaatu(pp, 1673)
    # CreatePrakriya.add_unaadi(pp, "इन्")

    # CreatePrakriya.add_dhaatu(pp, 2181)
    # CreatePrakriya.add_krt(pp, "घञ्", Krdartha.BHAAVA)

    # CreatePrakriya.add_dhaatu(pp, 1215)
    # CreatePrakriya.add_unaadi(pp, "डुम्सुँन्")

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
