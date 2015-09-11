
from enum import Enum

class AminoAcid(Enum):
    cut = 'AC'
    dlt = 'AG'
    swi = 'AT'
    mvr = 'CA'
    mvl = 'CC'
    cop = 'CG'
    off = 'CT'
    ina = 'GA'
    inc = 'GC'
    ing = 'GG'
    int = 'GT'
    tpy = 'TA'
    rpu = 'TC'
    lpy = 'TG'
    lpu = 'TT'

    @classmethod
    def get_acid_by_pair(cls, pair):
        for acid in cls:
            if pair == acid.value:
                return acid