from abc import *

import copy
import itertools
import json
import pprint

import sys

sys.setrecursionlimit(2000)

class Calc(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def _do():
        pass
    
    @staticmethod
    @abstractmethod
    def _do_v2():
        pass

    @staticmethod
    @abstractmethod
    def _do_v3():
        pass
    
    @staticmethod
    @abstractmethod
    def _do_v3_v2():
        pass
    
    @staticmethod
    @abstractmethod
    def _do_v3_v3():
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
    
    @staticmethod
    def _do_v3(obj):
        def rec(now):
            if now["children"]:
                # now: D
                nxts = list()
                for nxt in now["children"]:
                    # nxt: C, E
                    tokens = rec(now)
                    # Cの場合: tokens: [[A, C], [B, C],,,]
                    for token in tokens:
                        token.insert(0, json.dumps(now))
                        nxts.append(token)
                    # [[A, C, D], [B, C, D],,,]
                return nxts
            else:
                return [
                    [json.dumps(now)]
                ]
        for branch in itertools.combinations(rec(obj), 2):
            branch_00 = sorted(branch[0], key=lambda x:len(x), reverse=True)
            branch_01 = sorted(branch[1], key=lambda x:len(x), reverse=True)
            output_branch_00 = list()
            output_branch_01 = list()
            for branch_0 in branch_00:
                c = json.dumps(branch_0)
                output_branch_00.append(c)
            for branch_1 in branch_01:
                c = json.dumps(branch_1)
                output_branch_01.append(c)
            print("output_branch_00:", output_branch_00)
            print("output_branch_01:", output_branch_01)
    
    @staticmethod
    def _do_v3_v2(obj):
        sequence = list()
        def rec(now, have=list()):
            if now["children"]:
                for nxt in now["children"]:
                    had = copy.copy(have)
                    had.append(json.dumps(now))
                    rec(nxt, had)
            else:
                have.append(json.dumps(now))
                sequence.append(have)
        rec(obj, have=list())

        output_branches = list()
        for branch in itertools.combinations(sequence, 2):
            branch_00 = sorted(branch[0], key=lambda x:len(x), reverse=True)
            branch_01 = sorted(branch[1], key=lambda x:len(x), reverse=True)
            output_branch_00 = list()
            output_branch_01 = list()
            for branch_0 in branch_00:
                c = json.loads(branch_0)
                output_branch_00.append(c["type"])
            for branch_1 in branch_01:
                c = json.loads(branch_1)
                output_branch_01.append(c["type"])



            if not branch_00:
                continue
            if not branch_01:
                continue

            if len(branch_00) <= 1:
                output_branch_02 = list()
                firsts = copy.copy(branch_00)
                seconds = copy.copy(branch_01)
                thirds = firsts+seconds
                for third in thirds:
                    c = json.loads(third)
                    output_branch_02.append(c["type"])
                print("output_branch_02:", output_branch_02)
                output_branch = {
                    "output_branch_00": output_branch_00,
                    "output_branch_01": output_branch_01,
                    "output_branch_02": output_branch_02
                }
                output_branches.append(output_branch)
                continue
            if len(branch_01) <= 1:
                output_branch_02 = list()
                firsts = copy.copy(branch_00)
                seconds = copy.copy(branch_01)
                firsts.reverse()
                _ = firsts.pop(-1)
                thirds = firsts+seconds
                for third in thirds:
                    c = json.loads(third)
                    output_branch_02.append(c["type"])
                # print("output_branch_02:", output_branch_02)
                output_branch = {
                    "output_branch_00": output_branch_00,
                    "output_branch_01": output_branch_01,
                    "output_branch_02": output_branch_02
                }
                output_branches.append(output_branch)
                continue


            if branch_00 == branch_01:
                firsts = copy.copy(branch_00)
                seconds = copy.copy(branch_01)
                thirds = [firsts[-1]+firsts[-2]+seconds[-1]]
                output_branch_02 = list()
                for third in thirds:
                    c = json.loads(third)
                    output_branch_02.append(c["type"])
                # print("output_branch_02:", output_branch_02)
                output_branch = {
                    "output_branch_00": output_branch_00,
                    "output_branch_01": output_branch_01,
                    "output_branch_02": output_branch_02
                }
                output_branches.append(output_branch)
                continue
            
            count = 0
            for branch_0, branch_1 in zip(branch_00, branch_01):
                if branch_0 != branch_1:
                    break
                count += 1
            
            if count == 0:
                firsts = copy.copy(branch_00)
                seconds = copy.copy(branch_01)
                firsts.reverse()
                thirds = firsts+["BASH-SCRIPT"]+seconds
                output_branch_02 = list()
                for third in thirds:
                    c = json.loads(third)
                    output_branch_02.append(c["type"])
                # print("output_branch_02:", output_branch_02)
                output_branch = {
                    "output_branch_00": output_branch_00,
                    "output_branch_01": output_branch_01,
                    "output_branch_02": output_branch_02
                }
                output_branches.append(output_branch)
                continue

            
            firsts = copy.copy(branch_00[count-1:])
            seconds = copy.copy(branch_01[count-1:])
            firsts.reverse()
            _ = firsts.pop(-1)

            thirds = firsts+seconds
            output_branch_02 = list()
            for third in thirds:
                c = json.loads(third)
                output_branch_02.append(c["type"])
            # print("output_branch_02:", output_branch_02)
            output_branch = {
                "output_branch_00": output_branch_00,
                "output_branch_01": output_branch_01,
                "output_branch_02": output_branch_02
            }
            output_branches.append(output_branch)

        
        return output_branches
    
    @staticmethod
    def _do_v3_v3(obj):
        sequence = list()
        def rec(now, have=list()):
            if now["children"]:
                for nxt in now["children"]:
                    had = copy.copy(have)
                    had.append(json.dumps(now))
                    rec(nxt, had)
            else:
                have.append(json.dumps(now))
                sequence.append(have)
        rec(obj, have=list())

        yoshikos = copy.copy(sequence)
        mahirus = copy.copy(sequence)
        _ = yoshikos.pop(-1)
        _ = mahirus.pop(0)

        output_branches = list()
        # for branch in itertools.combinations(sequence, 2):
        for yoshiko, mahiru in zip(yoshikos, mahirus):
            branch_00 = sorted(yoshiko, key=lambda x:len(x), reverse=True)
            branch_01 = sorted(mahiru, key=lambda x:len(x), reverse=True)
            output_branch_00 = list()
            output_branch_01 = list()
            for branch_0 in branch_00:
                c = json.loads(branch_0)
                output_branch_00.append(c["type"])
            for branch_1 in branch_01:
                c = json.loads(branch_1)
                output_branch_01.append(c["type"])



            if not branch_00:
                continue
            if not branch_01:
                continue

            if len(branch_00) <= 1:
                output_branch_02 = list()
                firsts = copy.copy(branch_00)
                seconds = copy.copy(branch_01)
                thirds = firsts+seconds
                for third in thirds:
                    c = json.loads(third)
                    output_branch_02.append(c["type"])
                print("output_branch_02:", output_branch_02)
                output_branch = {
                    "output_branch_00": output_branch_00,
                    "output_branch_01": output_branch_01,
                    "output_branch_02": output_branch_02
                }
                output_branches.append(output_branch)
                continue
            if len(branch_01) <= 1:
                output_branch_02 = list()
                firsts = copy.copy(branch_00)
                seconds = copy.copy(branch_01)
                firsts.reverse()
                _ = firsts.pop(-1)
                thirds = firsts+seconds
                for third in thirds:
                    c = json.loads(third)
                    output_branch_02.append(c["type"])
                # print("output_branch_02:", output_branch_02)
                output_branch = {
                    "output_branch_00": output_branch_00,
                    "output_branch_01": output_branch_01,
                    "output_branch_02": output_branch_02
                }
                output_branches.append(output_branch)
                continue


            if branch_00 == branch_01:
                firsts = copy.copy(branch_00)
                seconds = copy.copy(branch_01)
                thirds = [firsts[-1], firsts[-2], seconds[-1]]
                output_branch_02 = list()
                for third in thirds:
                    c = json.loads(third)
                    output_branch_02.append(c["type"])
                # print("output_branch_02:", output_branch_02)
                output_branch = {
                    "output_branch_00": output_branch_00,
                    "output_branch_01": output_branch_01,
                    "output_branch_02": output_branch_02
                }
                output_branches.append(output_branch)
                continue
            
            count = 0
            for branch_0, branch_1 in zip(branch_00, branch_01):
                if branch_0 != branch_1:
                    break
                count += 1
            
            if count == 0:
                firsts = copy.copy(branch_00)
                seconds = copy.copy(branch_01)
                firsts.reverse()
                thirds = firsts+["BASH-SCRIPT"]+seconds
                output_branch_02 = list()
                for third in thirds:
                    c = json.loads(third)
                    output_branch_02.append(c["type"])
                # print("output_branch_02:", output_branch_02)
                output_branch = {
                    "output_branch_00": output_branch_00,
                    "output_branch_01": output_branch_01,
                    "output_branch_02": output_branch_02
                }
                output_branches.append(output_branch)
                continue

            
            firsts = copy.copy(branch_00[count-1:])
            seconds = copy.copy(branch_01[count-1:])
            firsts.reverse()
            _ = firsts.pop(-1)

            thirds = firsts+seconds
            output_branch_02 = list()
            for third in thirds:
                c = json.loads(third)
                output_branch_02.append(c["type"])
            # print("output_branch_02:", output_branch_02)
            output_branch = {
                "output_branch_00": output_branch_00,
                "output_branch_01": output_branch_01,
                "output_branch_02": output_branch_02
            }
            output_branches.append(output_branch)

        
        return output_branches
    





def main():
    pass
    with open("../../data/gold/ffaef29733eba4016ab92139a635d8c58a9e782f.json", mode="r") as f:
        data = json.load(f)


if __name__ == "__main__":
    main()