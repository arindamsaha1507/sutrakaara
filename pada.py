"""Module to represent a Pada"""

from dataclasses import dataclass, field

from utils import Khanda


@dataclass
class Pada(Khanda):
    """Class to represent a Pada"""

    moola: str = field(default=None)
    names: list = field(default_factory=list)

    def __post_init__(self):
        self.roopa = self.moola
        self.typ.extend(self.names)
        self.aupadeshika = False

    def __repr__(self) -> str:
        # pylint: disable=useless-super-delegation
        return super().__repr__()
