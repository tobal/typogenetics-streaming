
from enum import Enum

class Base(Enum):
    adenine = 'A'
    guanine = 'G'
    cytozine = 'C'
    thymine = 'T'

    @classmethod
    def get_base_by_symbol(cls, symbol):
        for base in cls:
            if symbol == base.value:
                return base
