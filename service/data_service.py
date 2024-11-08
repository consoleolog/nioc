from abc import ABCMeta, abstractmethod


class DataService(metaclass=ABCMeta):

    @abstractmethod
    def current_status(self, data):
        """
        데이터 보고 현재 상태 판단
        :param data: {

        }
        :return:
        """