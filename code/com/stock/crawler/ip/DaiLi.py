#encoding=utf8
import requests
import os
from bs4 import BeautifulSoup
import socket

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

def test(proxy):
    socket.setdefaulttimeout(1)
    url = "http://ip.chinaz.com/getip.aspx"
    try:
        requests.get(url,proxies=proxy)._content
        print("ok")
        return True
    except Exception as e:
        print(e)
        return False

def xicidaili():
    file = "E:/stock/ip/xicidaili"
    if os.path.exists(file):
        os.remove(file)
    f = open(file, "w")
    for index in range(1,2628):
        url = 'http://www.xicidaili.com/nn/'+str(index)
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.content)
        ips = soup.findAll('tr')
        for x in range(1, len(ips)):
            ip = ips[x]
            tds = ip.findAll("td")
            ip = tds[1].contents[0]
            port = tds[2].contents[0]
            proxy = {"http": "http://"+ip+":"+port}
            flag = test(proxy)
            if flag:
                ip_temp = ip + "\t" + port + "\n"
                f.write(ip_temp)
    f.close()

def sixsixip():
    file = "E:/stock/ip/66ip"
    if os.path.exists(file):
        os.remove(file)
    f = open(file, "w")
    for index in range(1,4):
        url = 'http://www.66ip.cn/areaindex_35/'+str(index)+'.html'
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.content)
        ips = soup.findAll('table')[2].findAll('tr')
        for x in range(1, len(ips)):
            ip = ips[x]
            tds = ip.findAll("td")
            ip = tds[0].contents[0]
            port = tds[1].contents[0]
            proxy = {"http": "http://"+ip+":"+port}
            flag = test(proxy)
            print(flag,type(flag))
            if flag:
                ip_temp = ip + "\t" + port + "\n"
                f.write(ip_temp)
    f.close()
if __name__ == '__main__':
    sixsixip()


