#!/usr/bin/env python

from .aminoacid import AminoAcid
from .enzyme import Enzyme


def ribosome_get_enzymes_from_strand(strand):
    if not strand:
        return
    length = len(strand) // 2
    acid_chain = []
    for i in range(length):
        duplet = strand[i*2:(i+1)*2]
        if duplet == 'AA':
            yield Enzyme(acid_chain)
            acid_chain = []
        else:
            acid_chain.append(AminoAcid.get_acid_by_duplet(duplet))
    yield Enzyme(acid_chain)


if __name__ == '__main__':
    pass
