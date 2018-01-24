from bs4 import BeautifulSoup
import requests
class GongGao:
    1


if __name__ == '__main__':
    code = '600158'
    url ='http://data.eastmoney.com/notices/detail/'+code+'/AN201202240003286734,JUU0JUI4JUFEJUU0JUJEJTkzJUU0JUJBJUE3JUU0JUI4JTlB.html'
    print("开始获取(%s)内容" % url)
    response = requests.get(url)
    print("获取网页内容完毕")
    soup = BeautifulSoup(response.content)
    #内容
    cont = soup.select(".cont_txt")[0]
    #公告日期
    date = cont.select(".detail-header")[0].find("div").find('span').text.replace(" ","")
    #公告内容
    detail = cont.select(".detail-body")[0].find("div").text.replace(" ","")
    print(detail)
    # 为了防止漏掉调用close方法，这里使用了with语句
    # 写入到文件中的编码为utf-8
    title = detail.split('\r')[0]
    fileName = code+"_"+title+"_"+date+".txt"

    with open(fileName, 'w') as f:
        print(detail)
        f.write(detail)


