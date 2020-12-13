from selenium import webdriver
import os
from bs4 import BeautifulSoup
from fp.fp import FreeProxy


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    os_path = os.getcwd()
    path = 'driver/chromedriver'
    print(os_path)
    print(os.path.join(os.getcwd(), path))

    # proxy = FreeProxy(timeout=0.5, rand=True).get()
    proxy = FreeProxy().get()
    proxy = proxy[7:]
    print(proxy)
    # free proxy 설정
    # PROXY = '181.30.60.147:8080'
    # webdriver.DesiredCapabilities.CHROME['proxy'] = {
    #     "httpProxy": proxy,
    #     "ftpProxy": proxy,
    #     "sslProxy": proxy,
    #     "proxyType": "MANUAL"
    # }

    driver = webdriver.Chrome(os.path.join(os.getcwd(), path))
    # driver = webdriver.Chrome()
    driver.get('https://m.blog.naver.com/loverman85/222144352446')
    driver.refresh()
    print(driver)
    div = driver.find_element_by_id("ssp-adda")

    print(div.find_elements_by_tag_name("iframe")[0].get_attribute('id'))

    # iframe 으로 전환
    # driver.switch_to.frame("id 또는 name")
    driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0].get_attribute('id'))
    a = driver.find_element_by_tag_name('a')
    r = a
    a.click()
    soup = BeautifulSoup(r, 'html.parser')
    print(soup)
    # sf_body = driver.find_element_by_class_name('sf_body')
    # print(sf_body)
    # print(sf_body.find_element_by_tag_name('a'))


if __name__ == '__main__':
    print_hi('PyCharm')

