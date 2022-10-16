from abc import *

from libs.files import *
from libs.calcs import *
from libs.cleanings import *

import os
import copy

class Content(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def _get_sequence():
        pass
    
    @staticmethod
    @abstractmethod
    def _get_sequence_v2():
        pass

class RUNContent(Content):
    @staticmethod
    def _get_sequence(file_path):
        base_name = os.path.basename(file_path)
        base_name = base_name.replace(".json", "")
        sequence_dict = dict()
        df_contents = JsonFile._get_contents(file_path)
        for df_id, df_content in enumerate(df_contents):
            sequences = Recursive._do(df_content)
            for sequence in sequences:
                DC = sequence.pop(0)
                if DC != "DOCKER-RUN":
                    continue
                sequence = CleanRUN._do(sequence)
                if not sequence:
                    continue
                sequence_key = "{base_name}:{df_id}".format(
                    base_name=base_name,
                    df_id=df_id
                )
                if not sequence_key in sequence_dict:
                    sequence_dict[sequence_key] = list()
                sequence_dict[sequence_key].append(sequence)
        return sequence_dict
    
    @staticmethod
    def _get_trace_sequence(file_path):
        """
            ++ 変換前 ++
            ['SC-APT-GET-INSTALL', 'SC-APT-GET-F-NO-INSTALL-RECOMMENDS'],
            ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:TCL'],
            ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:TK']

            ++ 変換後1 ++
            ['SC-APT-GET-INSTALL', 'SC-APT-GET-F-NO-INSTALL-RECOMMENDS', 'SC-APT-GET-INSTALL'],
            ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:TCL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-INSTALL'],
            ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:TK', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-INSTALL']

            ++ 変換後2 ++
            変換後1をextendで全て繋げる

        """
        base_name = os.path.basename(file_path)
        base_name = base_name.replace(".json", "")
        sequence_dict = dict()
        df_contents = JsonFile._get_contents(file_path)
        for df_id, df_content in enumerate(df_contents):
            sequences = Recursive._do(df_content)
            for sequence in sequences:
                DC = sequence.pop(0)
                if DC != "DOCKER-RUN":
                    continue
                sequence = CleanRUN._do(sequence)
                if not sequence:
                    continue
                sequence_key = "{base_name}:{df_id}".format(
                    base_name=base_name,
                    df_id=df_id
                )
                """
                    追加分
                """
                sequence_clone = copy.copy(sequence)
                sequence.reverse()
                sequence_v2 = sequence_clone[:-1]+sequence

                if not sequence_key in sequence_dict:
                    sequence_dict[sequence_key] = list()
                sequence_dict[sequence_key].append(sequence_v2)
        return sequence_dict






