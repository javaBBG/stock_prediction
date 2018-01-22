#收集所有股票每日K线数据

import  os
import  pandas as pd

class CollectDay:
    concurrentDay = '2017-12-28'
    beginDay = '2004-01-01'
    yearEndStr = "-12-31"
    yearBeginStr = "-01-01"
    dayDataPath = "E:/stock/day/"


if __name__ == '__main__':
