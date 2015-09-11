
from ..aminoacid import AminoAcid
from unittest import TestCase

class AminoAcidTest(TestCase):
    def test_can_get_acid_by_duplet(self):
        expected_acid = AminoAcid.dlt
        self.assertEqual(AminoAcid.get_acid_by_duplet('AG'), expected_acid)
