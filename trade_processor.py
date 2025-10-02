from typing import TextIO

from trade_database import TradeDatabase
from trade_parser import TradeParser


def process_trades(stream: TextIO):
    trades = TradeParser().parse(stream)
    TradeDatabase().save_all(trades)
    print(f"INFO: {len(trades)} trades processed")


if __name__ == "__main__":
    with open("trades.txt", "r") as trade_file:
        process_trades(trade_file)
