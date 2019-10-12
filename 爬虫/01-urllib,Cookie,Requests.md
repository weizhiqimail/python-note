## 1. urllib

#### 1.1 urlopen()

```python
from urllib import requests

data = requests.urlopen('http://www.baidu.com').read('utf-8')

print(data)
```

#### 1.2 urlretrieve()
将网页的一个文件保存到本地

```python
from urllib import requests

requests.urlretrieve('http://www.baidu.com', 'baidu.html')
```

#### 1.3 urlencode()
使用代码发送请求，必须手动进行编码，需要使用`urlencode`函数来实现

```python
from urllib import parse

data = {'name': '小明', 'home': '上海市宝山区'}

qs = parse.urlencode(data)

print(qs)
```

#### 1.4 parae_qs()
将经过编码后的url参数进行解码，解析的字典的value的值是一个list
```python
from urllib import parse

qs = parse.parse_qs('name=%E5%B0%8F%E6%98%8E&home=%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%AE%9D%E5%B1%B1%E5%8C%BA')

print(qs)
```

#### 1.5 urlparse和urlsplit

```python
from urllib import parse

url = 'https://play.google.com/store/newsstand/news/Khaleej_Times?id=CAowuqefCQ'
q = parse.urlparse(url)
s = parse.urlsplit(url)
print(q)
print(s)
print(q.scheme)
print(q.netloc)
print(q.path)
print(q.params) # urlsplit没有这个属性
print(q.query)
print(q.fragment)
```

#### 1.6 Cookie
使用`cookielib`库和`HTTPCookieProcessor`模拟登陆
+ 在请求头添加`Cookie`信息

```python
# encoding: utf-8

from urllib import request, parse

url = 'http://www.renren.com/880151247/profile'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Cookie': 'anonymid=jkbzzgim-b5qk9c; depovince=GW; _r01_=1; ick_login=ebc64b2c-420f-4be8-8e7b-a5e3910890c6; t=83c0b343edf8e18f2ef8f888ddd4c9f91; societyguester=83c0b343edf8e18f2ef8f888ddd4c9f91; id=967238831; xnsid=7547a4f; jebecookies=c26cc093-ded9-40b1-8a49-0e901a08a0e4|||||; JSESSIONID=abcjYy0j_S6DKbBt4Q4tw; wp_fold=0; ver=7.0; loginfrom=null; wp=0'
}

req = request.Request(url=url, headers=headers)

res = request.urlopen(req).read().decode('utf-8')

with open('renren.html', 'w', encoding='utf-8') as fp:
    fp.write(res)

```

+ `http.cookirjar`模块
该模块主要有的类有`CookieJar`，`FileCookieJar`，`MozillaCookieJar`和`LWPCookieJar`
    - `CookieJar`管理HTTP Cookie的值，存储HTTP请求生成的cookie，向传出的HTTP请求添加cookie对象，整个cookie都存储在内存中，对`CookieJar`实例进行垃圾回收后cookie也将丢失
    - `FileCookieJar(Filename, delayload=None,policy=None)`从`CookieJar`派生而来，用来创建FileCookieJar实例，检错cookie信息并且将cookie存储到文件中。Filename是存储cookie的文件名，delayload为True时支持延迟访问文件，即只有在需要的时候才读取文件或在文件中存储数据。
    - `MozillaCookieJar(filename, delayload=None,policy=None)`从FileCookieJar派生而来，创建与Mozilla浏览器cookies.txt兼容的FileCookieJar实例
    - `LWPCookieJar(filename,delayload=None,policy=None)`从FileCookieJar派生而来，创建与libwww-per标准的Set-Cookie3文件格式兼容的FileCookieJar实例

```python
# encoding: utf-8
from urllib import request, parse
from http.cookiejar import CookieJar

loginUrl = 'http://www.renren.com'
dapengUrl = 'http://www.renren.com/880151247/profile'
# 创建一个cookiejar对象
cookiejar = CookieJar()

# 使用cookiejar创建一个HTTPCookieProcess对象
handler = request.HTTPCookieProcessor(cookiejar)

# 创建一个opener
opener = request.build_opener(handler)

# 使用opener发送登录请求
headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

data = {
    'email': '18770280716',
    'password': 'mima.63165855'
}

req = request.Request(loginUrl, data=parse.urlencode(data).encode('utf-8'), headers=headers)

opener.open(req)

# 访问个人主页，使用之前的opener
res = request.Request(dapengUrl, headers=headers)
resp = opener.open(res)
with open('renren.html', 'w', encoding='utf-8') as fp:
    fp.write(resp.read().decode('utf-8'))

```
+ 保存cookie到本地
把cookie信息保存到本地的cookie.txt文件中

```python
# encoding: utf-8
from urllib import request, parse
from http.cookiejar import MozillaCookieJar

cookiejar = MozillaCookieJar('cookie.txt')
cookiejar.load()
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

resp = opener.open('http://httpbin.org/cookies/set?name=jackkk')
print(resp)

cookiejar.save(ignore_discard=True)
for cookie in cookiejar:
    print(cookie)

```