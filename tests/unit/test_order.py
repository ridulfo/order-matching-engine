from ordermatchinengine import *

def test_initialStates():
    order = Order(1)
    assert isinstance(order.order_id, int)
    assert isinstance(order.time, int)
    assert order.order_id == 1


    order = CancelOrder(1)
    assert isinstance(order.order_id, int)
    assert isinstance(order.time, int)
    assert order.order_id == 1
    

    order = MarketOrder(1, Side.BUY, 10)
    assert isinstance(order.order_id, int)
    assert isinstance(order.time, int)
    assert order.order_id == 1
    assert order.side == Side.BUY
    assert order.size == 10

    order = LimitOrder(1, Side.BUY, 10, 100)
    assert isinstance(order.order_id, int)
    assert isinstance(order.time, int)
    assert order.order_id == 1
    assert order.side == Side.BUY
    assert order.size == 10
    assert order.price == 100


