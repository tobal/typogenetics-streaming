
from base import Base
from unittest import TestCase

class AminoAcidTest(TestCase):
    def test_can_get_base_by_symbol(self):
        expected_base = Base.adenine
        self.assertEqual(Base.get_base_by_symbol('A'), expected_base)
