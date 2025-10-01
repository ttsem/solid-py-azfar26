import os

import pyodbc

from trade_record import TradeRecord


class TradeDatabase:
    CONNECTION_STRING = os.getenv("CONNECTION_STRING")

    def save_all(self, trades: list[TradeRecord]):
        with pyodbc.connect(self.CONNECTION_STRING) as conn:
            cursor = conn.cursor()
            try:
                for trade in trades:
                    cursor.execute(
                        "{CALL dbo.insert_trade (?, ?, ?, ?)}",
                        trade.source_currency,
                        trade.destination_currency,
                        trade.lots,
                        trade.price,
                    )
                conn.commit()
            except Exception:
                conn.rollback()
                raise
