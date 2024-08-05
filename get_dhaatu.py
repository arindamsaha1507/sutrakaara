"""Get Dhaatus from a file"""

from utils import Prakriya

from dhaatu_prakarana import DhaatuSanjna
from it_prakarana import ItSanjna
from praakrita_kaarya import PraakritaKaaraya


class LoadDhaatus:
    """Class to load Dhaatus from a file"""

    @staticmethod
    def create_all_dhaatus():
        """Create all Dhaatus from the file"""

        with open("धातुपाठ_मूल.txt", "r", encoding="utf-8") as ff:
            s = ff.read()

        s = s.split("\n")
        # dhaatus = [Dhaatu(moola=w) for w in s]
        return s


def main():
    """Main function"""

    with open("धातु_1.csv", "r", encoding="utf-8") as ff:
        ref = ff.read()

    ref = ref.split("\n")

    selected_dhaatus = [
        0,
        956,
        268,
        1,
        424,
        1206,
        1647,
        2081,
        1211,
        74,
    ]

    for dhaatu_kramaanka in selected_dhaatus:

        pp = Prakriya()
        moola = LoadDhaatus.create_all_dhaatus()[dhaatu_kramaanka]
        DhaatuSanjna(pp, moola)
        ItSanjna(pp)
        PraakritaKaaraya(pp)

        ref_dhaatu = ref[dhaatu_kramaanka + 1].split(",")[6]

        print(dhaatu_kramaanka, ref_dhaatu, pp.vartamaana_sthiti[0])




    with open("prakriya.txt", "w", encoding="utf-8") as ff:
        ff.write(pp.__repr__())


if __name__ == "__main__":
    main()
