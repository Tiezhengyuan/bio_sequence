"""
protein
"""
import re
from typing import Iterable
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

from bio_sequence.seq_model.scan import Scan


class Protein:
    def __init__(self, seq:str):
        self.seq = Seq(seq, IUPAC.protein)
    
    def _motif(self, prosite:str, k:int):
        '''
        detect motif
        '''
        iter = Scan.k_mers(self.seq, k)
        for seq in iter:
