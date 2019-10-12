## 1. selenium基本使用

+ 打开浏览器
```python
# encoding: utf-8

from selenium import webdriver
import time

driverPath = r'F:\software\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driverPath)

driver.get('https://www.qq.com/')

time.sleep(5)

# 关闭当前的标签页面
# driver.close()

# 关闭整个浏览器
driver.quit()

```

+ 查找元素，输入信息

```python
# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driverPath = r'F:\software\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driverPath)

driver.get('https://www.baidu.com/')

inputTag = driver.find_elements(By.CSS_SELECTOR, '#kw')[0]

print(inputTag)

inputTag.send_keys('python')

time.sleep(3)

inputTag.clear()
```

+ 登录豆瓣网

```python
# encoding: utf-8

from selenium import webdriver
import time

driverPath = r'F:\software\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driverPath)

driver.get('https://www.douban.com/')

email = driver.find_element_by_id('form_email')
email.send_keys('xxxx@xxx.com')

password = driver.find_element_by_id('form_password')
password.send_keys('xxxxxxx')

rememberBtn = driver.find_element_by_name('remember')
rememberBtn.click()

loginBtn = driver.find_element_by_class_name('bn-submit')
loginBtn.click()

```

+ 使用select下拉框

```python
# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driverPath = r'F:\software\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driverPath)

driver.get('https://www.dobai.com/')

selectBtn = Select(driver.find_element_by_name('jumpMenu'))
selectBtn.select_by_index(1)
```

+ 行为链

```python
# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driverPath = r'F:\software\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driverPath)

driver.get('https://www.baidu.com/')

inputTag = driver.find_element_by_id('kw')
submitBtn = driver.find_element_by_id('su')

actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag, '大爷')
actions.move_to_element(submitBtn)
actions.click(submitBtn)
actions.perform()
```

+ 操作cookie

```python
# encoding: utf-8

from selenium import webdriver

driverPath = r'F:\software\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driverPath)

driver.get('https://www.baidu.com/')

# 获取所有cookie
for cookie in driver.get_cookies():
    print('cookie: ', cookie)

# 获取某一个cookie
print(driver.get_cookie('PSTM'))

# 删除某一个cookie
driver.delete_cookie('PSTM')

# 删除所有的cookies
driver.delete_all_cookies()
print(driver.get_cookie('PSTM'))
```

+ 等待

> 页面等待，如果页面上的dom元素还没有加载出来，但是代码直接使用了这个dom元素，那么就会抛出NullPointer的异常，为了解决这个问题，可以使用等待方式，一种是隐式等待，一种是显式等待

> 隐式等待，调用driver,implicitly_wait，在获取不可用的元素之前，Juin先等待10秒钟

> 显式等待，显示等待表明某一个条件成立后才执行获取元素的操作，也可以在等待的时候指定一个最大的时间，如果超过这个最大的时间，就会抛出一个异常，显示等待应该使用selenium.webdriver.support.excepted_conditions期望条件和selenium.webdriver.support.ui.WebDriverWait来配合完成

+ 隐式等待

```python
# encoding: utf-8

from selenium import webdriver

driverPath = r'F:\software\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driverPath)

driver.implicitly_wait(10)

driver.get('https://www.baidu.com/')

```

+ 显式等待

```python
# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driverPath = r'F:\software\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driverPath)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By, 10, 'DynamicElementError'))
    )
finally:
    driver.quit()

driver.get('https://www.baidu.com/')
```

+ 其他等待方式
```
presence_of_element_located:某个元素已经加载完毕了
presence_of_all_element_located:网页中所有满足条件的元素都加载完毕了
element_to_be_cliable:某个元素可以点击了
```
