from typing import TextIO

from trade_record import TradeRecord


class TradeParser:
    LOT_SIZE = 100000.0

    def parse(self, stream: TextIO) -> list[TradeRecord]:
        """Parses trades from a text stream"""
        trades = []
        line_count = 1

        for raw_line in stream:
            line = raw_line.strip()
            if not line:
                continue

            fields = line.split(",")

            if not self._validate_fields(fields, line_count):
                line_count += 1
                continue

            try:
                trade_amount = int(fields[1])
                trade_price = float(fields[2])
            except ValueError as e:
                print(f"WARN: Parsing error on line {line_count}: {e}")
                line_count += 1
                continue

            source_currency = fields[0][:3]
            destination_currency = fields[0][3:]

            trades.append(
                TradeRecord(
                    source_currency,
                    destination_currency,
                    trade_amount / self.LOT_SIZE,
                    trade_price,
                )
            )
            line_count += 1

        return trades

    def _validate_fields(self, fields: list, line_count: int) -> bool:
        if len(fields) != 3:
            print(
                f"WARN: Line {line_count} malformed. Only {len(fields)} field(s) found."
            )
            return False

        if len(fields[0]) != 6:
            print(
                f"WARN: Trade currencies on line {line_count} malformed: '{fields[0]}'"
            )
            return False

        return True
