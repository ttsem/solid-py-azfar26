class TradeRecord:
    def __init__(
        self, source_currency: str, destination_currency: str, lots: float, price: float
    ):
        """Entity that holds trade information"""
        self.source_currency = source_currency
        self.destination_currency = destination_currency
        self.lots = lots
        self.price = price
