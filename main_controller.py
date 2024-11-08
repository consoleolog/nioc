from container import Container
from multiprocessing.dummy import Pool as ThreadPool



def start(ticker):
    container = Container({
        "short": 15,
        "mid": 40,
        "long": 60,
        "ticker": f"KRW-{ticker}"
    })

    container.coin_repository.create_table()

    intervals = ["minutes1", "minutes3", "minutes5", "minutes5", "minutes10", "minutes15", "minutes30", "minutes60"]

    def save_coin_data(interval):
        close = container.upbit_provider.get_data(interval)
        ema_and_stage = container.ema_provider.get_data(close)
        macd = container.macd_provider.get_data(ema_and_stage)

        container.coin_repository.insert(
            ticker=ticker,
            interval=interval,
            close=close[-1],
            stage=ema_and_stage["stage"],
            ema_short=ema_and_stage["ema_short"][-1],
            ema_mid=ema_and_stage["ema_mid"][-1],
            ema_long=ema_and_stage["ema_long"][-1],
            macd_up=macd["macd_up"][-1],
            macd_mid=macd["macd_mid"][-1],
            macd_low=macd["macd_low"][-1]
        )

    try :
        for interval in intervals:
            save_coin_data(interval)

        # # DEFAULT TRADING
        # close_m1 = container.upbit_provider.get_data("minutes1")
        # ema_and_stage_m1 =  container.ema_provider.get_data(close_m1)
        # macd_m1 = container.macd_provider.get_data(ema_and_stage_m1)
        #
        # container.coin_repository.create_table()
        #
        # container.coin_repository.insert(
        #     ticker=ticker,
        #     interval="minutes1",
        #     close=close_m1[-1],
        #     stage=ema_and_stage_m1["stage"],
        #     ema_short=ema_and_stage_m1["ema_short"][-1],
        #     ema_mid=ema_and_stage_m1["ema_mid"][-1],
        #     ema_long=ema_and_stage_m1["ema_long"][-1],
        #     macd_up=macd_m1["macd_up"][-1],
        #     macd_mid=macd_m1["macd_mid"][-1],
        #     macd_low=macd_m1["macd_low"][-1]
        # )
        #
        # data = container.coin_repository.select_by_ticker(ticker="BTC")
        #
        # # SETTING COMPARE DATA
        # close_m3 = container.upbit_provider.get_data("minutes3")
        # ema_and_stage_m3 = container.ema_provider.get_data(close_m3)
        # macd_m3 = container.macd_provider.get_data(ema_and_stage_m3)
        #
        # container.coin_repository.insert(
        #     ticker=ticker,
        #     interval="minutes3",
        #     close=close_m3[-1],
        #     stage=ema_and_stage_m3["stage"],
        #     ema_short=ema_and_stage_m3["ema_short"][-1],
        #     ema_mid=ema_and_stage_m3["ema_mid"][-1],
        #     ema_long=ema_and_stage_m3["ema_long"][-1],
        #     macd_up=macd_m3["macd_up"][-1],
        #     macd_mid=macd_m3["macd_mid"][-1],
        #     macd_low=macd_m3["macd_low"][-1]
        # )
        #
        # close_m5 = container.upbit_provider.get_data("minutes5")
        # ema_and_stage_m5 = container.ema_provider.get_data(close_m5)
        # macd_m5 = container.macd_provider.get_data(ema_and_stage_m5)
        #
        # container.coin_repository.insert(
        #     ticker=ticker,
        #     interval="minutes5",
        #     close=close_m5[-1],
        #     stage=ema_and_stage_m5["stage"],
        #     ema_short=ema_and_stage_m5["ema_short"][-1],
        #     ema_mid=ema_and_stage_m5["ema_mid"][-1],
        #     ema_long=ema_and_stage_m5["ema_long"][-1],
        #     macd_up=macd_m5["macd_up"][-1],
        #     macd_mid=macd_m5["macd_mid"][-1],
        #     macd_low=macd_m5["macd_low"][-1]
        # )
        #
        # close_m10 = container.upbit_provider.get_data("minutes10")
        # ema_and_stage_m10 = container.ema_provider.get_data(close_m10)
        # macd_m10 = container.macd_provider.get_data(ema_and_stage_m10)
        #
        # container.coin_repository.insert(
        #     ticker=ticker,
        #     interval="minutes10",
        #     close=close_m10[-1],
        #     stage=ema_and_stage_m10["stage"],
        #     ema_short=ema_and_stage_m10["ema_short"][-1],
        #     ema_mid=ema_and_stage_m10["ema_mid"][-1],
        #     ema_long=ema_and_stage_m10["ema_long"][-1],
        #     macd_up=macd_m10["macd_up"][-1],
        #     macd_mid=macd_m10["macd_mid"][-1],
        #     macd_low=macd_m10["macd_low"][-1]
        # )
        #
        # close_m15 = container.upbit_provider.get_data("minutes15")
        # ema_and_stage_m15 = container.ema_provider.get_data(close_m15)
        # macd_m15 = container.macd_provider.get_data(ema_and_stage_m15)
        #
        # container.coin_repository.insert(
        #     ticker=ticker,
        #     interval="minutes15",
        #     close=close_m15[-1],
        #     stage=ema_and_stage_m15["stage"],
        #     ema_short=ema_and_stage_m15["ema_short"][-1],
        #     ema_mid=ema_and_stage_m15["ema_mid"][-1],
        #     ema_long=ema_and_stage_m15["ema_long"][-1],
        #     macd_up=macd_m15["macd_up"][-1],
        #     macd_mid=macd_m15["macd_mid"][-1],
        #     macd_low=macd_m15["macd_low"][-1]
        # )
        #
        # close_m30 = container.upbit_provider.get_data("minutes30")
        # ema_and_stage_m30 = container.ema_provider.get_data(close_m30)
        # macd_m30 = container.macd_provider.get_data(ema_and_stage_m30)
        #
        # container.coin_repository.insert(
        #     ticker=ticker,
        #     interval="minutes30",
        #     close=close_m10[-1],
        #     stage=ema_and_stage_m10["stage"],
        #     ema_short=ema_and_stage_m10["ema_short"][-1],
        #     ema_mid=ema_and_stage_m30["ema_mid"][-1],
        #     ema_long=ema_and_stage_m30["ema_long"][-1],
        #     macd_up=macd_m30["macd_up"][-1],
        #     macd_mid=macd_m30["macd_mid"][-1],
        #     macd_low=macd_m30["macd_low"][-1]
        # )
        #
        # close_m60 = container.upbit_provider.get_data("minutes60")
        # ema_and_stage_m60 = container.ema_provider.get_data(close_m60)
        # macd_m60 = container.macd_provider.get_data(ema_and_stage_m60)
        #
        # container.coin_repository.insert(
        #     ticker=ticker,
        #     interval="minutes60",
        #     close=close_m60[-1],
        #     stage=ema_and_stage_m60["stage"],
        #     ema_short=ema_and_stage_m60["ema_short"][-1],
        #     ema_mid=ema_and_stage_m60["ema_mid"][-1],
        #     ema_long=ema_and_stage_m60["ema_long"][-1],
        #     macd_up=macd_m60["macd_up"][-1],
        #     macd_mid=macd_m60["macd_mid"][-1],
        #     macd_low=macd_m60["macd_low"][-1]
        # )
        #
        # close_m240 = container.upbit_provider.get_data("minutes240")
        # ema_and_stage_m240 = container.ema_provider.get_data(close_m240)
        # macd_m240 = container.macd_provider.get_data(ema_and_stage_m240)
        #
        #


    except Exception as error:
        raise UserWarning("어디선가 에러가 났음") from error

start("BTC")