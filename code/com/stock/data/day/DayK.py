import tushare as ts
import  pandas as pd
import shutil
import os
import time
#每日K线
class DayK:
    # concurrentDay = time.strftime("%Y-%m-%d")
    concurrentDay = '2017-12-28'
    beginDay = '2004-01-01'
    yearEndStr = "-12-31"
    yearBeginStr = "-01-01"
    dayDataPath = "E:/stock/day/"

    @staticmethod
    def downStockHisData(code,begin=beginDay,end=concurrentDay):
        endYear = int(end[0:4])
        startYear = int(begin[0:4])
        gap = endYear - startYear
        for inc in range(0, gap + 1):
            if inc == 0:
                downBegin = begin
                downEnd   = str(startYear) + DayK.yearEndStr
            elif inc == gap:
                downBegin = str(endYear) + DayK.yearBeginStr
                downEnd   = end
            else:
                conYear = startYear + inc
                downBegin = str(conYear) + DayK.yearBeginStr
                downEnd   = str(conYear) + DayK.yearEndStr
            codePath = DayK.dayDataPath +code
            if not os.path.exists(codePath):
                os.mkdir(codePath)
            fileName =codePath + "/"+ code + "_" + downBegin.replace("-", "") + "_" + downEnd.replace("-",
                                                                                                          "") + ".csv"
            exists = os.path.exists(fileName)
            size = 0
            if not exists:
                historyYear = ts.get_hist_data(code,downBegin,downEnd)
                if historyYear is None:
                    size = 0
                else:
                    size = historyYear.size
            if size != 0:
                historyYear.to_csv(fileName)

    @staticmethod
    def downStockHisDataAll(code, begin=beginDay, end=concurrentDay):
        codePath = DayK.dayDataPath + code
        if not os.path.exists(codePath):
            os.mkdir(codePath)
        fileName = codePath + "/" + code + "_" + begin.replace("-", "") + "_" + end.replace("-",
                                                                                                        "") + ".csv"
        exists = os.path.exists(fileName)
        size = 0
        try:
            if not exists:
                conns = ts.get_apis()
                historyYear = ts.bar(code,conn=conns,freq='D',start_date=begin, end_date=end,ma=[5, 10, 20], factors=['vr', 'tor'])
                print(code + ","+ begin + ","+ end)
                if historyYear is None:
                    size = 0
                else:
                    size = historyYear.size
                if size != 0:
                    historyYear.to_csv(fileName)
            else:
                1
                # print('文件已经存在：' + fileName)
        except Exception as e:
            print('异常，删除文件夹：' + codePath)
            shutil.rmtree(codePath)
            if str(type(e)) != "<class 'OSError'>":
                time.sleep(1*30)
                DayK.downStockHisDataAll(code,begin,end)


if __name__ == '__main__':
    day = DayK()
    day.downStockHisData("000036")





