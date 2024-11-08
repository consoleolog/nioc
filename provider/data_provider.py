from abc import ABCMeta, abstractmethod


class DataProvider(metaclass=ABCMeta):

    @abstractmethod
    def get_data(self, **args):
        """
        각자 역할에 맞는 데이터 반환
        """