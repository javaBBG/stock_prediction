from com.stock.data.day.DayK import *
from com.stock.data.StockList import *

if __name__ == '__main__':
    #第一步获取股票
    sl = StockList.getStockCodes()
    # DayK.downStockHisDataAll('603655')
    for stock in sl:
        # time.sleep(1)
        DayK.downStockHisDataAll(stock)
        # DayK.downStockHisData(stock)
    print("end")
    # StockList.getStockCodes()
    # stocks = sl.getStockCodes()