from pyupbit import Upbit

from provider.env_provider import EnvProvider
from service.trader_service import TraderService

class UpbitService(TraderService):

    def __init__(self, env_provider: EnvProvider):
        super().__init__(env_provider)
        self.Upbit = Upbit(self.envs["upbitAccessKey"], self.envs["upbitSecretKey"])

    def create_buy(self, inputs):

        try :
            msg = self.Upbit.buy_market_order(f"KRW-{inputs['ticker']}", inputs['price'])
            if isinstance(msg, dict):
                self.logger.info(f" BUYING {inputs['ticker']}....")
            # self.send_mail({
            #     "content": f"{inputs['ticker']}"
            # })

        except Exception as error:
            self.logger.error(f"매수 하면서 에러났음 {str(error)}")
            raise UserWarning("create_buy ERROR") from error


    def create_sell(self, inputs):

        try:
            msg = self.Upbit.sell_market_order(f"KRW-{inputs['ticker']}", inputs['amount'])
            if isinstance(msg, dict):
                self.logger.info(f" SELLING {inputs['ticker']}....")

        except Exception as error:
            self.logger.error(f"매도 하면서 에러났음 {str(error)}")
            raise UserWarning("create_sell ERROR") from error