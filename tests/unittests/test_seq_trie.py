'''
Test class 
'''
from tests.helper import *
from bio_sequence.seq_model.seq_trie import SeqTrie

@ddt
class TestSeqTrie(TestCase):
    def setUp(self):
        self.c = SeqTrie()

    @data(
        ['ATCG', 'G', 4, ()],
        ['A', 'A', 1, ()],
    )
    @unpack
    def test_insert(self, input, expect_val, expect_depth, expect_pos):
        res = self.c.insert(input)
        assert res.val == expect_val
        assert res.depth == expect_depth
        assert getattr(res, 'val_pos') == expect_pos
        assert res.is_leave is True

    @data(
        ['ATCG', 'ATCG'],
    )
    @unpack
    def test_get(self, input, expect):
        leave_node = self.c.insert(input)
        res = self.c.get(leave_node)
        assert res == expect
