'''
Test class 
'''
from tests.helper import *
from bio_sequence.seq_model.scan import Scan as c

@ddt
class TestScan(TestCase):

    @data(
        ['ATC', None,  ['A', 'T', 'C']],
        ['ATC', 1,  ['A', 'T', 'C']],
        ['ATC', -2,  ['A', 'T', 'C']],
        ['ATC', 2,  ['AT', 'C']],
        ['ATCG', 2,  ['AT', 'CG']],
        ['ATC', 3,  ['ATC']],
        ['ATC', 10,  ['ATC']],
    )
    @unpack
    def test_forward(self, seq, step, expect):
        res = c.forward(seq, step)
        assert list(res) == expect

    @data(
        ['ATC', None,  ['C', 'T', 'A']],
        ['ATC', 1,  ['C', 'T', 'A']],
        ['ATC', -2,  ['C', 'T', 'A']],
        ['ATC', 2,  ['TC', 'A']],
        ['ATCG', 2,  ['CG', 'AT']],
        ['ATC', 3,  ['ATC']],
        ['ATC', 10,  ['ATC']],
    )
    @unpack
    def test_backward(self, seq, step, expect):
        res = c.backward(seq, step)
        assert list(res) == expect

    @data(
        ['ATC', None,  [('A', 'T'), ('T', 'C')]],
        ['ATCG', 1,  [('A', 'T'), ('T', 'C'), ('C', 'G')]],
        ['ATC', 2,  [('AT', 'TC'),]],
    )
    @unpack
    def test_neighbor_forward(self, seq, step, expect):
        res = c.neighbor_forward(seq, step)
        assert list(res) == expect

    @data(
        ['ATC', [('A','C')]],
        ['AC', [('A','C')]],
        ['A', []],
        ['', []],
        ['ATGCACC', [('A','C'),('T','C'),('G','A')]],
    )
    @unpack
    def test_biends(self, seq, expect):
        res = c.biends(seq)
        assert list(res) == expect

    @data(
        ['ATACTC', 5,  ['ATACT', 'TACTC']],
        ['ATACTC', 15,  ['ATACTC']],
        ['ATA', 1,  ['A','T','A',]],
    )
    @unpack
    def test_k_mers(self, seq, k, expect):
        res = c.k_mers(seq, k)
        assert [i[0] for i in res] == expect