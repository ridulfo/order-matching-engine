from ordermatchinengine.Order import *
from time import time

class Trade(object):
	"""
	Trade
	-----

	A trade object
	"""
	def __init__(self, incoming_side: Side, price: float, trade_size: int, incoming_order_id: int, book_order_id: int):
		self.timestamp = int(1e6 * time())
		self.side = incoming_side
		self.price = price
		self.size = trade_size
		self.incoming_order_id = incoming_order_id
		self.book_order_id = book_order_id

	def __repr__(self):
		return 'Executed: {0} {1} units at {2}'.format(self.side, self.size, self.price)
