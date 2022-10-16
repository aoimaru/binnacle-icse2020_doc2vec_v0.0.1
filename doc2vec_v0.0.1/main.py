from libs.files import *
from libs.calcs import *
from libs.cleanings import *
from libs.contents import *
from libs.trs import *
from libs.doc2vecs import *
from libs.index import *

import sys
import pprint

OPTION_01 = 1
MODEL_ROOT_PATH = "/Users/nakamurahekikai/Desktop/binnacle-icse2020_doc2vec_v0.0.1/model"

def create_model(target):
    file_paths = JsonFile._get_file_path(target=target)
    training_data =  TR_V1._get_training_data(file_paths)
    print("len(training_data):", len(training_data))
    documents = D2V_V1._get_documents(training_data)
    print("len(documents):", len(documents))
    D2V_V1._do(documents, model_path="{model_root_path}/{model_name}".format(
        model_root_path=MODEL_ROOT_PATH,
        model_name="{}.model".format(target)
    ))

def check_model(model_path):
    v1_index = Index._get_file("github.json")
    model = D2V_V1._load_model(model_path)
    for result in model.docvecs.most_similar("f39b64a71b6a95e1347fa05cbec2e56e6073cdeb:3:0"):
        print(result)
        pprint.pprint(v1_index[result[0]])
    
def create_index(target):
    file_paths = JsonFile._get_file_path(target=target)
    training_data =  TR_V1._get_training_data(file_paths)
    Index._create(training_data, "{}.json".format(target))



def main(args):
    # create_model(target=args[OPTION_01])
    # create_index(args[OPTION_01])
    # model_path="{model_root_path}/{model_name}".format(
    #     model_root_path=MODEL_ROOT_PATH,
    #     model_name="{}.model".format(args[OPTION_01])
    # )
    # check_model(model_path)

    file_paths = JsonFile._get_file_path(target=args[OPTION_01])
    training_data_v2 = TR_V1._get_training_data_v2(file_paths)
    Index._create_v2(training_data_v2, args[OPTION_01])







if __name__ == "__main__":
    main(sys.argv)