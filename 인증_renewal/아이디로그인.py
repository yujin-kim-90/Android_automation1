#인증renewal > 간편번호(휴대폰 인증)
#import OpenCV
import pytest
import time
# import os
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import common
from 변수 import 변수
from 변수 import 변수_인증
from 변수 import 변수_인증renewal
from 변수 import secure_keypad

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

def test_아이디로그인진입(driver)->None:
    driver.find_element(By.XPATH, 변수.운영앱).click()
    time.sleep(10)
    driver.find_element(By.ID, 변수_인증renewal.아이디로그인버튼).click()
    time.sleep(10)
    driver.find_element(By.ID, 변수_인증renewal.아이디비밀번호설정).click()

def test_카드인증(driver)->None:
    time.sleep(3)
    common.카드인증(driver)
def test_비밀번호설정(driver)-> None: #비밀번호 :1r2r3r4r!
    #driver.find_element(By.ID, 변수_인증.아이디입력id).send_keys("aaaqwww1")
    driver.find_element(By.ID, 변수_인증.비번입력id).click()
    common.비밀번호입력(driver)
    driver.find_element(By.ID, 변수_인증.비번확인id).click()
    common.비밀번호입력(driver)
    driver.find_element(By.ID, 변수_인증.확인버튼id).click()
    time.sleep(5)
    driver.find_element(By.ID, 변수_인증.아이디비번확인버튼id).click()

def test_아이디로그인(driver)->None:
    time.sleep(5)
    driver.find_element(By.ID, 변수_인증.로그인아이디id).send_keys("aaaqwww1")
    driver.find_element(By.ID, 변수_인증.로그인비번id).click()
    common.비밀번호입력(driver)
    # time.sleep(10)
    # str1=driver.find_element(By.XPATH, 변수_인증renewal.홈text).text
    # assert str1=='홈'
