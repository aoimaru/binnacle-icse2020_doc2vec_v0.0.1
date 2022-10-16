from abc import *

from libs.files import *
from libs.calcs import *
from libs.cleanings import *
from libs.contents import *

import os

class TR(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def _get_training_data():
        pass

class TR_V1(TR):
    @staticmethod
    def _get_training_data(file_paths):
        training_data = dict()
        for file_path in file_paths:
            sequence_dict = RUNContent._get_sequence(file_path)
            for sequence_key, sequence_values in sequence_dict.items():
                sequences = CleanRUN._Disassembly(sequence_values)
                for seq_id, sequence in enumerate(sequences):
                    dst_sequence = list()
                    for seq in sequence:
                        dst_sequence.extend(seq)
                    sequence_id = "{}:{}".format(sequence_key, seq_id)
                    training_data[sequence_id] = dst_sequence
        return training_data
    
    @staticmethod
    def _get_training_data_v2(file_paths):
        training_data_v2 = dict()
        for file_path in file_paths:
            base_name = os.path.basename(file_path); base_name = base_name.replace(".json", "")
            training_data = dict()
            sequence_dict = RUNContent._get_sequence(file_path)
            for sequence_key, sequence_values in sequence_dict.items():
                sequences = CleanRUN._Disassembly(sequence_values)
                for seq_id, sequence in enumerate(sequences):
                    dst_sequence = list()
                    for seq in sequence:
                        dst_sequence.extend(seq)
                    sequence_id = "{}:{}".format(sequence_key, seq_id)
                    training_data[sequence_id] = dst_sequence
            training_data_v2[base_name] = training_data
        return training_data_v2