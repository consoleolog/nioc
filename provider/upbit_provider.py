import os

import pyupbit
from pyupbit import Upbit

from custom_logging import CustomLogger
from provider.data_provider import DataProvider

from dotenv import load_dotenv

load_dotenv()

class UpbitProvider(DataProvider):

    def __init__(self, data_opt):
        self.UPBIT = Upbit(os.getenv('UPBIT_ACCESS_KEY'), os.getenv('UPBIT_SECRET_KEY'))
        self.market = ""
        self.logger = CustomLogger().get_logger(__class__.__name__)
        self.data_opt = data_opt

    def get_data(self, interval):
        df = pyupbit.get_ohlcv(ticker=self.data_opt["ticker"], interval=interval , count=200)

        return df["close"].values
