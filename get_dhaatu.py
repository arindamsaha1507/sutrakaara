# import pandas as pd
from dhaatu_creator import Dhaatu, Prakriya


# import yaml
# from pathlib import Path

# def get_dhaatu(query, find_unique=False):

#     df = pd.read_csv('धातु.csv')

#     for ii in query.keys():
#         if ii in df.columns:
#             df = df[df[ii] == query[ii]]

#     idx = df.index.values

#     with open('धातुपाठ_मूल.txt', 'r') as ff:
#         s = ff.read()

#     s = s.split('\n')

#     return [Dhaatu(s[ii]) for ii in idx]


class DhaatuFunctions:

    @staticmethod
    def create_all_dhaatus():
        with open("धातुपाठ_मूल.txt", "r", encoding="utf-8") as ff:
            s = ff.read()

        s = s.split("\n")
        dhaatus = [Dhaatu(moola=w) for w in s]
        return dhaatus


def main():

    pp = Prakriya()
    # dhaatu = DhaatuFunctions.create_all_dhaatus()[0]
    # dhaatu = DhaatuFunctions.create_all_dhaatus()[956]
    # dhaatu = DhaatuFunctions.create_all_dhaatus()[268]
    # dhaatu = DhaatuFunctions.create_all_dhaatus()[1]
    # dhaatu = DhaatuFunctions.create_all_dhaatus()[424]
    # dhaatu = DhaatuFunctions.create_all_dhaatus()[1206]
    # dhaatu = DhaatuFunctions.create_all_dhaatus()[1647]
    # dhaatu = DhaatuFunctions.create_all_dhaatus()[2081]
    dhaatu = DhaatuFunctions.create_all_dhaatus()[1211]
    dhaatu.add_dhaatu(pp)
    dhaatu.identify_it(pp)

    # print(उपदेशेऽजनुनासिकइत्(pp))

    with open("prakriya.txt", "w", encoding="utf-8") as ff:
        ff.write(pp.__repr__())

    print(dhaatu.__dict__)


if __name__ == "__main__":
    main()