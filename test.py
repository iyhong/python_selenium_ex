from selenium import webdriver
import os
from fp.fp import FreeProxy
from bs4 import BeautifulSoup


def go():
    os_path = os.getcwd()
    path = 'driver/chromedriver'
    print(os_path)
    print(os.path.join(os.getcwd(), path))
    # proxy = FreeProxy(timeout=0.5, rand=True).get()
    # proxy = FreeProxy(country_id=['HK']  ).get()
    # proxy = proxy[7:]
    # print(proxy)
    # free proxy 설정
    proxy = '14.37.69.97:3128'
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": proxy,
        "ftpProxy": proxy,
        "sslProxy": proxy,
        "proxyType": "MANUAL"
    }

    driver = webdriver.Chrome(os.path.join(os.getcwd(), path))
    # driver = webdriver.Chrome()
    # driver.get('https://www.google.com')
    driver.get('https://www.naver.com')
    print('test')


if __name__ == '__main__':
    go()