#!/usr/bin/env python

from .aminoacid import AminoAcid


def ribosome_get_amino_acids_from_strands(strand):
    if not strand:
        return
    length = len(strand) // 2
    acid_chain = []
    for i in range(length):
        duplet = strand[i*2:(i+1)*2]
        if duplet == 'AA':
            yield acid_chain
            acid_chain = []
        else:
            acid_chain.append(AminoAcid.get_acid_by_duplet(duplet))
    yield acid_chain

if __name__ == '__main__':
    pass
