from abc import *


class TR(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def _get_training_data():
        pass