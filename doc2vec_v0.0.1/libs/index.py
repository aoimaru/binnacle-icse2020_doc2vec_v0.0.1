import json
import os

INDEX_ROOT_PATH = "/Users/nakamurahekikai/Desktop/binnacle-icse2020_doc2vec_v0.0.1/index"

class Index(object):
    @staticmethod
    def _create(training_data, file_name):
        """
            1つのファイルに全ての情報を格納
        """
        file_path = "{index_root_path}/{file_name}".format(
            index_root_path=INDEX_ROOT_PATH,
            file_name=file_name
        )
        with open(file_path, mode="w") as f:
            try:
                json.dump(training_data, f, indent=4)
            except Exception as e:
                print(e)
    
    @staticmethod
    def _create_v2(training_data_v2, target):
        dst_file_dir = "{index_root_path}/{dst_file_dir}".format(
            index_root_path=INDEX_ROOT_PATH,
            dst_file_dir=target
        )
        try:
            os.mkdir(dst_file_dir)
        except Exception as e:
            print(e)

        for tr_key, training_data in training_data_v2.items():
            file_path = "{index_root_path}/{dst_file_dir}/{file_name}".format(
                index_root_path=INDEX_ROOT_PATH,
                dst_file_dir=target,
                file_name="{}.json".format(tr_key)
            )
            with open(file_path, mode="w") as f:
                try:
                    json.dump(training_data, f, indent=4)
                except Exception as e:
                    print(e)
            
    
    @staticmethod
    def _get_file(file_name):
        file_path = "{index_root_path}/{file_name}".format(
            index_root_path=INDEX_ROOT_PATH,
            file_name=file_name
        )
        with open(file_path, mode="r") as f:
            data = json.load(f)
        return data


