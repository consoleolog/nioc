import os
import sqlite3
from os.path import dirname, join

from provider.ema_provider import EMAProvider
from provider.env_provider import EnvProvider
from provider.macd_provider import MACDProvider
from provider.upbit_provider import UpbitProvider
from repository.coin_repository import CoinRepository
from repository.trade_repository import TradeRepository
from service.upbit_service import UpbitService


class Container:

    db = sqlite3.connect(f"{os.getcwd()}/nioc.sqlite")

    def __init__(self, opt):
        self.__coin_repository = CoinRepository(self.db)
        self.__trade_repository = TradeRepository(self.db)

        self.__ema_provider = EMAProvider(opt)
        self.__macd_provider = MACDProvider(opt)
        self.__upbit_provider = UpbitProvider(opt)
        self.__env_provider = EnvProvider(join(dirname(__file__), '.env'))

        self.__upbit_service = UpbitService(self.env_provider)

    @property
    def coin_repository(self):
        return self.__coin_repository

    @property
    def trade_repository(self):
        return self.__trade_repository

    @property
    def ema_provider(self):
        return self.__ema_provider

    @property
    def macd_provider(self):
        return self.__macd_provider

    @property
    def upbit_provider(self):
        return self.__upbit_provider

    @property
    def env_provider(self):
        return self.__env_provider

    @property
    def upbit_service(self):
        return self.__upbit_service
