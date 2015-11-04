
from ..aminoacid import AminoAcid, TertiaryDirection
from ..working_enzyme import WorkingEnzyme
from unittest import TestCase

class AminoAcidTest(TestCase):
    def test_can_get_acid_by_duplet(self):
        expected_acid = AminoAcid.dlt
        self.assertEqual(AminoAcid.get_acid_by_duplet('AG'), expected_acid)

    def test_amino_acid_stores_tertiary_direction(self):
        expected_direction = TertiaryDirection.left
        self.assertEqual(AminoAcid.off.value.direction, expected_direction)

    def test_dlt(self):
        input_working_enzyme = WorkingEnzyme(strand='ATA', pos=1)
        delete = AminoAcid.dlt
        output_working_enzyme, output_strand = delete.value.apply(input_working_enzyme)
        expected_working_enzyme = WorkingEnzyme(strand='AA', pos=1)
        self.assertEqual(expected_working_enzyme, output_working_enzyme)
        self.assertEqual('', output_strand)

    def test_mvr(self):
        input_working_enzyme = WorkingEnzyme(strand='ATA', pos=1)
        move_right = AminoAcid.mvr
        output_working_enzyme, output_strand = move_right.value.apply(input_working_enzyme)
        expected_working_enzyme = WorkingEnzyme(strand='ATA', pos=2)
        self.assertEqual(expected_working_enzyme, output_working_enzyme)
        self.assertEqual('', output_strand)

    def test_int(self):
        input_working_enzyme = WorkingEnzyme(strand='ATA', pos=1)
        insert_t = AminoAcid.int
        output_working_enzyme, output_strand = insert_t.value.apply(input_working_enzyme)
        expected_working_enzyme = WorkingEnzyme(strand='ATTA', pos=1)
        self.assertEqual(expected_working_enzyme, output_working_enzyme)
        self.assertEqual('', output_strand)

    def test_ina(self):
        input_working_enzyme = WorkingEnzyme(strand='ATA', pos=1)
        insert_a = AminoAcid.ina
        output_working_enzyme, output_strand = insert_a.value.apply(input_working_enzyme)
        expected_working_enzyme = WorkingEnzyme(strand='ATAA', pos=1)
        self.assertEqual(expected_working_enzyme, output_working_enzyme)
        self.assertEqual('', output_strand)
