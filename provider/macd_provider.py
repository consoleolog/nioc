import numpy as np

from provider.data_provider import DataProvider


class MACDProvider(DataProvider):
    def __init__(self, ema_opt):
        self.short = ema_opt['short']
        self.mid = ema_opt['mid']
        self.long = ema_opt['long']


    def get_data(self, data):

        ema_short = np.array(data["ema_short"])
        ema_mid = np.array(data["ema_mid"])
        ema_long = np.array(data["ema_long"])

        return {
            "macd_up": ema_short - ema_mid,   # ( 상 )
            "macd_mid": ema_short - ema_long, # ( 중 )
            "macd_low": ema_mid - ema_long    # ( 하 )
        }


