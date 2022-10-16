from abc import *

import copy


class Calc(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def _do():
        pass


class Recursive(Calc):
    @staticmethod
    def _do(obj):
        """
            - シンプルな再帰
            - 深さ優先探索を行う
            - ASTをDoc2Vec, Word2Vecで受け入れられる最低限の形に持っていく
        """
        sequence = list()
        def rec(now, have=list()):
            if now["children"]:
                for nxt in now["children"]:
                    had = copy.copy(have)
                    had.append(now["type"])
                    rec(nxt, had)
            else:
                have.append(now["type"])
                sequence.append(have)
        rec(obj, have=list())

        return sequence