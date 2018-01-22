from com.stock.crawler.GongGaoList import *
from com.stock.data.StockList import *

if __name__ == '__main__':
    #第一步获取股票
    sl = StockList.getStockCodes()
    # DayK.downStockHisDataAll('603655')
    for stock in sl:
        # time.sleep(1)
        GongGaoList.getNoticList("000726")
        time.sleep(1 * 5)
        # DayK.downStockHisData(stock)
        break
    print("end")
    # StockList.getStockCodes()
    # stocks = sl.getStockCodes()