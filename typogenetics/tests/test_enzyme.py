
from ..enzyme import Enzyme, Base
from ..aminoacid import AminoAcid
from unittest import TestCase

class EnzymeTest(TestCase):
    def test_can_determine_binding_preference(self):
        enzyme = Enzyme([AminoAcid.dlt, AminoAcid.off, AminoAcid.mvr,
                         AminoAcid.ing, AminoAcid.lpu, AminoAcid.cop])
        self.assertEqual(enzyme.binding_preference, Base.adenine)
        self.assertEqual(Enzyme([AminoAcid.int]).binding_preference, Base.cytozine)
        self.assertEqual(Enzyme([AminoAcid.swi]).binding_preference, Base.guanine)
        self.assertEqual(Enzyme([AminoAcid.swi, AminoAcid.swi]).binding_preference, Base.thymine)
