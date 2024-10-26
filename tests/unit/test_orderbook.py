from ordermatchinengine import *

def testInitialState():
    book = Orderbook()
    #Book should be empty to begin with
    assert len(book) == 0

    assert book.getBid() == None
    assert book.getAsk() == None
    
def testInsert():
    book = Orderbook()
    order = LimitOrder(0, Side.BUY, 10, 10)
    book.processOrder(order)
    assert len(book) == 1
    assert book.getBid() == 10
    assert book.getAsk() == None

def testExecution():
    book = Orderbook()
    order = LimitOrder(0, Side.BUY, 10, 10)
    book.processOrder(order)
    order = LimitOrder(1, Side.SELL, 10, 10)
    book.processOrder(order)

    assert len(book) == 0
    assert book.getBid() == None
    assert book.getAsk() == None

def testExecution_marmooli():
    book = Orderbook()
    order = LimitOrder(0, Side.SELL, 5, 105)
    book.processOrder(order)
    order = LimitOrder(0, Side.SELL, 5, 106)
    book.processOrder(order)
    order = LimitOrder(0, Side.BUY, 1, 105)
    trade = book.processOrder(order)
    assert len(book) == 2
    assert book.getBid() == None
    assert book.getAsk() == 105
    assert len(book.trades)==1
