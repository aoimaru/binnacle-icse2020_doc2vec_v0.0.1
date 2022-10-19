from libs.files import *
from libs.calcs import *
from libs.cleanings import *
from libs.contents import *
from libs.trs import *
from libs.doc2vecs import *
from libs.index import *

import sys
import pprint
import numpy as np

OPTION_01 = 1

def main(args):
    file_paths = JsonFile._get_file_path(target=args[OPTION_01])
    training_data =  TR_V1._get_training_data(file_paths)
    Tokens = dict()
    for tr_tokens in training_data.values():
        for tr_token in tr_tokens:
            if not tr_token in Tokens:
                Tokens[tr_token] = 0
            Tokens[tr_token] += 1
    
    pprint.pprint(Tokens)



if __name__ == "__main__":
    main(sys.argv)