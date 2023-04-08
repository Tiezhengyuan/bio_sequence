'''
Test class 
'''
from tests.helper import *
from bio_sequence.sequence.dna import DNA as c

@ddt
class TestDNA(TestCase):

    def test_(self):
        c('ATGC')

    @data(
        ['ATGC', 'TACG'],
        ['ATIN', 'TAIN'],
    )
    @unpack
    def test_complement(self, seq, expect):
        res = c(seq).complement()
        assert res == expect

    @data(
        ['ATGC', 'GCAT'],
    )
    @unpack
    def test_reverse_complement(self, seq, expect):
        res = c(seq).reverse_complement()
        assert res == expect

    @data(
        ['ATGC', .5],
        ['GCGGC', 1],
        ['', 0],
        ['AB', 0],
    )
    @unpack
    def test_calculate_gc(self, seq, expect):
        res = c(seq).calculate_gc()
        assert res == expect



    @data(
        ['GATCTCTAG', True],
        ['GATCCTAG', True],
        ['GAG', True],
        ['GG', True],
        ['GATT', False],
        ['', False],
    )
    @unpack
    def test_is_palindromic(self, input, expect):
        res = c.is_palindromic(input)
        assert res == expect

    @data(
        ['ATGC', 'TGA', 2, [(1,3)]],
        ['ATGCTATGCT', 'TGCT', 4,  [(1, 4), (6, 9)]],
    )
    @unpack
    def test_detect_similarity(self, seq1, seq2, expect_max, expect):
        res = c(seq1).detect_similarity(seq2)
        assert res[0] == expect_max
        assert res[1] == expect

    @data(
        ['AAATAAA', 'AAATTT', 3],
        ['AAATAAA', 'TAAATTT', 0],
    )
    @unpack
    def test_detect_overlap(self, seq1, seq2, expect):
        res = c(seq1).detect_overlap(seq2)
        assert res == expect





