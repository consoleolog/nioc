import pandas as pd

from provider.data_provider import DataProvider


class EMAProvider(DataProvider):

    def __init__(self, ema_opt):
        self.short = ema_opt['short']
        self.mid = ema_opt['mid']
        self.long = ema_opt['long']


    def get_data(self, data):
        ema_short = pd.Series(data).ewm(span=self.short, adjust=False).mean().values
        ema_mid = pd.Series(data).ewm(span=self.mid, adjust=False).mean().values
        ema_long = pd.Series(data).ewm(span=self.long, adjust=False).mean().values

        result = {
            "ema_short": ema_short,
            "ema_mid": ema_mid,
            "ema_long": ema_long
        }

        # STAGE 1  단 > 중 > 장
        if ema_short[-1] >= ema_mid[-1] >= ema_long[-1]:
            result["stage"] = 1
        # STAGE 2 중 > 단 > 장
        elif ema_mid[-1] >= ema_short[-1] >= ema_long[-1]:
            result["stage"] = 2
        # STAGE 3 중 > 장 > 단
        elif ema_mid[-1] >= ema_long[-1] >= ema_short[-1]:
            result["stage"] = 3
        # STAGE 4 장 > 중 > 단
        elif ema_long[-1] >= ema_mid[-1] >= ema_short[-1]:
            result["stage"] = 4
        # STAGE 5 장 > 단 > 중
        elif ema_long[-1] >= ema_short[-1] >= ema_mid[-1]:
            result["stage"] = 5
        # STAGE 6 단 > 장 > 중
        elif ema_short[-1] >= ema_mid[-1] >= ema_long[-1]:
            result["stage"] = 6

        return result