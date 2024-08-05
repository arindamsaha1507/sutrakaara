"""Module for Dhaatu Prakarana."""

from dataclasses import dataclass, field
from utils import Prakriya
import sutra_list


@dataclass
class DhaatuSanjna:
    """Class to define the Sutras for the Dhaatu Sanjna"""

    prakriya: Prakriya
    moola: str = field(default=None)

    def __post_init__(self):

        sutra = sutra_list.SutraOneThreeOne()
        sutra.call(self.prakriya, self.moola)

