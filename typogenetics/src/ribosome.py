#!/usr/bin/env python

from enum import Enum

class WorkingEnzyme():
    strand_pair = None
    head_pos = None

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

def ribosome_get_amino_acids_from_strands(strand):
    if not strand:
        return []
    acids = []
    for acid in AminoAcid:
        if strand == acid.value:
            acids.append(acid)
    return acids

if __name__ == '__main__':
    pass

