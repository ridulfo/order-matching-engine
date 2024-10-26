from ordermatchinengine import *

def testInitialState():
    book = Orderbook()
    #Book should be empty to begin with
    assert len(book) == 0

    assert book.get_bid() == None
    assert book.get_ask() == None
    
def testInsert():
    book = Orderbook()
    order = LimitOrder(0, Side.BUY, 10, 10)
    book.process_order(order)
    assert len(book) == 1
    assert book.get_bid() == 10
    assert book.get_ask() == None

def testExecution():
    book = Orderbook()
    order = LimitOrder(0, Side.BUY, 10, 10)
    book.process_order(order)
    order = LimitOrder(1, Side.SELL, 10, 10)
    book.process_order(order)

    assert len(book) == 0
    assert book.get_bid() == None
    assert book.get_ask() == None

def testExecution_marmooli():
    book = Orderbook()
    order = LimitOrder(0, Side.SELL, 5, 105)
    book.process_order(order)
    order = LimitOrder(0, Side.SELL, 5, 106)
    book.process_order(order)
    order = LimitOrder(0, Side.BUY, 1, 105)
    trade = book.process_order(order)
    assert len(book) == 2
    assert book.get_bid() == None
    assert book.get_ask() == 105
    assert len(book.trades)==1
