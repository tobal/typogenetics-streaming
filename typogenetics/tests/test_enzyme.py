
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

    def test_enzyme_can_manipulate_null_strand(self):
        input_strand = ''
        expected_strand = []
        enzyme = Enzyme([AminoAcid.dlt, AminoAcid.mvr, AminoAcid.int])
        output_strand = enzyme.manipulate_strand(input_strand)
        self.assertListEqual(expected_strand, output_strand)

    def test_simple_enzyme_can_manipulate_simple_strand(self):
        input_strand = 'ACA'
        expected_strand = ['CA']
        enzyme = Enzyme([AminoAcid.dlt])
        output_strand = enzyme.manipulate_strand(input_strand)
        self.assertListEqual(expected_strand, output_strand)

    def test_enzyme_can_manipulate_simple_strand(self):
        input_strand = 'ACA'
        expected_strand = ['AAT']
        enzyme = Enzyme([AminoAcid.dlt, AminoAcid.mvr, AminoAcid.int])
        output_strand = enzyme.manipulate_strand(input_strand)
        self.assertListEqual(expected_strand, output_strand)
