from ordermatchinengine import Orderbook, LimitOrder, Side

from random import getrandbits, randint

# Benchmark
OB = Orderbook()
numOrders = 10**7
orders = []
for n in range(numOrders):
	if bool(getrandbits(1)):
		orders.append(LimitOrder(n, Side.BUY, randint(1, 200), randint(1, 4)))
	else:
		orders.append(LimitOrder(n, Side.SELL, randint(1, 200), randint(1, 4)))

from time import time
start = time()
for order in orders:
	OB.process_order(order)
end = time()
totalTime = (end-start)
print("Time: " + str(totalTime))
print("Time per order (us): " + str(1000000*totalTime/numOrders))
print("Orders per second: " + str(numOrders/totalTime))

"""
Output
Time: 25.271270990371704
Time per order (us): 2.5271270990371706
Orders per second: 395706.25489354995
"""
