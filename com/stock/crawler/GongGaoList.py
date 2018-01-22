import json
import time
import os
import requests
class GongGaoList:
    url = "http://data.eastmoney.com/notices/stock/600158.html"
    newsPath = "E:/stock/news/"

    @staticmethod
    def getNoticList(code):
        page = 1
        pageSize = 50
        codeNewPath = GongGaoList.newsPath + "/" + code + ".txt"
        #文件存在则不抓取
        if os.path.exists(codeNewPath):
            return
        output = open(codeNewPath, 'w+')
        while (1):
            time.sleep(1 * 2)
            url = "http://data.eastmoney.com/notices/getdata.ashx?StockCode=" + code + "&CodeType=1&PageIndex=" + str(
                page) + "&PageSize=" + str(pageSize)
            page = page + 1
            print("开始获取(%s)内容" % url)
            response = requests.get(url)
            content = response._content.decode("gbk")
            begin = content.index('{')
            res = content[begin:-1]
            js = json.loads(res)
            dataList = js.get('data')
            for dict in dataList:
                Url = dict['Url']
                title = dict['NOTICETITLE']
                typeName = dict['ANN_RELCOLUMNS'][0]['COLUMNNAME']
                noticeDate = dict['NOTICEDATE']
                output.write(Url + " " + title + " " + typeName + " " + noticeDate + '\n')
            print("获取网页内容完毕")
            if dataList.__len__() < pageSize:
                break

        output.close()







if __name__ == '__main__':
    total = 123
    page = 1
    pageSize  = 50
    while(1):
        a = (page - 1) * pageSize + 1
        b = a + pageSize - 1
        print(str(a) + "~" + str(b))
        page = page + 1
        if(b > total):
            break
    # for i in range(int(total/pageSize)):
    #     a = (page-1 + i) * pageSize
    #     b = (page + i )* pageSize
    #     print(str(a) + "~" + str(b))

    # code = '600158'
    # page = str(1)
    # pageSize = str(2)
    # url = "http://data.eastmoney.com/notices/getdata.ashx?StockCode="+code+"&CodeType=1&PageIndex="+page+"&PageSize="+pageSize
    # print("开始获取(%s)内容" % url)
    # response = requests.get(url)
    # print("获取网页内容完毕")
    # content = response._content.decode("gbk")
    # content.index('{')
    # res = content[7:-1]
    # js = json.loads(res)
    # TotalCount = js.get('TotalCount')
    # pages = js.get('pages')
    # dataList = js.get('data')
    # codeNewPath = GongGaoList.newsPath + "/" + code+".txt"
    # output = open(codeNewPath, 'w+')
    # for dict in dataList:
    #     Url = dict['Url']
    #     title = dict['NOTICETITLE']
    #     typeName = dict['ANN_RELCOLUMNS'][0]['COLUMNNAME']
    #     noticeDate = dict['NOTICEDATE']
    #     output.write(Url + " " + title + " " + typeName + " " + noticeDate +'\n')
    # output.close()





