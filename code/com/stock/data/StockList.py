#获取2017-12-31年之前的股票代码
import tushare as ts
import  pandas as pd
import os
class StockList:
    stocksFile = 'E:/stock/stocks.csv'
    stocksMap = {}

    @staticmethod
    def initStockCodes():
        exists = os.path.exists(StockList.stocksFile)
        if not exists:
            stocksData = ts.get_stock_basics()
            stocksData.to_csv(StockList.stocksFile)
        stocks = pd.read_csv('E:/stock/stocks.csv')
        stocksArr = stocks.code.values
        # 股票数据补全
        for stock in stocksArr:
            stock = str(stock)
            codeLen = len(stock)
            if codeLen == 1:
                stock = '00000' + stock
            elif codeLen == 2:
                stock = '0000' + stock
            elif codeLen == 3:
                stock = '000' + stock
            elif codeLen == 4:
                stock = '00' + stock
            elif codeLen == 5:
                stock = '0' + stock
            if not StockList.stocksMap.__contains__(stock):
                StockList.stocksMap[stock] = ""

    @staticmethod
    def getStockCodes():
        if StockList.stocksMap.__len__() == 0:
            StockList.initStockCodes()
        return list(StockList.stocksMap.keys())


if __name__ == '__main__':
    list = StockList.getStockCodes()
    i = 0
    for str in  list:
        i= i + 1
        print(str)
        if i > 10: break
    print(list[0:5])






# if __name__ == '__main__':
#     #获取上市的股票
#     #stocks = ts.get_stock_basics()
#     # stocks.to_csv('E:/stock/stocks.csv')
#     s = pd.read_csv('E:/stock/stocks.csv')
#     print(type(s))
    # print(s.0)
    # for index,row in  s.iterrows():
    #     print()
    # d = ts.get_hist_data('600848')
    # h = d.tail(3)
    # print(h)

