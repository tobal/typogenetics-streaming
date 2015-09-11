#!/usr/bin/env python

from .aminoacid import AminoAcid


def ribosome_get_enzymes_from_strand(strand):
    if not strand:
        return
    length = len(strand) // 2
    enzymes = []
    for i in range(length):
        duplet = strand[i*2:(i+1)*2]
        if duplet == 'AA':
            yield enzymes
            enzymes = []
        else:
            enzymes.append(AminoAcid.get_acid_by_duplet(duplet))
    yield enzymes

if __name__ == '__main__':
    pass
