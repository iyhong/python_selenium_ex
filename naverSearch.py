from selenium import webdriver
import os
from bs4 import BeautifulSoup
from fp.fp import FreeProxy
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException


def main():
    os_path = os.getcwd()
    path = 'driver/chromedriver'
    print(os_path)
    print(os.path.join(os.getcwd(), path))

    # 프록시 설정
    # proxy_setting()
    # url = 'https://m.naver.com/'
    url = 'https://google.com/'
    subtitle = '아마존 리눅스 docker jenkins'
    keyword ='loverman85'
    driver = webdriver.Chrome(os.path.join(os.getcwd(), path))

    # 네이버 검색
    # naver_search(driver, url, subtitle, keyword)

    # 구글 검색
    google_search(driver, url, subtitle, keyword)
    time.sleep(3)

    # 최근에 열린 탭으로 전환
    driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    print('end')


def google_search(driver, url, subtitle, keyword):
    driver.get(url)
    driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(subtitle)
    driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)
    result_list = driver.find_elements_by_css_selector('div.hlcw0c')
    my_blog_click_google(result_list, keyword)
    # 광고 클릭
    ad_click(driver)


def my_blog_click_google(result_list, keyword):
    for one in result_list:
        a_tag = one.find_element_by_css_selector('div.g > div.rc > div.yuRUbf > a')
        a_url = a_tag.get_attribute('href')
        print(a_url)
        if str(a_url).find(keyword):
            a_tag.click()
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
    div = driver.find_element_by_id("ssp-adda")
    print(div.find_elements_by_tag_name("iframe")[0].get_attribute('id'))
    # iframe 으로 전환
    # driver.switch_to.frame("id 또는 name")
    driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0].get_attribute('id'))
    a = driver.find_element_by_tag_name('a')
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

