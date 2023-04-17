'''
Test class 
'''
from tests.helper import *
from bio_sequence.seq_model.scan import Scan
from bio_sequence.seq_model.seq_trie import SeqTrie

class TestSeqTrie(TestCase):

    def setUp(self):
        '''
        root-A1-T2-G3-C4
           |     |-T5-A6
            -G7-T8
        '''
        sequence = 'ATGCATTAATGCGT'
        self.t = SeqTrie()
        for seq, end_pos in Scan.forward(sequence, 0, 4):
            # print(seq, end_pos)
            self.t.insert(seq, end_pos)

    def test_insert(self):
        root = self.t.root
        assert root.val == ''
        assert root.depth == 0
        assert list(root.children) == ['A', 'G']

        node1 = root.children['A']
        assert node1.val == 'A'
        assert node1.depth == 1
        assert list(node1.children) == ['T',]
        node2 = node1.children['T']
        assert node2.val == 'T'
        assert node2.depth == 2
        assert list(node2.children) == ['G', 'T']

        node3 = node2.children['G']
        assert node3.val == 'G'
        assert node3.depth == 3
        assert list(node3.children) == ['C',]
        node4 = node3.children['C']
        assert node4.val == 'C'
        assert node4.depth == 4
        assert list(node4.children) == []
        assert node4.is_leave is True
        assert node4.val_pos == (4, 12)

    def test_dfs_search(self):
        iter = self.t.dfs_search(self.t.root, '')
        res = next(iter)
        assert res == ('ATGC', (4,12))
        res = next(iter)
        assert res == ('ATTA', (8,))
        res = next(iter)
        assert res == ('GT', (14,))

    def test_scan(self):
        res = self.t.scan()
        assert list(res) == ['ATGC', 'ATTA', 'GT']

    def test_retrieve(self):
        res = self.t.retrieve()
        assert list(res) == ['ATGC', 'ATTA', 'ATGC', 'GT']

    def test_get_sequence(self):
        res = self.t.get_sequence()
        assert res == 'ATGCATTAATGCGT'