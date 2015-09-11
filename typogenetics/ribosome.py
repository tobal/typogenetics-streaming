#!/usr/bin/env python

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

