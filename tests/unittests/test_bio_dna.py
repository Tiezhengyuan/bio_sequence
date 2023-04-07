'''
Test class 
'''
from tests.helper import *
from sequence.bio_dna import bio_DNA as c

@ddt
class Test_(TestCase):

    def setUp(self):
        pass

    def test_(self):
        c('ATGC')
    
    def test_count_subseq(self):
        res = c('ATGATCTA').count('AT')
        assert res == 2

    def test_locate_subseq(self):
        res = c('GATCTA').find('AT')
        assert res == 1

    def test_complement(self):
        res = c('GATCTA').complement()
        assert res == 'CTAGAT'

    def test_reverse_complement(self):
        res = c('GATCTA').reverse_complement()
        assert res == 'TAGATC'

    @data(
        ['GATCTA', 'DL'],
        ["ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", 'MAIVMGR*KGAR*'],
        # ['AT', ''],
    )
    @unpack
    def test_to_protein(self, seq, expect):
        res = c(seq).translate()
        assert res == expect

    def test_to_rna(self):
        res = c('GATCTA').transcribe()
        assert res == 'GAUCUA'
    
