from abc import *

class Filter(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def _do():
        pass

class RUNFilter(Filter):
    @staticmethod
    def _do():
        pass