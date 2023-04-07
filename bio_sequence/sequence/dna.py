"""
process DNA sequence using naive methods
"""
from typing import Iterable
from .seq import Seq

class DNA(Seq):
    nt_pair = {'A':'T', 'T':'A', 'G':'C', 'C':'G',}

    def __init__(self, seq:str=None):
        super(DNA, self).__init__(seq)
    
    def complement(self)->str:
        return DNA.replace(self.seq)

    def reverse_complement(self)->str:
        return DNA.replace(self.seq[::-1])

    @staticmethod
    def replace(seq:str):
        if len(seq)==0:
            return ''
        nt = DNA.nt_pair.get(seq[0], seq[0])
        return nt + DNA.replace(seq[1:])

    def calculate_gc(self):
        '''
        GC percentage
        '''
        if self.length() == 0:
            return 0
        g = self.count_sub_seq('G')
        c = self.count_sub_seq('C')
        return (g + c)/self.length()

    @staticmethod
    def is_palindromic(seq:str, iter:str=None)->bool:
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
    
