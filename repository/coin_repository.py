from sqlite3 import Connection

from repository.data_repository import DataRepository


class CoinRepository(DataRepository):
    def __init__(self, connection: Connection):
        self.connection = connection
        self.db = self.connection.cursor()

    def create_table(self):
        self.db.execute("""
        create table if not exists coin_data(
            id integer primary key autoincrement ,
            interval varchar(10) not null,
            date timestamp not null,
            ticker varchar(10) not null ,
            stage integer not null ,
            close float not null ,
            ema_short float not null ,
            ema_mid float not null ,
            ema_long float not null ,
            macd_up float not null ,
            macd_mid float not null ,
            macd_low float not null 
        );
        """)

    def select_by_ticker(self, ticker):
        self.db.execute("""
        select c.id,
               c.interval,
               c.date, 
               c.ticker,
               c.stage,
               c.close,
               c.ema_short,
               c.ema_mid,
               c.ema_long,
               c.macd_up,
               c.macd_mid,
               c.macd_low
         from coin_data c where c.ticker=? order by c.id desc limit 10;
        """, (ticker,))
        return self.db.fetchall()

    def select_by_ticker_and_interval(self, ticker, interval):
        self.db.execute("""
        select c.id,
               c.interval,
               c.date, 
               c.ticker,
               c.stage,
               c.close,
               c.ema_short,
               c.ema_mid,
               c.ema_long,
               c.macd_up,
               c.macd_mid,
               c.macd_low
         from coin_data c where c.ticker=? and c.interval=? order by c.id desc limit 10;
        """, (ticker, interval))
        return self.db.fetchall()


    def insert(self, interval, ticker, stage, close, ema_short, ema_mid, ema_long, macd_up, macd_mid, macd_low):
        self.db.execute("""
        insert into coin_data(
            interval,
            date,
            ticker,
            stage,
            close,
            ema_short,
            ema_mid,
            ema_long,
            macd_up,
            macd_mid,
            macd_low
        ) values (?, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (interval, ticker, stage, close, ema_short, ema_mid, ema_long, macd_up, macd_mid, macd_low))
        self.connection.commit()

