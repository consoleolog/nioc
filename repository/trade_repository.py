from sqlite3 import Connection

from repository.data_repository import DataRepository


class TradeRepository(DataRepository):
    def __init__(self, connection: Connection):
        self.connection = connection
        self.db = self.connection.cursor()

    def create_table(self):
        self.db.execute("""
        create table if not exists trade_data(
            id integer primary key autoincrement ,
            date timestamp not null ,
            ticker varchar(10) not null ,
            mode varchar(10) not null ,
            price float not null ,
            market_price float not null
        );
        """)

    def select_by_ticker(self, ticker):
        self.db.execute("""
        select t.id,
               t.date,
               t.ticker,
               t.mode,
               t.price,
               t.market_price
        from trade_history t where t.market=? order by t.id limit 10;
        """, (ticker,))
        return self.db.fetchall()

    def insert(self, ticker, mode, price, market_price):
        self.db.execute("""
        insert into trade_data(
            date,
            ticker,
            mode,
            price,
            market_price,
        ) values (CURRENT_TIMESTAMP, ?, ?, ?, ?)
        """, (ticker, mode, price, market_price))
        self.connection.commit()
