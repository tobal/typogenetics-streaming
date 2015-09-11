#!/usr/bin/env python

from .aminoacid import AminoAcid


def ribosome_get_amino_acids_from_strands(strand):
    if not strand:
        return
    length = len(strand) // 2
    acid_chain = []
    for i in range(length):
        pair = strand[i*2:(i+1)*2]
        if pair == 'AA':
            yield acid_chain
            acid_chain = []
        else:
            acid_chain.append(AminoAcid.get_acid_by_pair(pair))
    yield acid_chain

if __name__ == '__main__':
    pass
