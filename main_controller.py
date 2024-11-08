from container import Container


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

    def coin_data(interval):
        return container.coin_repository.select_by_ticker_and_interval(ticker, interval)

    try :
        for i in intervals:
            save_coin_data(i)
            print(coin_data(i))

    except Exception as error:
        raise UserWarning("어디선가 에러가 났음") from error

start("BTC")