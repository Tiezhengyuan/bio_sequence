"""
compress sequence
"""
import re
from typing import Iterable

class Compress:
    def __init__(self):
        pass
    
    @staticmethod
    def encode_repeat(seq:Iterable):
        '''
        count consecutive repeating characters as digits
        '''
        if len(list(seq)) == 0:
            return ''
        encoded = []
        curr, count = seq[0], 1
        for i in seq[1:]:
            if i != curr:
                encoded.append(curr)
                if count > 1:
                    encoded.append(str(count))
                curr, count = i, 1
            else:
                count += 1
        else:
            encoded.append(curr)
            if count > 1:
                encoded.append(str(count))
        return ''.join(encoded)

    @staticmethod
    def decode_repeat(encoded_seq:Iterable):
        encoded = filter(None, re.split(r'([A-Za-z])', encoded_seq))
        seq = []
        for i in encoded:
            try:
                seq[-1] = seq[-1] * int(i)
            except:
                seq.append(i)
        return ''.join(seq)

                    
