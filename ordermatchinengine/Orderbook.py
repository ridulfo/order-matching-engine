from ordermatchinengine.Order import *
from ordermatchinengine.Trade import *
from sortedcontainers import SortedList


class Orderbook(object):
	"""
	An orderbook.
	-------------

	It can store and process orders.
	"""
	def __init__(self):
		self.bids: SortedList[Order] = SortedList()
		self.asks: SortedList[Order] = SortedList()
		self.trades = []

	def process_order(self, incoming_order):
		"""
		Processes an order

		Depending on the type of order the following can happen:
		- Market Order
		- Limit Order
		- Cancel Order
		"""

		if incoming_order.__class__ == CancelOrder:
			for order in self.bids:
				if incoming_order.order_id == order.order_id:
					self.bids.discard(order)
					break

			for order in self.asks:
				if incoming_order.order_id == order.order_id:
					self.asks.discard(order)
					break
			
			return # Exiting process order

		def while_clause():
			"""
			Determined whether to continue the while-loop
			"""
			if incoming_order.side==Side.BUY:
				if incoming_order.__class__ == LimitOrder:
					return len(self.asks) > 0 and incoming_order.price >= self.asks[0].price # Limit order on the BUY side
				elif incoming_order.__class__ == MarketOrder:
					return len(self.asks) > 0 # Market order on the BUY side
			else:
				if incoming_order.__class__ == LimitOrder:
					return len(self.bids) > 0 and incoming_order.price <= self.bids[0].price # Limit order on the SELL side
				elif incoming_order.__class__ == MarketOrder:
					return len(self.bids) > 0 # Market order on the SELL side

		# while there are orders and the orders requirements are matched
		while while_clause():
			bookOrder = None
			if incoming_order.side==Side.BUY:
				bookOrder = self.asks.pop(0)
			else:
				bookOrder = self.bids.pop(0)

			if incoming_order.remaining == bookOrder.remaining:  # if the same volume
				volume = incoming_order.remaining
				incoming_order.remaining -= volume
				bookOrder.remaining -= volume
				self.trades.append(Trade(
					incoming_order.side, bookOrder.price, volume, incoming_order.order_id, bookOrder.order_id))
				break

			elif incoming_order.remaining > bookOrder.remaining:  # incoming has greater volume
				volume = bookOrder.remaining
				incoming_order.remaining -= volume
				bookOrder.remaining -= volume
				self.trades.append(Trade(
					incoming_order.side, bookOrder.price, volume, incoming_order.order_id, bookOrder.order_id))

			elif incoming_order.remaining < bookOrder.remaining:  # book has greater volume
				volume = incoming_order.remaining
				incoming_order.remaining -= volume
				bookOrder.remaining -= volume
				self.trades.append(Trade(
					incoming_order.side, bookOrder.price, volume, incoming_order.order_id, bookOrder.order_id))

				if bookOrder.side==Side.SELL:
					self.asks.add(bookOrder)
				else:
					self.bids.add(bookOrder)
				break

		if incoming_order.remaining > 0 and incoming_order.__class__ == LimitOrder:
			if incoming_order.side == Side.BUY:
				self.bids.add(incoming_order)
			else:
				self.asks.add(incoming_order)

	def get_bid(self): return self.bids[0].price if len(self.bids)>0 else None
	def get_ask(self): return self.asks[0].price if len(self.asks)>0 else None

	def __repr__(self):
		lines = []
		lines.append("-"*5 + "OrderBook" + "-"*5)

		lines.append("\nAsks:")
		asks = self.asks.copy()
		while len(asks) > 0:
			lines.append(str(asks.pop()))

		lines.append("\t"*3 + "Bids:")
		bids = list(reversed(self.bids.copy()))
		while len(bids) > 0:
			lines.append("\t"*3 + str(bids.pop()))

		lines.append("-"*20)
		return "\n".join(lines)
	
	def __len__(self):
		return len(self.asks) + len(self.bids)
