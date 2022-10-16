from abc import *

import pprint

FIRST_SEQUENCES = 0
FIRST_SEQUENCE = 0

class Clean(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def _do():
        pass
    
    @staticmethod
    @abstractmethod
    def _Disassembly():
        pass

class CleanRUN(Clean):
    @staticmethod
    def _do(sequence):
        tokens = list()
        for seq in sequence:
            if seq.startswith("BASH-"):
                continue
            if seq == "UNKNOWN":
                continue
            tokens.append(seq)
        return tokens
    
    @staticmethod
    def _Disassembly(sequences):
        comp = sequences[FIRST_SEQUENCES][FIRST_SEQUENCE]
        dst_sequences = list()
        dst_sequence = list()
        for sequence in sequences:
            if sequence[FIRST_SEQUENCE] != comp:
                if dst_sequence:
                    dst_sequences.append(dst_sequence)
                dst_sequence = list()
                comp = sequence[FIRST_SEQUENCE]
            else:
                dst_sequence.append(sequence)
        
        return dst_sequences
                



