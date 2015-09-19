
from .working_enzyme import WorkingEnzyme
from enum import Enum
from collections import namedtuple


Acid = namedtuple('Acid', 'duplet direction apply')


def _dlt(working_enzyme):
    strand = working_enzyme.strand
    pos = working_enzyme.pos
    output_strand = ''

    strand = strand[:pos] + strand[pos + 1:]

    return WorkingEnzyme(strand=strand, pos=pos), output_strand


def _swi(working_enzyme):
    pass


def _mvr(working_enzyme):
    strand = working_enzyme.strand
    pos = working_enzyme.pos
    output_strand = ''

    pos += 1

    return WorkingEnzyme(strand=strand, pos=pos), output_strand


def _mvl(working_enzyme):
    pass


def _cop(working_enzyme):
    pass


def _off(working_enzyme):
    pass


def _ina(working_enzyme):
    pass


def _inc(working_enzyme):
    pass


def _ing(working_enzyme):
    pass


def _int(working_enzyme):
    strand = working_enzyme.strand
    pos = working_enzyme.pos
    output_strand = ''

    strand = strand[:pos + 1] + 'T' + strand[pos + 1:]

    return WorkingEnzyme(strand=strand, pos=pos), output_strand


def _rpy(working_enzyme):
    pass


def _rpu(working_enzyme):
    pass


def _lpy(working_enzyme):
    pass


def _lpu(working_enzyme):
    pass


def _cut(working_enzyme):
    pass


class TertiaryDirection(Enum):
    left = 'l'
    right = 'r'
    straight = 's'


class AminoAcid(Enum):
    cut = Acid(duplet='AC', direction=TertiaryDirection.straight, apply=_cut)
    dlt = Acid(duplet='AG', direction=TertiaryDirection.straight, apply=_dlt)
    swi = Acid(duplet='AT', direction=TertiaryDirection.right, apply=_swi)
    mvr = Acid(duplet='CA', direction=TertiaryDirection.straight, apply=_mvr)
    mvl = Acid(duplet='CC', direction=TertiaryDirection.straight, apply=_mvl)
    cop = Acid(duplet='CG', direction=TertiaryDirection.right, apply=_cop)
    off = Acid(duplet='CT', direction=TertiaryDirection.left, apply=_off)
    ina = Acid(duplet='GA', direction=TertiaryDirection.straight, apply=_ina)
    inc = Acid(duplet='GC', direction=TertiaryDirection.right, apply=_inc)
    ing = Acid(duplet='GG', direction=TertiaryDirection.right, apply=_ing)
    int = Acid(duplet='GT', direction=TertiaryDirection.left, apply=_int)
    rpy = Acid(duplet='TA', direction=TertiaryDirection.right, apply=_rpy)
    rpu = Acid(duplet='TC', direction=TertiaryDirection.left, apply=_rpu)
    lpy = Acid(duplet='TG', direction=TertiaryDirection.left, apply=_lpy)
    lpu = Acid(duplet='TT', direction=TertiaryDirection.left, apply=_lpu)

    @classmethod
    def get_acid_by_duplet(cls, duplet):
        for acid in cls:
            if duplet == acid.value.duplet:
                return acid
