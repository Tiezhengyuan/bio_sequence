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
    
    
    def detect_similarity(self, seq2:str)->tuple:
        '''
        Note: length of seq2<= self.seq
        '''
        len_seq = len(seq2)
        min_dist, pool = len_seq, []
        S = Seq(seq2)
        for seq1, start, end in self.k_mers(len_seq):
            dist = S.calculate_hamming_distance(seq1)
            if dist < min_dist:
                min_dist = dist
                pool = [(start, end)]
            elif dist == min_dist:
                pool.append((start, end))
        max_same = len_seq - min_dist
        return max_same, pool

    def detect_overlap(self, seq2:str)->tuple:
        '''
        3-end of seq1 is overlapped with 5-end of seq2
        '''
        olen = 0
        while self.seq[-(olen+1):] == seq2[:(olen+1)]:
            olen +=1
        return olen