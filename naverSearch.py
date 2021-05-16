from selenium import webdriver
import os
from bs4 import BeautifulSoup
from fp.fp import FreeProxy
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

# pyinstaller 로 실행파일 만드는 명령어 (mac)
# pyinstaller --onefile --add-data "driver/chromedriver 2:./driver/" naverSearch.py
# pyinstaller 로 실행파일 만드는 명령어 (window)
# pyinstaller --onefile -w --add-data "driver/chromedriver 2;./driver/" naverSearch.py


def main():
    os_path = os.getcwd()
    path = 'driver/chromedriver 2'
    dir_path = os.path.dirname(os.path.realpath(__file__));
    print(os_path)
    print(os.path.join(path))
    print(os.path.join(os.getcwd(), path))
    print(os.path.abspath(__file__))
    # 실행파일의 절대경로 구하기
    print('절대경로')
    print(os.path.dirname(os.path.realpath(__file__)))
    # 상대경로 구하기
    print('상대경로')
    print(os.path.relpath(dir_path))
    print(os.path.join(dir_path, path))
    os.chdir(dir_path)
    print(os.getcwd())
    # 프록시 설정
    # proxy_setting()
    url = 'https://m.naver.com/'
    # url = 'https://google.com/'
    title_list = [
        'javascript async defer use strict',
        '텔레그램 봇 telegram bot 만들기',
        'ssh로 aws instance 접속',
        'AWS ubuntu Tomcat 에 WAR파일 배포하기',
        '레오폴드 fc750r 갈축 그라파이트',
        '[maven] 설치하기 / 환경변수 설정 (mac)',
        '크롬확장프로그램 현위치 날씨',
        '네이버페이 5분투자',
        '클레버이지뷰 맥북 거치대',
        '[spring] DB properties 파일 읽어오기',
        '맥북 ssh 비번없이 로그인하기 ssh-keygen & ssh-copy-id',
        '[javascript] jsencrypt RSA 암호화',
        'aws ec2 Amazon Linux git 설치',
        'aws ami 시스템 시간 확인 & 수정 하기',
        'aws에 git remote setup하기',
        'StringTokenizer Vs String.split()'
    ]
    # subtitle = '텔레그램 봇 telegram bot 만들기'
    subtitle = 'ssh로 aws instance 접속'
    keyword = 'loverman85'

    mobile_emulation = {
        "deviceMetrics": {"width": 480, "height": 900, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
    chrome_options = Options()
    # chrome_options.add_argument('headless')
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(os.path.join(dir_path, path), chrome_options=chrome_options)
    # driver = webdriver.Chrome(os.path.join(path), chrome_options=chrome_options)
    driver.implicitly_wait(10);
    subtitle = random.choice(title_list)
    print(subtitle)
    # 네이버 검색
    naver_search(driver, url, subtitle, keyword)
    time.sleep(5)
    # 최근에 열린 탭으로 전환
    driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    print('end')


# 네이버 검색
def naver_search(driver, url, subtitle, keyword):
    driver.get(url)
    driver.find_element_by_id('MM_SEARCH_FAKE').click()
    driver.find_element_by_id('query').send_keys(subtitle)
    driver.find_element_by_id('query').send_keys(Keys.ENTER)
    # VIEW 탭 클릭
    view_tab_click(driver)
    # 블로그클릭
    my_blog_click(driver, keyword)

    # 광고 클릭
    ad_click(driver)


# 블로그 들어가기 클릭
def my_blog_click(driver, keyword):
    view_list = driver.find_elements_by_css_selector(".bx._svp_item > div.total_wrap > a")
    # print(view_list)
    for blog in view_list:
        # print(blog)
        url = blog.get_attribute('href')
        # a = blog.find_element_by_xpath("//li[@class='bx']/div/a")
        # a = blog.find_elements_by_tag_name('a')
        str_url = str(url)
        # print(url)
        if str_url.find(keyword) >= 0:
            blog.click()
            return
    print('No search result at naver')


# 네이버 검색결과에서 VIEW 탭 클릭
def view_tab_click(driver):
    tabs = driver.find_elements_by_css_selector('ul.api_list_scroll.lst_sch > li.bx')
    for tab in tabs:
        a_tag = tab.find_element_by_css_selector('a')
        text = a_tag.find_element_by_css_selector('span').text
        if text == 'VIEW':
            a_tag.click()
            break


# 블로그에서 광고 클릭
def ad_click(driver):
    driver.refresh()
    try:
        div = driver.find_element_by_id("ssp-adda")
    except NoSuchElementException:
        print('no ad!!')
        return
    # iframe 으로 전환
    # driver.switch_to.frame("id 또는 name")
    # print(div.find_elements_by_tag_name("iframe"))
    try:
        driver.switch_to.frame(div.find_elements_by_tag_name("iframe")[0].get_attribute('id'))
    except NoSuchElementException:
        print('no iframe!!')
    finally:
        a = driver.find_element_by_tag_name('a')
    # print(a.get_attribute('href'))
    a.click()


# 프록시 셋팅
def proxy_setting():
    proxy = FreeProxy(timeout=0.5, rand=True).get()
    # proxy = FreeProxy().get()
    proxy = proxy[7:]
    print(proxy)
    # free proxy 설정
    # proxy = '181.30.60.147:8080'
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": proxy,
        "ftpProxy": proxy,
        "sslProxy": proxy,
        "proxyType": "MANUAL"
    }


if __name__ == '__main__':
    main()

