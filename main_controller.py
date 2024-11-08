from container import Container


def start(ticker):
    container = Container({
        "short": 15,
        "mid": 40,
        "long": 60,
        "ticker": f"KRW-{ticker}"
    })

    try :

        close_prices = container.upbit_provider.get_data("minutes1")
        ema_and_stage =  container.ema_provider.get_data(close_prices)

        macd = container.macd_provider.get_data(ema_and_stage)

        container.coin_repository.create_table()

        container.coin_repository.insert(
            ticker="BTC",
            close=close_prices[-1],
            stage=ema_and_stage["stage"],
            ema_short=ema_and_stage["ema_short"][-1],
            ema_mid=ema_and_stage["ema_mid"][-1],
            ema_long=ema_and_stage["ema_long"][-1],
            macd_up=macd["macd_up"][-1],
            macd_mid=macd["macd_mid"][-1],
            macd_low=macd["macd_low"][-1]
        )

        data = container.coin_repository.select_by_ticker(ticker="BTC")

    except Exception as e:
        print(e)

start("BTC")