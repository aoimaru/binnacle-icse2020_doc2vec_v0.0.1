from libs.files import *
from libs.calcs import *
from libs.cleanings import *
from libs.contents import *

import sys
import pprint

OPTION_01 = 1

def main(args):
    file_paths = JsonFile._get_file_path(target=args[OPTION_01])
    for file_path in file_paths:
        sequence_dict = RUNContent._get_sequence(file_path)
        for sequence_key, sequence_values in sequence_dict.items():
            print(sequence_key)
            sequences = CleanRUN._Disassembly(sequence_values)
            for sequence in sequences:
                print()
                pprint.pprint(sequence)




if __name__ == "__main__":
    main(sys.argv)