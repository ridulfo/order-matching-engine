from enum import Enum
from time import time

class Side(Enum):
    BUY = 0
    SELL = 1

class Order(object):
    def __init__(self, order_id: int):
        self.order_id = order_id
        self.time = int(1e6 * time())
    
    def __getType__(self):
        return self.__class__


class CancelOrder(Order):
    def __init__(self, order_id):
        super().__init__(order_id)

    def __repr__(self):
        return "Cancel Order: {}.".format(self.order_id)


class MarketOrder(Order):
    def __init__(self, order_id: int, side: Side, size: int):
        super().__init__(order_id)
        self.side = side
        self.size = self.remainingToFill = size
    
    def __repr__(self):
        return "Market Order: {0} {1} units.".format(
            "BUY" if self.side == Side.BUY else "SELL",
            self.RemainingToFill)



class LimitOrder(MarketOrder):
    def __init__(self, order_id: int, side: Side, size: int, price: int):
        super().__init__(order_id, side, size)
        self.price = price
    
    def __lt__(self, other):
        if self.price != other.price:
            if self.side == Side.BUY:
                return self.price > other.price
            else:
                return self.price < other.price

        elif self.time != other.time:
             return self.time < other.time

        elif self.size != other.size:
            self.size < other.size

    def __repr__(self):
        return 'Limit Order: {0} {1} units at {2}.'.format(
            "BUY" if self.side == Side.BUY else "SELL",
            self.remainingToFill, self.price)
