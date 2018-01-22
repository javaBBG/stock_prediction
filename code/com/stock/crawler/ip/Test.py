#encoding=utf8
import requests
import socket
socket.setdefaulttimeout(3)
file = "E:/stock/ip/proxy"
f = open(file)
lines = f.readlines()
proxys = []
for i in range(0,len(lines)):
    ip = lines[i].strip("\n").split("\t")
    proxy_host = "http://"+ip[0]+":"+ip[1]
    proxy_temp = {"http":proxy_host}
    proxys.append(proxy_temp)
url = "http://ip.chinaz.com/getip.aspx"
for proxy in proxys:
    try:
        res = requests.get(url,proxies=proxy)._content
        print(11,proxy)
    except Exception as e:
        print(22,e)
        continue