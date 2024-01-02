'''
Test class 
'''
from tests.helper import *
from src.eseq import BioDNA

@ddt
class Test_(TestCase):

    def test_(self):
        BioDNA('ATGC')
    
    def test_count_subseq(self):
        res = BioDNA('ATGATCTA').count('AT')
        assert res == 2

    def test_locate_subseq(self):
        res = BioDNA('GATCTA').find('AT')
        assert res == 1

    def test_complement(self):
        res = BioDNA('GATCTA').complement()
        assert res == 'CTAGAT'

    def test_reverse_complement(self):
        res = BioDNA('GATCTA').reverse_complement()
        assert res == 'TAGATC'

    @data(
        ['GATCTA', None, 'DL'],
        ["ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", None, 'MAIVMGR*KGAR*'],
        ["ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", True, 'MAIVMGR'],
        ['AT', None, ''],
    )
    @unpack
    def test_to_protein(self, seq, to_stop, expect):
        res = BioDNA(seq).translate(to_stop=to_stop)
        assert res == expect

    def test_to_rna(self):
        res = BioDNA('GATCTA').transcribe()
        assert res == 'GAUCUA'
    
