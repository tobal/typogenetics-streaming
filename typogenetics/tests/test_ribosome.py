
from src.ribosome import ribosome_get_amino_acids_from_strands, AminoAcid
from unittest import TestCase

class RibosomeTest(TestCase):
    def test_nullstrand_returns_no_amino_acids(self):
        strand = ''
        amino_acids = ribosome_get_amino_acids_from_strands(strand)
        self.assertEqual(len(amino_acids), 0)

    def test_can_convert_one_pair_to_amino_acid(self):
        strand = 'AC'
        amino_acids = ribosome_get_amino_acids_from_strands(strand)
        self.assertEqual(len(amino_acids), 1)
        self.assertEqual(amino_acids[0], AminoAcid.cut)
        self.assertEqual(amino_acids[0].value, strand)

    def test_converts_long_strands_to_correct_acid_chain(self):
        pass

    def test_can_cut_into_multiple_acid_chains(self):
        pass
