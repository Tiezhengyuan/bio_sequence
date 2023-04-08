'''
Test class 
'''
from tests.helper import *
from bio_sequence.seq_model.compress import Compress as c

@ddt
class TestCompress(TestCase):

    @data(
        ['AATTTGCCC','A2T3GC3'],
        ['ATGC', 'ATGC'],
        ['A', 'A'],
        ['ACCCCCCC', 'AC7'],
        ['TTTT', 'T4'],
        ['', ''],
    )
    @unpack
    def test_encode_repeat(self, input, expect):
        res = c.encode_repeat(input)
        assert res == expect


    @data(
        ['A2T3GC3', 'AATTTGCCC'],
        ['ATGC', 'ATGC'],
        ['AC7', 'ACCCCCCC'],
    )
    @unpack
    def test_decode_repeat(self, input, expect):
        res = c.decode_repeat(input)
        assert res == expect
