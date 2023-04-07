'''
Test class 
'''
from tests.helper import *
from sequence.dna import DNA as c

@ddt
class TestDNA(TestCase):

    def setUp(self):
        pass

    def test_(self):
        c('ATGC')
    
   
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
