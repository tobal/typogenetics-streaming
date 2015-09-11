
from enum import Enum
from collections import namedtuple


Acid = namedtuple('Acid', 'duplet direction')


class TertiaryDirection(Enum):
    left = 'l'
    right = 'r'
    straight = 's'


class AminoAcid(Enum):
    cut = Acid(duplet='AC', direction=TertiaryDirection.straight)
    dlt = Acid(duplet='AG', direction=TertiaryDirection.straight)
    swi = Acid(duplet='AT', direction=TertiaryDirection.right)
    mvr = Acid(duplet='CA', direction=TertiaryDirection.straight)
    mvl = Acid(duplet='CC', direction=TertiaryDirection.straight)
    cop = Acid(duplet='CG', direction=TertiaryDirection.right)
    off = Acid(duplet='CT', direction=TertiaryDirection.left)
    ina = Acid(duplet='GA', direction=TertiaryDirection.straight)
    inc = Acid(duplet='GC', direction=TertiaryDirection.right)
    ing = Acid(duplet='GG', direction=TertiaryDirection.right)
    int = Acid(duplet='GT', direction=TertiaryDirection.left)
    rpy = Acid(duplet='TA', direction=TertiaryDirection.right)
    rpu = Acid(duplet='TC', direction=TertiaryDirection.left)
    lpy = Acid(duplet='TG', direction=TertiaryDirection.left)
    lpu = Acid(duplet='TT', direction=TertiaryDirection.left)

    @classmethod
    def get_acid_by_duplet(cls, duplet):
        for acid in cls:
            if duplet == acid.value.duplet:
                return acid
