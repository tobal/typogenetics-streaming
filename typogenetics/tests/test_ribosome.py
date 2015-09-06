
from src.ribosome import ribosome_get_amino_acids_from_strands, AminoAcid
from unittest import TestCase

class RibosomeTest(TestCase):
    def test_nullstrand_returns_no_amino_acids(self):
        strand = ''
        amino_acids = list(ribosome_get_amino_acids_from_strands(strand))
        self.assertEqual(len(amino_acids), 0)

    def test_can_convert_one_pair_to_amino_acid(self):
        strand = 'AC'
        amino_acids = list(ribosome_get_amino_acids_from_strands(strand))
        self.assertEqual(len(amino_acids), 1)
        self.assertEqual(amino_acids[0], AminoAcid.cut)
        self.assertEqual(amino_acids[0].value, strand)

    def test_converts_long_strands_to_correct_acid_chain(self):
        strand = 'ACGCCACC'
        amino_acids = list(ribosome_get_amino_acids_from_strands(strand))
        self.assertEqual(len(amino_acids), 4)
        self.assertListEqual(amino_acids, [AminoAcid.cut, AminoAcid.inc,
                                           AminoAcid.mvr, AminoAcid.mvl])

    def test_converts_long_strands_with_extra_character(self):
        strand = 'ACGCCACCG'
        amino_acids = list(ribosome_get_amino_acids_from_strands(strand))
        self.assertEqual(len(amino_acids), 4)
        self.assertListEqual(amino_acids, [AminoAcid.cut, AminoAcid.inc,
                                           AminoAcid.mvr, AminoAcid.mvl])

    def test_can_cut_into_multiple_acid_chains(self):
        strand = 'ACGCAACACCG'
        amino_acids = list(ribosome_get_amino_acids_from_strands(strand))
        self.assertEqual(len(amino_acids), 2)
        self.assertListEqual(amino_acids[0], [AminoAcid.cut, AminoAcid.inc])
        self.assertListEqual(amino_acids[1], [AminoAcid.mvr, AminoAcid.mvl])
