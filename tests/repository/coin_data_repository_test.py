import sys
import os

from container import Container

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest



class CoinDataRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.container = Container()

    def test_create_table(self):
        self.container.coin_data_repository.create_table()


