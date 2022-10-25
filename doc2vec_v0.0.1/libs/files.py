from abc import *

import json
import glob

DATA_ROOT_PATH = "/Users/nakamurahekikai/Desktop/binnacle-icse2020_doc2vec_v0.0.1/data"

NEW_INDEX_01_PATH = "/Users/nakamurahekikai/Desktop/binnacle-icse2020_doc2vec_v0.0.1/new_index_01"
NEW_INDEX_02_PATH = "/Users/nakamurahekikai/Desktop/binnacle-icse2020_doc2vec_v0.0.1/new_index_02"

class File(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def _get_contents():
        pass

    @staticmethod
    @abstractmethod
    def _get_file_path():
        pass

    @staticmethod
    @abstractmethod
    def _create_new_index_01_path():
        pass
    
    @staticmethod
    @abstractmethod
    def _create_new_index_02_path():
        pass

class JsonFile(File):
    @staticmethod
    def _get_contents(file_path: str):
        try:
            with open(file_path, mode="r") as f:
                contents = json.load(f)
        except Exception as e:
            print(e)
            return []
        else:
            return contents
        
    @staticmethod
    def _get_file_path(target: str):
        return glob.glob(
            "{data_root_path}/{target}/**/*.json".format(
                data_root_path=DATA_ROOT_PATH,
                target=target
            ),
            recursive=True
        )
    
    @staticmethod
    def _create_new_index_01_path(target, file_id, objs):
        file_path = "{new_index_01}/{target}/{file_id}.json".format(
            new_index_01=NEW_INDEX_01_PATH,
            target=target,
            file_id=file_id
        )
        try:
            with open(file_path, mode="w") as f:
                json.dump(objs, f, indent=4)
        except Exception as e:
            print(e)
        else:
            print("status: OK")
    

    @staticmethod
    def _create_new_index_02_path(target, file_id, objs):
        file_path = "{new_index_02}/{target}/{file_id}.json".format(
            new_index_02=NEW_INDEX_02_PATH,
            target=target,
            file_id=file_id
        )
        try:
            with open(file_path, mode="w") as f:
                json.dump(objs, f, indent=4)
        except Exception as e:
            print(e)
        else:
            print("status: OK")
            
