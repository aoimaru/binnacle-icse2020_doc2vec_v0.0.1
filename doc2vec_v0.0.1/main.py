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
MODEL_ROOT_PATH = "/Users/nakamurahekikai/Desktop/binnacle-icse2020_doc2vec_v0.0.1/model"
INDEX_ROOT_PATH = "/Users/nakamurahekikai/Desktop/binnacle-icse2020_doc2vec_v0.0.1/index"


def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

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

def create_trace_model(target):
    file_paths = JsonFile._get_file_path(target=target)
    trace_training_data =  TR_V1._get_trace_training_data(file_paths)
    print("len(trace_training_data):", len(trace_training_data))
    documents = D2V_V1._get_documents(trace_training_data)
    print("len(documents):", len(documents))
    D2V_V1._do(documents, model_path="{model_root_path}/{model_name}".format(
        model_root_path=MODEL_ROOT_PATH,
        model_name="trace-{}.model".format(target)
    ))



def check_model(model_path, target, file_id):
    index_path = "{index_root_path}/{target}".format(
        index_root_path=INDEX_ROOT_PATH,
        target=target
    )
    target_id = file_id.split(":")[0]; target_path = "{}/{}.json".format(index_path, target_id)
    target_contents = Index._get_file(target_path)
    pprint.pprint(target_contents[file_id])
    model = D2V_V1._load_model(model_path)
    for result in model.docvecs.most_similar(file_id):
        print(result)
        file_id = result[0].split(":")[0]; file_path = "{}/{}.json".format(index_path, file_id)
        result_contents = Index._get_file(file_path=file_path)
        pprint.pprint(result_contents[result[0]])

def check_model_v2(model_path, file_id):
    model = D2V_V1._load_model(model_path)
    # vector = model.infer_vector(file_id)
    vector = model[file_id]
    print(vector)


    
def create_index(target):
    file_paths = JsonFile._get_file_path(target=target)
    training_data =  TR_V1._get_training_data_v2(file_paths)
    Index._create_v2(training_data, "{}".format(target))


def compare_v1(model_path, target, file_id_01, file_id_02):

    index_path = "{index_root_path}/{target}".format(
        index_root_path=INDEX_ROOT_PATH,
        target=target
    )

    file_01 = file_id_01.split(":")[0]; file_path_01 = "{}/{}.json".format(index_path, file_01)
    contents_01 = Index._get_file(file_path_01)
    pprint.pprint(contents_01[file_id_01])
    print()
    file_02 = file_id_02.split(":")[0]; file_path_02 = "{}/{}.json".format(index_path, file_02)
    contents_02 = Index._get_file(file_path_02)
    pprint.pprint(contents_02[file_id_02])
    print()

    model = D2V_V1._load_model(model_path)
    vector_01 = model[file_id_01]; vector_02 = model[file_id_02]
    print(cos_sim(vector_01, vector_02))


def main(args):
    # create_model(target=args[OPTION_01])
    # create_index(args[OPTION_01])
    model_path="{model_root_path}/{model_name}".format(
        model_root_path=MODEL_ROOT_PATH,
        model_name="{}.model".format(args[OPTION_01])
    )
    # check_model(model_path, args[OPTION_01], "f39b64a71b6a95e1347fa05cbec2e56e6073cdeb:3:0")
    # check_model(model_path, args[OPTION_01], "636b8940f290f0557d21f498a240cbb2fc89d5a4:8:3")
    # check_model_v2(model_path, "636b8940f290f0557d21f498a240cbb2fc89d5a4:8:3")
    # check_model_v2(model_path, "281ec5c0177461d29279dd471dd82e7c5dbd526a:1:1")

    # compare_v1(
    #     model_path,
    #     args[OPTION_01],
    #     "df14a602bcd653559e635eb000a9a48180add800:3:1",
    #     "281ec5c0177461d29279dd471dd82e7c5dbd526a:1:1"
    # )

    # compare_v1(
    #     model_path,
    #     args[OPTION_01],
    #     "df14a602bcd653559e635eb000a9a48180add800:3:1",
    #     "a62087e4b0d69dd5fe7e9a825f2c66e555d882d3:7:0"
    # )
    # compare_v1(
    #     model_path,
    #     args[OPTION_01],
    #     "df14a602bcd653559e635eb000a9a48180add800:3:1",
    #     "785213f529f1855dd78041d27adf7bd608070510:1:1"
    # )

    # file_paths = JsonFile._get_file_path(target=args[OPTION_01])
    # trace_training_data = TR_V1._get_trace_training_data(file_paths)
    # for key, value in trace_training_data.items():
    #     print(value)

    # file_paths = JsonFile._get_file_path(target=args[OPTION_01])
    # training_data_v2 = TR_V1._get_training_data_v2(file_paths)
    # Index._create_v2(training_data_v2, args[OPTION_01])
    
    
    # create_trace_model(args[OPTION_01])
    # create_index(args[OPTION_01])

    trace_model_path="{model_root_path}/{model_name}".format(
        model_root_path=MODEL_ROOT_PATH,
        model_name="trace-{}.model".format(args[OPTION_01])
    )


    # compare_v1(
    #     trace_model_path,
    #     args[OPTION_01],
    #     "df14a602bcd653559e635eb000a9a48180add800:3:1",
    #     "281ec5c0177461d29279dd471dd82e7c5dbd526a:1:1"
    # )

    # compare_v1(
    #     trace_model_path,
    #     args[OPTION_01],
    #     "df14a602bcd653559e635eb000a9a48180add800:3:1",
    #     "a62087e4b0d69dd5fe7e9a825f2c66e555d882d3:7:0"
    # )
    # compare_v1(
    #     trace_model_path,
    #     args[OPTION_01],
    #     "df14a602bcd653559e635eb000a9a48180add800:3:1",
    #     "785213f529f1855dd78041d27adf7bd608070510:1:1"
    # )


    # check_model(trace_model_path, args[OPTION_01], "a62087e4b0d69dd5fe7e9a825f2c66e555d882d3:3:1")
    # check_model(trace_model_path, args[OPTION_01], "ca4acdafd2a1886c6fe0440e939eded376856338:2:0")
    # check_model(trace_model_path, args[OPTION_01], "d81fcee655ef5116135f0e27bc8adaaa1f51e8a4:2:1")


    check_model(trace_model_path, args[OPTION_01], "afterthedeadline:4:0")





if __name__ == "__main__":
    main(sys.argv)