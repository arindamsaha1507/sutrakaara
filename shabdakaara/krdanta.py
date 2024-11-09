"""Module for handling the krdanta class in Sanskrit."""

from dataclasses import dataclass, field
from utils import Prakriya, Khanda, KhandaType


@dataclass
class Krdanta(Khanda):
    """Class to represent a Krdanta"""

    prakriya: Prakriya = field(default=None)
    krdanta: str = field(default=None)

    def __post_init__(self):

        self.typ.append(KhandaType.KRIDANTA)
        self.roopa = self.krdanta
