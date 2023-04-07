'''
Test class 
'''
from tests.helper import *
from bio_sequence.sequence.seq import Seq as c

@ddt
class TestDNA(TestCase):

    @data(
        ['ATGC', 'ATGC'],
        ['AT\nGC', 'ATGC'],
        ['AtgC', 'ATGC'],
        ['', ''],
    )
    @unpack
    def test_(self, seq, expect):
        res = c(seq)
        assert getattr(res, 'seq') == expect

    @data(
        ['ATGC', 4],
        ['', 0],
    )
    @unpack
    def test_length(self, seq, expect):
        res = c(seq).length()
        assert res == expect

    @data(
        ['ATGC', 'CGTA'],
        ['', ''],
    )
    @unpack
    def test_reverse(self, seq, expect):
        res = c(seq).reverse()
        assert res == expect

    @data(
        ['ATGCCGCT', 'GC', 2],
        ['ATGCCGCT', 'C', 3],
        ['ATGCCGCT', 'GT', 0],
        ['ATGCCGCT', '', 0],
        ['ATGCCGCT', 'ATGCCGCT', 1],
    )
    @unpack
    def test_count_sub_seq(self, seq, sub_seq, expect):
        res = c(seq).count_sub_seq(sub_seq)
        assert res == expect

    @data(
        ['AAC', {'C':1, 'A':2}],
        ['', {}],
    )
    @unpack
    def test_count_occurrence(self, seq, expect):
        res = c(seq).count_occurrence()
        assert res == expect

    @data(
        ['ATGCCGCT', 'GC', [(2,4),(5,7)],],
        ['ATGCCGCT', 'AGC', [],],
        ['ATGCCGCT', 'T', [(1,2),(7,8)],],
        ['ATGCCGCT', '', [],],
        ['TAAAT', 'AA', [(1,3)],],
    )
    @unpack
    def test_search_sub_seq(self, seq, sub_seq, expect):
        res = c(seq).search_sub_seq(sub_seq)
        assert res == expect