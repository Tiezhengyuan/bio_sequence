"""
process sequence
"""
from typing import Iterable

class Seq:
    def __init__(self, seq:str=None):
        self.seq = seq.upper().replace('\n', '')
    
    def length(self)->int:
        return len(self.seq)

    def reverse(self)->str:
        return self.seq[::-1]
    
    def count_sub_seq(self, sub_seq:str)->list:
        if len(sub_seq)==0:
            return 0
        return self.seq.count(sub_seq)

    def count_occurrence(self)->dict:
        res = {}
        for i in self.seq:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        return res
    
    def search_sub_seq(self, sub_seq:str)->list:
        if len(sub_seq)==0:
            return []
        #
        count, start = [], 0
        while start != -1:
            pos = self.seq.find(sub_seq, start)
            if pos >= 0:
                end = pos + len(sub_seq)
                count.append((pos, end))
                start += end
            else:
                start = -1
        return count

        
