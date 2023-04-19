'''
Test class 
'''
from tests.helper import *
from bio_sequence.sequence.bio_dna import BioDNA as c

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
        ['GATCTA', None, 'DL'],
        ["ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", None, 'MAIVMGR*KGAR*'],
        ["ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", True, 'MAIVMGR'],
        ['AT', None, ''],
    )
    @unpack
    def test_to_protein(self, seq, to_stop, expect):
        res = c(seq).translate(to_stop=to_stop)
        assert res == expect

    def test_to_rna(self):
        res = c('GATCTA').transcribe()
        assert res == 'GAUCUA'
    
