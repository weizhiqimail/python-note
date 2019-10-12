+ url的前进与后退

```python
# encoding: utf-8

from selenium import webdriver
import os
import time

driverPath = r'D:\chromedriver\chromedriver.exe'

if 'HTTP_PROXY' in os.environ:
    del os.environ['HTTP_PROXY']

driver = webdriver.Chrome(executable_path=driverPath)

urlA = 'http://www.taobao.com'
print('urlA: ', urlA)
driver.get(urlA)
time.sleep(3)

urlB = 'http://www.baidu.com'
print('urlB: ', urlB)
driver.get(urlB)
time.sleep(3)

print('back to urlA: ', urlA)
driver.back()
time.sleep(3)

print('forward to urlB: ', urlB)
driver.forward()
time.sleep(3)

driver.quit()
```
+ 切换页面

```python
# encoding: utf-8

from selenium import webdriver

driverPath = r'F:\software\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driverPath)

driver.get('https://www.baidu.com/')

# 打开新标签页面
driver.execute_script('window.open("http://www.douban.com")')

# 虽然打开了豆瓣页面，但是此时driver的url还是百度的url
print(driver.current_url)

# 切换页面
driver.switch_to.window(driver.window_handles[1])

# 此时是豆瓣的url地址
print(driver.current_url)

# 获取页面的源代码
print(driver.page_source)
```
+ 代理IP

```python
# encoding: utf-8

from selenium import webdriver

driverPath = r'F:\software\chromedriver\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://202.107.195.217:80')

driver = webdriver.Chrome(executable_path=driverPath, chrome_options=options)

driver.get('http://httpbin.org/ip')
```

+ webelement

```python
# encoding: utf-8

from selenium import webdriver

driverPath = r'F:\software\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driverPath)

driver.get('https://www.taobao.com')

# submitBtn = driver.find_element_by_id('su')

# print(type(submitBtn))

# print(submitBtn.get_attribute('value'))

driver.save_screenshot('a.png')
```