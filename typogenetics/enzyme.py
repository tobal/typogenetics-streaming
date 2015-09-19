
from collections import namedtuple
from .base import Base
from .aminoacid import TertiaryDirection, AminoAcid

WorkingEnzyme = namedtuple('WorkingEnzyme', 'strand pos')

class Enzyme:
    def __init__(self, acid_chain):
        self._acid_chain = acid_chain
        self._binding_preference = self._determine_binding_preference()

    @property
    def acid_chain(self):
        return self._acid_chain

    @property
    def binding_preference(self):
        return self._binding_preference

    def manipulate_strand(self, strand):
        strands = []
        working_enzyme = self._bind_to_strand(strand)
        if working_enzyme:
            for amino_acid in self._acid_chain:
                working_enzyme, strand = self._apply_amino_acid_on_working_enzyme(amino_acid, working_enzyme)
                if strand:
                    strands.append(strand)
            strands.append(working_enzyme.strand)
        return strands

    def _determine_binding_preference(self):
        direction = self._determine_direction()
        return self._binding_base_by_direction(direction)

    @staticmethod
    def _binding_base_by_direction(direction):
        if direction == 0:
            return Base.adenine
        if direction == 1:
            return Base.cytozine
        if direction == 2:
            return Base.thymine
        if direction == 3:
            return Base.guanine

    def _determine_direction(self):
        direction_indicator = 0
        for acid in self._acid_chain:
            if acid.value.direction == TertiaryDirection.left:
                direction_indicator += 1
            elif acid.value.direction == TertiaryDirection.right:
                direction_indicator -= 1
        return direction_indicator % 4

    def _bind_to_strand(self, strand):
        for idx, symbol in enumerate(strand):
            if Base.get_base_by_symbol(symbol) == self.binding_preference:
                return WorkingEnzyme(strand=strand, pos=idx)

    def _apply_amino_acid_on_working_enzyme(self, amino_acid,  working_enzyme):
        strand = working_enzyme.strand
        pos = working_enzyme.pos
        output_strand = ''
        if amino_acid == AminoAcid.dlt:
            strand = strand[:pos] + strand[pos + 1:]
        if amino_acid == AminoAcid.mvr:
            pos += 1
        if amino_acid == AminoAcid.int:
            strand = strand[:pos + 1] + 'T' + strand[pos + 1:]
        return WorkingEnzyme(strand=strand, pos=pos), output_strand
