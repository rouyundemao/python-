from urllib.request import urlopen

url = 'http://www.baidu.com'

resp = urlopen(url)
# print(resp.read().decode('utf-8'))   # 拿到页面源代码

with open("mybaidu.html", mode='w', encoding='UTF-8') as f:
    f.write(resp.read().decode('utf-8'))
