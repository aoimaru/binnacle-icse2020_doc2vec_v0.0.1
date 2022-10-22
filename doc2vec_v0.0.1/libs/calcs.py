from abc import *

import copy


class Calc(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def _do():
        pass
    
    @staticmethod
    @abstractmethod
    def _do_v2():
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
    
    @staticmethod
    def _do_v2(obj):
        def rec(now):
            if now["children"]:
                # now: D
                nxts = list()
                for nxt in now["children"]:
                    # nxt: C, E
                    tokens = rec(now)
                    # Cの場合: tokens: [[A, C], [B, C],,,]
                    for token in tokens:
                        token.insert(0, now["type"])
                        nxts.append(token)
                    # [[A, C, D], [B, C, D],,,]
                return nxts
            else:
                return [
                    [now["type"]]
                ]
        return rec(obj)