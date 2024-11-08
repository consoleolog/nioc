from abc import ABCMeta, abstractmethod


class DataRepository(metaclass=ABCMeta):

    @abstractmethod
    def select_by_ticker(self, ticker:str):
        """
        종목 코드로 데이터 가져오기
        :param ticker: str
        """
    @abstractmethod
    def create_table(self):
        """ 테이블 생성 """
    @abstractmethod
    def insert(self, *args):
        """ 데이터 하나 insert """