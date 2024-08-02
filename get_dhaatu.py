from dhaatu import Dhaatu, Prakriya


class LoadDhaatus:
    """Class to load Dhaatus from a file"""

    @staticmethod
    def create_all_dhaatus():
        """Create all Dhaatus from the file"""

        with open("धातुपाठ_मूल.txt", "r", encoding="utf-8") as ff:
            s = ff.read()

        s = s.split("\n")
        dhaatus = [Dhaatu(moola=w) for w in s]
        return dhaatus


def main():
    """Main function"""

    pp = Prakriya()
    dhaatu = LoadDhaatus.create_all_dhaatus()[0]
    dhaatu = LoadDhaatus.create_all_dhaatus()[956]
    dhaatu = LoadDhaatus.create_all_dhaatus()[268]
    dhaatu = LoadDhaatus.create_all_dhaatus()[1]
    dhaatu = LoadDhaatus.create_all_dhaatus()[424]
    dhaatu = LoadDhaatus.create_all_dhaatus()[1206]
    dhaatu = LoadDhaatus.create_all_dhaatus()[1647]
    dhaatu = LoadDhaatus.create_all_dhaatus()[2081]
    dhaatu = LoadDhaatus.create_all_dhaatus()[1211]
    dhaatu.add_dhaatu(pp)
    dhaatu.identify_it(pp)

    # print(उपदेशेऽजनुनासिकइत्(pp))

    with open("prakriya.txt", "w", encoding="utf-8") as ff:
        ff.write(pp.__repr__())

    print(dhaatu.__dict__)


if __name__ == "__main__":
    main()
