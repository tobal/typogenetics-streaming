
from ..aminoacid import AminoAcid, TertiaryDirection
from unittest import TestCase

class AminoAcidTest(TestCase):
    def test_can_get_acid_by_duplet(self):
        expected_acid = AminoAcid.dlt
        self.assertEqual(AminoAcid.get_acid_by_duplet('AG'), expected_acid)

    def test_amino_acid_stores_tertiary_direction(self):
        expected_direction = TertiaryDirection.left
        self.assertEqual(AminoAcid.off.value.direction, expected_direction)
