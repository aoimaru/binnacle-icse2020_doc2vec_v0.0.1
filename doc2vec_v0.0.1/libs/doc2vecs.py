from abc import *

from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

MODEL_ROOT_PATH = "/Users/nakamurahekikai/Desktop/binnacle-icse2020_doc2vec_v0.0.1/model"

class D2V(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def _get_documents():
        pass
    
    @staticmethod
    @abstractmethod
    def _do():
        pass
    
    @staticmethod
    def _load_model(model_path):
        return Doc2Vec.load(model_path)

class D2V_V1(D2V):
    @staticmethod
    def _get_documents(training_data):
        documents = [
            TaggedDocument(tr_value, [tr_key]) for tr_key, tr_value in training_data.items()
        ]
        return documents
    
    @staticmethod
    def _do(documents, model_path):
        model = Doc2Vec(documents, vector_size=10, window=5, min_count=1, workers=4, dm=1)
        model.save(model_path)

