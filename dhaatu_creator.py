"""Module to create Dhaatu objects from a list of Dhatus"""
# pylint: disable=non-ascii-module-import

from dataclasses import dataclass, field

from utils import Khanda, Prakriya, KhandaType
from sutra import sutra_1_3_1, sutra_1_3_2, vartika_1_3_2, sutra_1_3_3, sutra_1_3_4

# import pandas as pd
# from varna import *
# from vinyaasa import *
# from pratyaahaara import *
# from recorder import *
# from sutra import *


GANAS = {
    "१": "भ्वादि",
    "२": "अदादि",
    "३": "जुहोत्यादि",
    "४": "दिवादि",
    "५": "स्वादि",
    "६": "तुदादि",
    "७": "रुधादि",
    "८": "तनादि",
    "९": "क्र्यादि",
    "१०": "चुरादि",
}

@dataclass
class Dhaatu(Khanda):
    """Class to represent a Dhaatu"""

    # pylint: disable=too-many-instance-attributes

    moola: str = field(default=None)
    kramaanka: str = field(init=False)
    gana: str = field(init=False)
    upadesha: str = field(init=False)
    artha: str = field(init=False)
    dhaatu: str = field(init=False)
    pada: str = field(init=False)
    idaagama: str = field(init=False)
    anudaatta_it: bool = field(default=False)
    svarita_it: bool = field(default=False)
    anudaatta_svara: bool = field(init=False, default=False)

    def __post_init__(self):
        self.typ.append(KhandaType.DHAATU)
        self.kramaanka = self.moola.split(" ", maxsplit=1)[0]
        self.upadesha = self.moola.split(" ")[1]
        self.artha = " ".join(self.moola.split(" ")[2:])
        self.gana = GANAS[self.kramaanka.split(".")[0]]

        self.roopa = self.upadesha

    def __repr__(self) -> str:
        return super().__repr__()

    def add_dhaatu(self, prakriya: Prakriya):
        """Add the Dhaatu to the Prakriya"""

        if prakriya.length > 0:
            raise ValueError("The Prakriya is not empty")

        sutra_1_3_1(prakriya, self)

    def identify_it(self, prakriya: Prakriya):
        """Identify the It of the Dhaatu"""

        vartika_1_3_2(prakriya)
        sutra_1_3_3(prakriya)
        sutra_1_3_2(prakriya)
        sutra_1_3_4(prakriya)

    #     # fname = f'धातु/{self.upadesha}.csv'
    #     # row = {'स्थिति': self.upadesha, 'सूत्र': '-', 'टिप्पणी': '-'}
    #     # self.df = pd.concat([self.df, pd.DataFrame([row])], ignore_index=True)

    #     # self.df, anudaatta, svarita = self.it_lopa()
    #     # self.df = self.pada_nirnaya(anudaatta, svarita)
    #     # self.df = self.get_idaagama()
    #     # self.df = self.praakritika()

    #     # self.df.to_csv(fname, index=False)

    # def __repr__(self):
    #     return f'धातु : {self.dhaatu} \nअर्थ : {self.artha} \nगण : {self.gana} \nपद : {self.pada}\nइडागम : {self.idaagama} \nउपदेश : {self.upadesha} \nइत् : {" ".join(self.it)}'

    # def get_gana(self):
    #     d = {
    #         "१": "भ्वादि",
    #         "२": "अदादि",
    #         "३": "जुहोत्यादि",
    #         "४": "दिवादि",
    #         "५": "स्वादि",
    #         "६": "तुदादि",
    #         "७": "रुधादि",
    #         "८": "तनादि",
    #         "९": "क्र्यादि",
    #         "१०": "चुरादि",
    #     }

    #     self.gana = d[self.kramaanka.split(".")[0]]

    # def it_lopa(self):
    #     vv = get_vinyaasa(self.upadesha)
    #     svarita = []
    #     anudaatta = []
    #     anunaasika = []

    #     for ii in range(len(vv)):
    #         if vv[ii] == '॑':
    #             svarita.append(ii-1)
    #         if vv[ii] == '॒':
    #             anudaatta.append(ii-1)
    #         if vv[ii] in anunaasika_svara:
    #             anunaasika.append(ii)

    #     if len(anunaasika) > 0:
    #         self.df, aa = उपदेशेऽजनुनासिक_इत्(self.df, anunaasika)
    #         self.it.extend(aa)

    #     if vv[-1] in expand_pratyahaara('हल्'):
    #         self.df, bb = हलन्त्यम्(self.df)
    #         self.it.append(bb)

    #     if get_shabda(vv[:2]) in ['ञि', 'टु', 'डु']:
    #         self.df, cc = आदिर्ञिटुडवः(self.df)
    #         self.it.append(cc)

    #     if len(self.it) > 0:
    #         self.df = तस्य_लोपः(self.df, ii='dhaatu')

    #     return self.df, anudaatta, svarita

    # def pada_nirnaya(self, anudaatta, svarita):
    #     if len(self.it) == 0:
    #         self.df = शेषात्_कर्तरि_परस्मैपदम्(self.df)
    #         self.pada = 'परस्मैपदी'
    #     else:
    #         if 'ञ्' in self.it or len(svarita) > 0:
    #             self.df = स्वरितञितः_कर्त्रभिप्राये_क्रियाफले(self.df)
    #             self.pada = 'उभयपदी'
    #         elif 'ङ्' in self.it or len(anudaatta) > 0:
    #             self.df = अनुदात्तङित_आत्मनेपदम्(self.df)
    #             self.pada = 'आत्मनेपदी'
    #         else:
    #             self.df = शेषात्_कर्तरि_परस्मैपदम्(self.df)
    #             self.pada = 'परस्मैपदी'

    #     self.dhaatu = get_shabda(get_sthiti(self.df))
    #     return self.df

    # def get_idaagama(self):
    #     vv = get_vinyaasa(self.dhaatu)
    #     cc = len([x for x in vv if x in svara])

    #     if '॒' in vv and cc == 1:
    #         self.df = एकाच_उपदेशेऽनुदात्तात्(self.df)
    #         self.idaagama = 'अनिट्'
    #         self.dhaatu = get_shabda(get_sthiti(self.df))

    #     elif 'ऊ' in self.it:
    #         self.df = स्वरतिसूतिसूयतिधूञूदितो_वा(self.df)
    #         self.idaagama = 'वेट्'
    #     else:
    #         self.idaagama = 'सेट्'

    #     return self.df

    # def praakritika(self):
    #     vv = get_vinyaasa(self.dhaatu)

    #     if vv[0] == 'ष्':
    #         self.df = धात्वादेः_षः_सः(self.df)
    #     elif vv[0] == 'ण्':
    #         self.df = णो_नः(self.df)

    #     if 'इ' in self.it:
    #         self.df, jj = इदितो_नुम्_धातोः(self.df)
    #         vv = get_vinyaasa(get_sthiti(self.df))
    #         if vv[jj+2] in expand_pratyahaara('झल्'):
    #             self.df = नश्चापदान्तस्य_झलि(self.df, jj+1)
    #             self.df = अनुस्वारस्य_ययि_परसवर्णः(self.df, jj+1)

    #     self.dhaatu = get_shabda(get_sthiti(self.df))
    #     return self.df


# if __name__ == "__main__":
#     with open("धातुपाठ_मूल.txt", "r") as ff:
#         s = ff.read()

#     s = s.split("\n")
#     dhaatus = [Dhaatu(w) for w in s]
#     d = [dhaatu.__dict__ for dhaatu in dhaatus]

#     df = pd.DataFrame(d)
#     df = df.set_index("क्रमाङ्क")
#     print(df)
#     df.to_csv("धातु_1.csv")
