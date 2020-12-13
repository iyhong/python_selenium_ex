from selenium import webdriver
import os
from bs4 import BeautifulSoup
from fp.fp import FreeProxy
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

# 네이버
# 레오폴드 fc750 그라파이트
# 클레버 이지뷰 맥북 거치대
# 네이버 페이 5분투자
#
# 구글
# 아마존 리눅스 docker jenkins
# java rsa string public key
# java 달력 만들기


def main():
    os_path = os.getcwd()
    path = 'driver/chromedriver'
    print(os_path)
    print(os.path.join(os.getcwd(), path))

    # 프록시 설정
    # proxy_setting()
    # url = 'https://m.naver.com/'
    url = 'https://google.com/'
    subtitle = 'java rsa string public key'
    keyword ='loverman85'

    mobile_emulation = {
        "deviceMetrics": {"width": 480, "height": 900, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(os.path.join(os.getcwd(), path), chrome_options=chrome_options)

    # 네이버 검색
    # naver_search(driver, url, subtitle, keyword)

    # 구글 검색
    try:
        google_search(driver, url, subtitle, keyword)
    except NoSuchElementException:
        print('NoSuchElementException')
    time.sleep(3)

    # 최근에 열린 탭으로 전환
    driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    print('end')


def google_search(driver, url, subtitle, keyword):
    driver.get(url)
    driver.find_element_by_css_selector('.gLFyf').send_keys(subtitle)
    driver.find_element_by_css_selector('.gLFyf').send_keys(Keys.ENTER)
    result_list = driver.find_elements_by_css_selector('div#rso > div')
    my_blog_click_google(result_list, keyword)
    # 광고 클릭
    ad_click(driver)


def my_blog_click_google(result_list, keyword):
    for one in result_list:
        print(one)
        a_tag = one.find_element_by_css_selector('a.C8nzq.BmP5tf')
        a_url = a_tag.get_attribute('href')
        print(a_url)
        if str(a_url).find(keyword) >= 0:
            a_tag.click()
            break
    print('No search result at google')


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
    print(view_list)
    for blog in view_list:
        print(blog)
        url = blog.get_attribute('href')
        # a = blog.find_element_by_xpath("//li[@class='bx']/div/a")
        # a = blog.find_elements_by_tag_name('a')
        str_url = str(url)
        print(url)
        if str_url.find(keyword) >= 0:
            blog.click()
            break
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
    div = driver.find_element_by_id("ssp-adda")
    try:
        # iframe 으로 전환
        # driver.switch_to.frame("id 또는 name")
        driver.switch_to.frame(div.find_elements_by_tag_name("iframe")[0].get_attribute('id'))
        a = driver.find_element_by_tag_name('a')
    except IndexError:
        a = div.find_element_by_tag_name('a')
    finally:
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

