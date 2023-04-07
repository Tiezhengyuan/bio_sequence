"""
process DNA sequence using naive methods
"""
from typing import Iterable
from .seq import Seq

class DNA(Seq):
    def __init__(self, seq:str=None):
        supper(DNA, self).__init__(self, seq)
    
    
    def complement(self):
        return self.seq.replace('A', 'T').replace('T', 'A').\
            replace('G','C').replace('C','G')

    def reverse_complement(self):
        com_seq = self.complement()
        return com_seq[::-1]

    def transcript(self):
        pass

    @staticmethod
    def is_palindromic(seq:str, iter:str=None):
        if iter is None: iter = 0
        if len(seq) >= 2:
            first, last = seq[0], seq[-1]
            if first == last:
                return DNA.is_palindromic(seq[1:-1], iter+1)
            return False
        else:
            if iter == 0:
                return False
        return True
    
