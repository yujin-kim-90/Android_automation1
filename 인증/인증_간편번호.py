#인증 > 간편번호(휴대폰 인증)
#import OpenCV
import pytest
import time
# import os
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import common
from 변수 import 변수
from 변수 import 변수_인증

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
    )
    appium_server_url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.press_keycode(3)
    yield driver
    driver.quit()

#tc_id: log_20
def test_case_01(driver)->None:
    driver.find_element(By.XPATH, 변수.운영앱).click()
    time.sleep(20)
    driver.find_element(By.ID, 변수.시작하기_로그인Id).click()
    time.sleep(10)
    driver.find_element(By.ID, 변수.로그인id).click()
    time.sleep(3)

    assert driver.find_element(By.ID, 변수_인증.간편번호설정문구확인id).text == "간편번호 설정"

#tc_id: log_22
def test_case_02(driver)->None:
    time.sleep(3)
    common.휴대폰인증(driver)
    time.sleep(10)
    assert driver.find_element(By.ID, 변수_인증.간편번호설정문구확인id).text == "간편번호 설정"

#tc_id: log_23
def test_case_03(driver)->None:
    common.간편번호설정(driver)

    driver.find_element(By.ID, 변수.지문등록시트_x버튼).click()
    time.sleep(10)

    # driver.save_screenshot(OpenCV.test_screenshot(OpenCV.test()))
    # name= 'card_setting_1.png'
    # driver.tap([OpenCV.Matching.detectimage(driver, name)])
    # name= 'card_setting_2.png'
    # driver.tap([OpenCV.Matching.detectimage(driver, name)])
    # time.sleep(10)
    #
    # driver.find_element(By.ID, 변수_인증.ars인증요청id).click()
    #
    # time.sleep(10)
    #
    # driver.find_element(By.ID, 변수_인증.로카페이반팝업종료id).click()
    # str1=driver.find_element(By.XPATH, 변수_인증.로카페이타이틀확인).text
    #
    # assert str1=="로카페이"

def test_case_04(driver)->None:
    driver.find_element(By.ID, 변수_인증.로카페이등록페이지종료).click()
    time.sleep(10)
    str1=driver.find_element(By.XPATH, 변수_인증.홈확인).text

    assert str1=="홈"




