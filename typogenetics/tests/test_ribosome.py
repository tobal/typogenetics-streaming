
from ..ribosome import ribosome_get_enzymes_from_strand
from ..aminoacid import AminoAcid
from unittest import TestCase

class RibosomeTest(TestCase):
    def test_nullstrand_returns_no_amino_acids(self):
        strand = ''
        amino_acids = list(ribosome_get_enzymes_from_strand(strand))
        self.assertEqual(len(amino_acids), 0)

    def test_can_convert_one_duplet_to_amino_acid(self):
        strand = 'AC'
        enzymes = list(ribosome_get_enzymes_from_strand(strand))
        self.assertListEqual([[AminoAcid.cut]], enzymes)

    def test_converts_long_strands_to_correct_acid_chain(self):
        strand = 'ACGCCACC'
        enzymes = list(ribosome_get_enzymes_from_strand(strand))
        self.assertListEqual([[AminoAcid.cut, AminoAcid.inc, AminoAcid.mvr, AminoAcid.mvl]],
                             enzymes)

    def test_converts_long_strands_with_extra_character(self):
        strand = 'ACGCCACCG'
        enzymes = list(ribosome_get_enzymes_from_strand(strand))
        self.assertListEqual([[AminoAcid.cut, AminoAcid.inc, AminoAcid.mvr, AminoAcid.mvl]],
                             enzymes)

    def test_can_cut_into_multiple_acid_chains(self):
        strand = 'ACGCAACACCG'
        enzymes = list(ribosome_get_enzymes_from_strand(strand))
        self.assertListEqual([[AminoAcid.cut, AminoAcid.inc], [AminoAcid.mvr, AminoAcid.mvl]],
                             enzymes)
