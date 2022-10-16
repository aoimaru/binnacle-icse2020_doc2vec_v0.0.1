from libs.files import *

import sys

OPTION_01 = 1

def main(args):
    file_paths = JsonFile._get_file_path(target=args[OPTION_01])
    for file_path in file_paths:
        print(file_path)


if __name__ == "__main__":
    main(sys.argv)